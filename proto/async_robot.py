import asyncio
import struct
import logging
from typing import Optional
from Xor import XORCipher
from protocol_map import protocol_map
from google.protobuf import message as pb_message

class AsyncRobot:
    """异步版机器人实现"""
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self.alive = False
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)  # 设置日志级别
        
        # 添加控制台处理器（如果尚未配置）
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)
        
        # 协议配置
        self.protocol_handlers = {
            1003: self._handle_login_result,
            # 3001: self._handle_heartbeat,
            # 2002: self._handle_enter_scene
        }
        self.cipher = XORCipher()

    async def connect(self) -> None:
        """建立异步TCP连接"""
        if self.is_connected:
            return
            
        try:
            self.reader, self.writer = await asyncio.open_connection(
                self.host, self.port
            )
            self.alive = True
            self.logger.info(f"Connected to {self.host}:{self.port}")
        except Exception as e:
            self.logger.error(f"连接失败: {str(e)}")
            await self.close()

    async def close(self) -> None:
        """关闭连接"""
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
            self.writer = None
            self.reader = None
            self.alive = False
            self.logger.info("Connection closed")

    async def send_protobuf(self, proto_id: int, data: bytes) -> None:
        """异步发送协议包"""
        if not self.writer:
            raise ConnectionError("未建立连接")
            
        try:
            encrypted = self.cipher.encode(
                proto_id.to_bytes(2, 'big') + data
            )
            header = len(encrypted).to_bytes(2, 'big')
            self.writer.write(header + encrypted)
            await self.writer.drain()
            self.logger.debug(f"已发送协议ID: {proto_id}")
        except Exception as e:
            self.logger.error(f"发送失败: {str(e)}")
            await self.close()

    async def message_loop(self) -> None:
        """异步消息处理主循环"""
        while self.alive:
            try:
                # 读取包头
                header = await self.reader.readexactly(2)
                if len(header) != 2:
                    break
                    
                packet_len = int.from_bytes(header, 'big')
                
                # 读取完整数据包
                encrypted = await self.reader.readexactly(packet_len)
                decrypted = self.cipher.encode(encrypted)
                
                # 解析协议
                proto_id = int.from_bytes(decrypted[:2], 'big')
                pb_data = decrypted[2:]
                print(pb_data)
                
                # 分发处理
                handler = self.protocol_handlers.get(proto_id)
                if handler:
                    await handler(pb_data)
                else:
                    self.logger.warning(f"未处理的协议ID: {proto_id}")
                    
            except (asyncio.IncompleteReadError, ConnectionResetError):
                break
            except Exception as e:
                self.logger.error(f"处理消息异常: {str(e)}")
                break

    async def start_heartbeat(self, interval: int = 10) -> None:
        """启动心跳定时任务"""
        while self.alive:
            try:
                await self.send_protobuf(3001, b'')  # 心跳协议
                await asyncio.sleep(interval)
            except Exception as e:
                self.logger.error(f"心跳异常: {str(e)}")
                await self.close()

    async def run(self) -> None:
        """主运行入口"""
        await self.connect()
        if not self.alive:
            return
            
        try:
            # 创建并行任务
            tasks = [
                self.message_loop(),
                self.start_heartbeat(),
                self._execute_login_sequence()
            ]
            await asyncio.gather(*tasks)
            
        except asyncio.CancelledError:
            self.logger.info("任务被取消")
        finally:
            await self.close()

    # 保留原有协议处理方法（需改为异步）
    async def _handle_login_result(self, data: bytes) -> None:
        """处理登录结果（示例）"""
        # 需要实现protobuf解析逻辑
        self.logger.info(f"收到登录结果: {data[:20]}...")

    async def _execute_login_sequence(self) -> None:
        """执行登录流程"""
        login_steps = [
            (1008, b''),  # QueryLogin
            (1001, b'account=123456789'), 
            (1002, b'pid=10506')
        ]
        
        for proto_id, data in login_steps:
            if not self.alive:
                break
            await self.send_protobuf(proto_id, data)
            await asyncio.sleep(1)

    @property
    def is_connected(self) -> bool:
        return self.writer is not None and not self.writer.is_closing()

async def main():
    robot = AsyncRobot("192.168.56.101", 7011)
    await robot.run()

if __name__ == "__main__":
    asyncio.run(main()) 