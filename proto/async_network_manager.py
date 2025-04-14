import asyncio
import socket
import struct
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncNetworkManager')

class AsyncNetworkManager:
    """异步网络管理器，处理网络连接和数据传输"""
    
    def __init__(self, host, port,robot_id,manager_id=None):
        self.host = host
        self.port = port
        self.robot_id = robot_id
        self.manager_id = manager_id or f"net_{id(self)}"  # 添加唯一标识
        self.reader = None                                           
        self.writer = None
        self.is_alive = False
        self.receive_callback = None
        self.connection_id = None
        self.last_activity = 0
        self.buffer = bytearray()  # 添加缓冲区
        self._receive_task = None  # 新增任务跟踪
        self._callback = None      # 使用私有属性存储回调
        
    async def connect(self):
        """异步连接到服务器"""
        try:
            self.reader, self.writer = await asyncio.open_connection(
                self.host, self.port)
            self.is_alive = True
            self.connection_id = f"{self.host}:{self.port}_{int(time.time())}"
            self.last_activity = time.time()
            logger.info(f"连接到服务器 {self.host}:{self.port} 成功")
            return True
        except Exception as e:
            logger.error(f"连接服务器失败: {str(e)}")
            self.is_alive = False
            return False
            
    async def close(self):
        """异步关闭连接"""
        if self.is_alive and self.writer:
            self.is_alive = False
            try:
                self.writer.close()
                await self.writer.wait_closed()
                logger.info("连接已关闭")
            except Exception as e:
                logger.error(f"关闭连接时出错: {str(e)}")
                
    async def send_data(self, data):
        """异步发送数据"""
        if not self.is_alive or not self.writer:
            logger.warning("尝试发送数据但连接未建立或已关闭")
            return False
            
        try:
            self.writer.write(data)
            await self.writer.drain()
            self.last_activity = time.time()
            return True
        except Exception as e:
            logger.error(f"发送数据失败: {str(e)}")
            self.is_alive = False
            return False
            
    async def receive_data(self, timeout=None):
        """异步接收数据，使用2字节头的缓冲区累积解包逻辑"""
        if not self.is_alive or not self.reader:
            return None
        
        try:
            # 1. 初始化缓冲区（如果尚未定义）
            if not hasattr(self, 'buffer'):
                self.buffer = bytearray()
            
            # 2. 读取可用数据（非精确读取）
            data = await asyncio.wait_for(self.reader.read(8192), timeout)
            
            if not data:
                logger.warning("服务器关闭了连接")
                self.is_alive = False
                return None
            
            # 3. 将新数据添加到缓冲区
            self.buffer.extend(data)
            self.last_activity = time.time()
            
            # 4. 处理完整消息包
            if len(self.buffer) >= 2:
                # 解析消息长度（前2个字节）
                msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                # 检查是否有完整的消息
                if len(self.buffer) >= msg_len + 2:
                    # 提取完整消息包
                    packet = bytes(self.buffer[:msg_len+2])
                    logger.info(f"{self.robot_id}收到完整消息: {packet}")
                    # 更新缓冲区，移除已处理的消息
                    self.buffer = self.buffer[msg_len+2:]
                    
                    # 日志记录 - 可以解析更多信息
                    if len(packet) >= 4:  # 如果包含协议ID
                        proto_id = int.from_bytes(packet[2:4], byteorder='big')
                        logger.debug(f"收到完整消息: 长度={msg_len}, 协议ID={proto_id}")
                    else:
                        logger.debug(f"收到完整消息: 长度={msg_len}")
                    
                    return packet
                else:
                    logger.debug(f"数据不足一个完整消息: 需要 {msg_len+2} 字节，当前有 {len(self.buffer)} 字节")
            
            # 没有完整消息，返回None
            return None
        
        except asyncio.TimeoutError:
            # 超时不是错误，只是当前没有数据
            return None
        except asyncio.IncompleteReadError:
            logger.warning("连接已关闭")
            self.is_alive = False
            return None
        except Exception as e:
            logger.error(f"接收数据失败: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_alive = False
            return None
            
    async def start_receive_loop(self, callback):
        """启动异步接收循环"""
        # 1. 存储独立的回调函数引用
        self._callback = callback
        
        # 2. 取消已有任务(如果存在)
        if self._receive_task and not self._receive_task.done():
            logger.debug(f"{self.manager_id}: 取消现有接收任务")
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass
        
        # 3. 创建新任务并添加任务名
        self._receive_task = asyncio.create_task(self._receive_loop()
        )
        
        # logger.info(f"{self.manager_id}: 启动接收任务 {self._receive_task.get_name()}")
        return self._receive_task
            
    async def _receive_loop(self):
        """异步接收循环"""
        logger.info(f"开始接收数据循环: {self.manager_id}")
        
        while self.is_alive:
            try:
                # 1. 读取一个完整的消息
                packet = await self.receive_data(timeout=1)
                
                # 2. 处理接收到的消息
                if packet and self._callback:
                    await self._callback(packet)
                
                # 3. 检查并处理缓冲区中的其他完整消息
                while hasattr(self, 'buffer') and len(self.buffer) >= 2:
                    msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                    if len(self.buffer) < msg_len + 2:
                        break  # 没有完整消息了
                    
                    # 提取下一个完整消息
                    next_packet = bytes(self.buffer[:msg_len+2])
                    self.buffer = self.buffer[msg_len+2:]
                    
                    # 如果有协议ID，记录日志
                    if len(next_packet) >= 4:
                        proto_id = int.from_bytes(next_packet[2:4], byteorder='big')
                        logger.debug(f"处理缓冲区附加消息: 长度={msg_len}, 协议ID={proto_id}")
                    
                    # 处理消息
                    if self.receive_callback:
                        await self.receive_callback(next_packet)
                
                # 4. 短暂休眠，避免CPU占用过高
                await asyncio.sleep(0.01)
                
            except Exception as e:
                logger.info(f"接收循环中出错: {str(e)}")
                
                if not self.is_alive:
                    break
                    
                # 短暂等待后继续
                await asyncio.sleep(1)
                
        logger.info("接收数据循环已结束")
        
    def get_connection_info(self):
        """获取连接信息"""
        return {
            "id": self.connection_id,
            "host": self.host,
            "port": self.port,
            "alive": self.is_alive,
            "last_activity": self.last_activity,
            "idle_time": time.time() - self.last_activity if self.last_activity else 0
        } 