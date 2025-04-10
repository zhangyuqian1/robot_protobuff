import struct
import logging
import asyncio
import traceback
from collections import defaultdict
import binascii

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncProtocolHandler')

class AsyncProtocolHandler:
    """异步协议处理器，处理游戏协议的序列化和反序列化"""
    
    def __init__(self):
        # 协议处理器映射表
        self.handlers = defaultdict(list)
        
    def register_handler(self, protocol_id, handler):
        """注册协议处理器"""
        self.handlers[protocol_id].append(handler)
        logger.debug(f"注册协议处理器: ID={protocol_id}")
        
    def unregister_handler(self, protocol_id, handler=None):
        """注销协议处理器"""
        if handler:
            if protocol_id in self.handlers:
                try:
                    self.handlers[protocol_id].remove(handler)
                except ValueError:
                    pass
        else:
            self.handlers[protocol_id] = []
            
    def serialize_message(self, protocol_id, data):
        """序列化消息"""
        try:
            # 将Protobuf对象序列化为二进制数据
            serialized_data = data.SerializeToString()
            return serialized_data
        except Exception as e:
            logger.error(f"序列化消息失败: ID={protocol_id}, 错误={str(e)}")
            logger.error(traceback.format_exc())
            return None
            
    def deserialize_message(self, protocol_id, data, message_class):
        """反序列化消息"""
        try:
            # 创建协议对象并解析二进制数据
            message = message_class()
            message.ParseFromString(data)
            return message
        except Exception as e:
            logger.error(f"反序列化消息失败: ID={protocol_id}, 错误={str(e)}")
            logger.error(f"数据: {binascii.hexlify(data)}")
            logger.error(traceback.format_exc())
            return None
            
    def create_packet(self, protocol_id, data):
        """创建数据包"""
        try:
            # 包结构: 总长度(4字节) + 协议ID(4字节) + 协议数据
            packet_length = len(data) + 4  # 协议ID占4字节
            header = struct.pack(">II", packet_length, protocol_id)
            return header + data
        except Exception as e:
            logger.error(f"创建数据包失败: {str(e)}")
            return None
            
    def parse_packet(self, packet):
        """解析数据包"""
        try:
            if len(packet) < 8:  # 至少需要8字节(长度+协议ID)
                logger.warning(f"包数据不完整: {len(packet)}字节")
                return None, None, None
                
            # 解析包头
            length_bytes = packet[0:4]
            pid_bytes = packet[4:8]
            
            packet_length = struct.unpack(">I", length_bytes)[0]
            protocol_id = struct.unpack(">I", pid_bytes)[0]
            
            # 检查包长度
            if len(packet) != packet_length + 4:  # +4是因为长度字段本身
                logger.warning(f"包长度不匹配: 预期={packet_length+4}, 实际={len(packet)}")
                return None, None, None
                
            # 获取协议数据
            protocol_data = packet[8:]
            
            # 获取协议名称
            from protocol_map_static import ProtocolMap
            protocol_name = ProtocolMap.get_name(protocol_id)
            
            return protocol_data, protocol_name, protocol_id
            
        except Exception as e:
            logger.error(f"解析数据包失败: {str(e)}")
            logger.error(traceback.format_exc())
            return None, None, None
            
    async def dispatch_protocol(self, protocol_id, data, protocol_name=None):
        """异步分发协议处理"""
        if protocol_id not in self.handlers:
            return False
            
        try:
            # 获取协议处理器
            handlers = self.handlers[protocol_id]
            
            # 分发到所有注册的处理器
            tasks = []
            for handler in handlers:
                # 检查处理器是否是异步函数
                if asyncio.iscoroutinefunction(handler):
                    tasks.append(asyncio.create_task(handler(data)))
                else:
                    # 如果处理器是同步函数，使用线程池执行
                    loop = asyncio.get_event_loop()
                    tasks.append(loop.run_in_executor(None, handler, data))
                    
            # 等待所有处理任务完成
            if tasks:
                await asyncio.gather(*tasks, return_exceptions=True)
                
            return True
            
        except Exception as e:
            logger.error(f"分发协议处理失败: ID={protocol_id}, 错误={str(e)}")
            logger.error(traceback.format_exc())
            return False 