import socket
import struct
import time
import threading

class NetworkManager:
    """网络连接管理器，处理底层网络通信"""
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.buffer = bytearray()
        self.is_alive = False
        self.header_fmt = ">HH"  # 包长(2字节) + 协议号(2字节)
        self.header_size = struct.calcsize(self.header_fmt)
        
    def connect(self):
        """建立TCP连接"""
        if self.is_connected():
            return True
            
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.settimeout(5)
            self.sock.connect((self.host, self.port))
            self.sock.settimeout(None)
            self.is_alive = True
            print(f"已连接到 {self.host}:{self.port}")
            return True
        except socket.error as e:
            print(f"连接失败: {str(e)}")
            self.close()
            return False

    def close(self):
        """关闭连接"""
        if self.sock:
            self.sock.close()
            self.sock = None
            self.is_alive = False
            print("连接已关闭")
    
    def is_connected(self):
        """检查连接状态"""
        return self.sock is not None and self.is_alive
        
    def send_data(self, data):
        """发送原始数据"""
        if not self.is_connected():
            print("未连接到服务器")
            return False
            
        try:
            self.sock.sendall(data)
            return True
        except socket.error as e:
            print(f"发送数据失败: {str(e)}")
            self.close()
            return False
            
    def start_receive_loop(self, packet_callback):
        """启动数据接收循环"""
        def receive_loop():
            while self.is_alive:
                try:
                    if not self.is_connected():
                        time.sleep(0.1)
                        continue
                        
                    data = self.sock.recv(8192)
                    if not data:
                        print("服务器关闭了连接")
                        self.is_alive = False
                        break
                    
                    self.buffer += data
                    
                    # 处理完整消息包
                    while len(self.buffer) >= 2:
                        msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                        if len(self.buffer) < msg_len + 2:
                            break
                        print(f"处理完整消息包: {msg_len}")
                        packet = self.buffer[:msg_len+2]
                        self.buffer = self.buffer[msg_len+2:]
                        
                        # 回调函数处理数据包
                        packet_callback(packet)
                        
                except Exception as e:
                    print(f"接收数据错误: {str(e)}")
                    # 不立即中断，允许重试
                time.sleep(0.01)
                
        # 使用daemon线程自动管理生命周期
        thread = threading.Thread(target=receive_loop, daemon=True)
        thread.start()
        return thread 