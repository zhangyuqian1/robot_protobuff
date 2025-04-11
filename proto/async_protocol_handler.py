import asyncio
import logging
import concurrent.futures
from google.protobuf import message as pb_message
from proto_mapper import ProtobufMapper
from protocol_map import PROTOCOL_MAP_C2S, protocol_map
from Xor import XORCipher

logger = logging.getLogger('AsyncProtocolHandler')
class AsyncProtocolHandler:
    """异步协议处理器，处理协议的序列化与反序列化"""
    
    def __init__(self):
        self.proto_mapper = ProtobufMapper(cipher_cls=XORCipher)
        self.cipher = XORCipher()
        self.protocol_handlers = {}
        self._protobuf_initialized = False
        # 创建线程池执行器
        self._thread_pool = concurrent.futures.ThreadPoolExecutor()
        
    async def init_protobuf(self):
        """异步初始化protobuf相关配置"""
        if self._protobuf_initialized:
            return
            
        try:
            # 使用run_in_executor替代to_thread
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(self._thread_pool, self.proto_mapper.load_proto_files)
            self._protobuf_initialized = True
        except Exception as e:
            logger.error(f"加载proto文件失败: {str(e)}")
            raise
            
    async def register_handler(self, proto_id, handler):
        """注册协议处理函数 - 保持同步以兼容现有代码"""
        self.protocol_handlers[proto_id] = handler
        logger.debug(f"注册协议处理器: ID={proto_id}")
        
    async def serialize_message(self, protocol_id, data, is_client_proto=True):
        """异步序列化消息"""
        if not self._protobuf_initialized:
            await self.init_protobuf()
            
        try:
            # 获取协议名称
            message_name = PROTOCOL_MAP_C2S.get(protocol_id) if is_client_proto else protocol_map.get(protocol_id)
            if not message_name:
                raise ValueError(f"未知协议ID: {protocol_id}")

            # 使用run_in_executor替代to_thread
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(
                self._thread_pool, 
                lambda: self.proto_mapper.serialize_message(
                    message_name=message_name,
                    data=data,
                    is_server=not is_client_proto
                )
            )
        except Exception as e:
            logger.error(f"协议序列化失败: {str(e)}")
            raise
            
    async def create_packet(self, protocol_id, serialized_data):
        """异步创建完整数据包"""
        try:
            # XOR加密处理 - 保持原有逻辑
            loop = asyncio.get_event_loop()
            encrypted = await loop.run_in_executor(
                self._thread_pool,
                lambda: self.cipher.encode(protocol_id.to_bytes(2, 'big') + serialized_data)
            )
            
            # 构造完整数据包 - 保持原有的2字节长度头
            return len(encrypted).to_bytes(2, 'big') + encrypted
        except Exception as e:
            logger.error(f"创建数据包失败: {str(e)}")
            return None
        
    async def parse_packet(self, packet):
        """异步解析数据包"""
        if not self._protobuf_initialized:
            await self.init_protobuf()
            
        try:
            # 使用run_in_executor替代to_thread
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(
                self._thread_pool,
                lambda: self.proto_mapper.parse_packet_server(packet, is_server=True)
            )
        except Exception as e:
            logger.error(f"解析数据包失败: {str(e)}")
            return None, None, None
            
    async def dispatch_protocol(self, proto_id, data, proto_name):
        """异步协议分发"""
        handler = self.protocol_handlers.get(proto_id)
        if not handler:
            # logger.warning(f"未注册的协议处理: [{proto_id}]{proto_name}")
            return 
            
        try:
            # logger.info(f"处理协议[{proto_id}]{proto_name}")
            
            # 检查处理器是否是协程函数
            if asyncio.iscoroutinefunction(handler):
                # 直接调用异步处理器
                await handler(data)
            else:
                # 非异步处理器放在线程池中执行
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(self._thread_pool, handler, data)
                
        except Exception as e:
            logger.error(f"处理协议{proto_id}异常: {str(e)}")
            
    async def unpack_data(self, buffer):
        """异步解包数据，返回完整消息列表和剩余的缓冲区"""
        messages = []
        remaining = buffer
        
        # 特别保留原有的2字节头长度解包逻辑
        while len(remaining) >= 2:  # 至少需要2字节头
            # 读取消息长度
            msg_len = int.from_bytes(remaining[:2], byteorder='big')
            
            # 检查是否有完整消息
            if len(remaining) >= msg_len + 2:
                # 提取消息体 (不包括长度字段)
                message = remaining[2:msg_len+2]
                messages.append(message)
                
                # 移动到下一个消息
                remaining = remaining[msg_len+2:]
            else:
                # 消息不完整，等待更多数据
                break
        
        return messages, remaining
        
    async def process_message(self, message):
        """异步处理单个完整消息"""
        if not self._protobuf_initialized:
            await self.init_protobuf()
            
        try:
            # 解析消息
            parsed_data, proto_name, proto_id = await self.parse_packet(message)
            
            if parsed_data and proto_id:
                # 分发到对应的处理器
                await self.dispatch_protocol(proto_id, parsed_data, proto_name)
                return True
        except Exception as e:
            logger.error(f"处理消息异常: {str(e)}")
        
        return False
        
    def __del__(self):
        """析构函数，关闭线程池"""
        if hasattr(self, '_thread_pool'):
            self._thread_pool.shutdown(wait=False) 