import asyncio
import socket
import struct
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncNetworkManager')

class AsyncNetworkManager:
    """异步网络管理器，处理网络连接和数据传输"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None
        self.is_alive = False
        self.receive_callback = None
        self.connection_id = None
        self.last_activity = 0
        
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
        """异步接收数据"""
        if not self.is_alive or not self.reader:
            return None
            
        try:
            # 读取4字节的头部，表示包长度
            header_data = await asyncio.wait_for(
                self.reader.readexactly(4), timeout)
            if not header_data or len(header_data) < 4:
                return None
                
            # 解析包长度
            packet_length = struct.unpack(">I", header_data)[0]
            
            # 读取包体
            packet_data = await asyncio.wait_for(
                self.reader.readexactly(packet_length), timeout)
            
            self.last_activity = time.time()
            return header_data + packet_data
            
        except asyncio.TimeoutError:
            return None
        except asyncio.IncompleteReadError:
            logger.warning("连接已关闭")
            self.is_alive = False
            return None
        except Exception as e:
            logger.error(f"接收数据失败: {str(e)}")
            self.is_alive = False
            return None
            
    async def start_receive_loop(self, callback):
        """启动异步接收循环"""
        self.receive_callback = callback
        
        # 启动接收循环任务
        asyncio.create_task(self._receive_loop())
            
    async def _receive_loop(self):
        """异步接收循环"""
        logger.info("开始接收数据循环")
        
        while self.is_alive:
            try:
                data = await self.receive_data(timeout=1)
                if data:
                    if self.receive_callback:
                        await self.receive_callback(data)
                        
                # 短暂休眠，避免CPU占用过高        
                await asyncio.sleep(0.01)
                
            except Exception as e:
                logger.error(f"接收循环中出错: {str(e)}")
                
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