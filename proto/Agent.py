import Xor
import socket
import time
from threading import Timer
from proto_mapper import ProtobufMapper

class Agent(object):
    def __init__(self, agent_host, agent_port, server_host, server_port,ui_thread):
        #传入uithread
        self.ui_thread = ui_thread
        # 设置一个socket server，以便后续监听客户端请求
        self.socket_service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 将socket server绑定指定的ip和端口号
        self.socket_service.bind((agent_host, int(agent_port)))
        self.socket_service.listen(5)
        # 设置客户端socket属性，先把它设置成一个空对象，后续有客户端请求过来之后再更新
        self.client_socket = None
        # 设置服务器socket属性，生成一个socket对象
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 将server_socket连接到游戏服务器
        self.server_socket.connect((server_host, server_port))
        # 给代理设置一个是否存活的状态，用于在遇到某些异常的时候终止转发线程
        self.alive = True
        self.client_buffer = b''  # 客户端数据缓冲区
        self.server_buffer = b''  # 服务器数据缓冲区
        self.BUFFER_SIZE = 8192   # 接收缓冲区大小
        # 添加ProtobufMapper实例作为类成员
        self.proto_mapper = ProtobufMapper()
        # 预先加载所有协议文件
        self.proto_mapper.load_proto_files()

    def client_to_server(self):
        """
        转发客户端发送给服务器的包
        """
        while self.alive:
            try:
                # 从客户端接收数据
                data = self.client_socket.recv(self.BUFFER_SIZE)
                if not data:
                    print('收到了空字节流，socket连接可能断开')
                    self.alive = False
                    break

                # 将新数据添加到缓冲区
                self.client_buffer += data
                
                # 处理缓冲区中的数据
                while len(self.client_buffer) >= 2:  # 至少需要2字节来读取长度
                    # 获取消息长度
                    msg_len = int.from_bytes(self.client_buffer[:2], byteorder='big')
                    
                    # 检查是否有完整的消息
                    if len(self.client_buffer) < msg_len + 2:
                        break  # 消息不完整，等待更多数据
                        
                    # 提取完整消息
                    msg_data = self.client_buffer[:msg_len + 2]
                    self.client_buffer = self.client_buffer[msg_len + 2:]
                    
                    # 解析消息
                    parsed_msg, message_name ,message_id= self.pbcheck(msg_data, protocol_type='client')
                    display_text = f'send_bytes: {msg_data}\n'
                    if parsed_msg:
                        display_text += f'Parsed message: {parsed_msg}\n'
                        display_text += f'message_name: {message_name}\n'
                        display_text += f'message_id: {message_id}\n'

                    self.ui_thread.send_signal.emit(display_text)
                    self.server_socket.send(msg_data)
                    
            except Exception as e:
                print(f"client_to_server error: {e}")
                self.alive = False
                break
                
            time.sleep(0.01)

    def server_to_client(self):
        """
        转发服务器返回给客户端的包
        """
        while self.alive:
            try:
                # 从服务器接收数据
                data = self.server_socket.recv(self.BUFFER_SIZE)
                if not data:
                    print('收到了空字节流，socket连接已经断开')
                    self.alive = False
                    break

                # 将新数据添加到缓冲区
                self.server_buffer += data
                
                # 处理缓冲区中的数据
                while len(self.server_buffer) >= 2:  # 至少需要2字节来读取长度
                    # 获取消息长度
                    msg_len = int.from_bytes(self.server_buffer[:2], byteorder='big')
                    
                    # 检查是否有完整的消息
                    if len(self.server_buffer) < msg_len + 2:
                        break  # 消息不完整，等待更多数据
                        
                    # 提取完整消息
                    msg_data = self.server_buffer[:msg_len + 2]
                    self.server_buffer = self.server_buffer[msg_len + 2:]
                    
                    # 解析消息
                    parsed_msg, message_name ,message_id= self.pbcheck(msg_data, protocol_type='server')

                    # display_text = f'recv_bytes: {msg_data}\n'
                    display_text = ''
                    if parsed_msg:
                        display_text += f'Parsed message: {parsed_msg}\n'
                        display_text += f'message_name: {message_name}\n'
                        display_text += f'message_id: {message_id}\n'

                    self.ui_thread.recv_signal.emit(display_text)
                    self.client_socket.send(msg_data)
                    
            except Exception as e:
                print(f"server_to_client error: {e}")
                self.alive = False
                break
                
            time.sleep(0.01)
    
    def start(self):
        """
        代理启动方法
        :return:
        """
        # 等待客户端连接
        self.client_socket, addr = self.socket_service.accept()
        # 启动转发线程，这里用的是Timer定时器，它也是继承自thread线程类，所以会单独起两个线程
        Timer(0, self.client_to_server).start()
        Timer(0, self.server_to_client).start()

    def stop(self):
        """
        代理结束方法
        :return:
        """
        # 在代理停止运行时，关闭客户端、服务器与代理之间的socket连接
        self.server_socket.shutdown(2)
        self.server_socket.close()
        self.socket_service.shutdown(2)
        self.socket_service.close()

    def pbcheck(self, data, protocol_type='client'):
        """
        解析protobuf数据
        :param data: 原始字节流
        :param protocol_type: 协议类型，可以是 'client' 或 'server'
        :return: 解析后的消息或None
        """
        try:
            # 检查数据长度是否足够
            if len(data) < 2:
                return None, None, None
                
            # 检查实际数据长度是否符合
            msg_len = int.from_bytes(data[:2], byteorder='big')
            if len(data) < msg_len + 2:
                return None, None, None
                
            # 提取实际消息内容
            msg_data = data
            # XOR解密
            cipher = Xor.XORCipher()
            # 解析消息长度和内容
            message_length = int.from_bytes(msg_data[:2], byteorder='big')
            message_content = msg_data[2:]

            # 解密并解析消息
            decrypted_data = cipher.encode(message_content)
            message_id = int.from_bytes(decrypted_data[:2], byteorder='big')
            actual_content = decrypted_data[2:]
            
            # 特殊处理固定长度的消息
            if len(msg_data) == 4:  # 移除 protocol_type 判断
                message_code = int.from_bytes(msg_data[2:], byteorder='big')
                
                # 根据不同的消息码返回对应的消息结构
                if protocol_type == 'server':
                    if message_code == 0x03c8:  # GS2CSetInviteCodeResult
                        parsed_msg = {
                            'errcode': message_code,
                            'msg': f'错误码: {message_code}'
                        }
                        return parsed_msg, 'GS2CSetInviteCodeResult', 1010
                    elif message_code == 0x03cb:  # GS2CQueryLogin
                        parsed_msg = {
                            'delete_file': [],
                            'res_file': [],
                            'code': f'消息码: {message_code}'
                        }
                        return parsed_msg, 'GS2CQueryLogin', 1009
                    elif message_code == 0x3a99:  # GS2CMarrySkill
                        parsed_msg = {
                            'skill_list': []
                        }
                        return parsed_msg, 'GS2CMarrySkill', 15011
                else:  # client messages
                    if message_code == 0x03ca:  # C2GSQueryLogin
                        parsed_msg = {
                            'res_file_version': []  # 空的版本列表
                        }
                        return parsed_msg, 'C2GSQueryLogin', 1008
            
            # 使用类成员的proto_mapper而不是创建新实例
            if protocol_type == 'client':
                parsed_msg, message_name = self.proto_mapper.parse_message(message_id, actual_content,is_server=False)
                if message_name and 'HeartBeat' in message_name:
                    return '这是心跳包', message_name, 3001
            else:
                parsed_msg, message_name = self.proto_mapper.parse_message(message_id, actual_content,is_server=True)
            
            # 添加心跳包判断，保持返回值格式一致
            
           
            return parsed_msg, message_name,message_id
        except Exception as e:
            # 通过检查当前线程的调用栈来确定数据来源
            import inspect
            caller_frame = inspect.currentframe().f_back
            source = "client" if caller_frame.f_code.co_name == "client_to_server" else "server"
            print(f"数据来源: {source}")
            print(f"解析protobuf数据失败: {str(e)}")
            return None, None, None  # 确保异常情况下也返回三个值

    

    def send_custom_protobuf(self, message_id, message_content):
        """完整的消息发送方法"""
        """
        发送自定义消息到服务器
        :param message_id: 协议ID (int)
        :param message_content: 消息内容 (bytes)
        :return: None
        """
        try:
            # 使用XOR加密消息内容
            cipher = Xor.XORCipher()
            
            # 构造消息格式：message_id (2 bytes) + content
            message_to_encrypt = message_id.to_bytes(2, byteorder='big') + message_content
            
            # 加密消息
            encrypted_data = cipher.encode(message_to_encrypt)
            
            # 计算消息总长度并添加长度头
            total_length = len(encrypted_data)
            final_message = total_length.to_bytes(2, byteorder='big') + encrypted_data
            
            # 发送消息到服务器
            self.server_socket.send(final_message)
            
            # 显示发送的消息信息
            display_text = f'Custom message sent: {final_message}\n'
            display_text += f'Message ID: {message_id}\n'
            self.ui_thread.send_signal.emit(display_text)
            
        except Exception as e:
            print(f"send_custom_message error: {e}")
if __name__ == '__main__':
    agent = Agent("127.0.0.1", 10086, "192.168.9.57", 7011,)
    agent.start()
