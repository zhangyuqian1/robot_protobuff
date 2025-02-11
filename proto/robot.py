import re
import socket
import struct
import time
from google.protobuf import message as pb_message
from Agent import Agent
# 假设已生成proto文件
from client import login_pb2,other_pb2,scene_pb2
from proto_mapper import ProtobufMapper
from protocol_map import PROTOCOL_MAP_C2S, protocol_map  # 假设存在protocol_map.py
from threading import Timer
from Xor import XORCipher
import threading
import asyncio
import logging

class SimpleRobot:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.buffer = bytearray()
        self.sequence = 0
        self.proto_mapper = ProtobufMapper(cipher_cls=XORCipher)
        self._init_protobuf()
        self.has_role_data = False
        # 新增协议处理器字典
        self.protocol_handlers = {
            1003: self._handle_login_result,  # GS2CLoginResult
            1005: self._handle_create_result,# GS2CCreateRole
            3001: self._handle_heartbeat,    # GS2CHeartBeat
            2002: self._handle_enter_scene,  # GS2CEnterScene
        }
        
        # 协议配置
        self.header_fmt = ">HH"  # 包长(2字节) + 协议号(2字节)
        self.header_size = struct.calcsize(self.header_fmt)
        self.reader = None  # 删除未使用的异步属性
        self.writer = None
        
    def _init_protobuf(self):
        """初始化protobuf相关配置"""
        try:
            self.proto_mapper.load_proto_files()
        except Exception as e:
            print(f"加载proto文件失败: {str(e)}")
            raise

    def serialize_protobuf(self, protocol_id: int, data: dict, is_client_proto: bool = True) -> bytes:
        """
        自主协议序列化方法
        :param protocol_id: 协议ID
        :param data: 消息字典
        :param is_client_proto: 是否为客户端协议
        :return: 序列化后的字节流
        """
        try:
            # 获取协议名称
            message_name = PROTOCOL_MAP_C2S.get(protocol_id) if is_client_proto else protocol_map.get(protocol_id)
            if not message_name:
                raise ValueError(f"未知协议ID: {protocol_id}")

            # 序列化数据
            return self.proto_mapper.serialize_message(
                message_name=message_name,
                data=data,
                is_server=not is_client_proto
            )
        except Exception as e:
            print(f"协议序列化失败: {str(e)}")
            raise

    def send_protobuf_packet(self, protocol_id: int, data: dict, is_client_proto: bool = True):
        """
        完整协议发送流程
        :param protocol_id: 协议ID
        :param data: 消息字典
        :param is_client_proto: 是否为客户端协议
        """
        try:
            # 序列化数据
            serialized = self.serialize_protobuf(protocol_id, data, is_client_proto)
            
            # XOR加密处理
            cipher = XORCipher()
            encrypted = cipher.encode(
                protocol_id.to_bytes(2, 'big') + serialized
            )
            
            # 构造完整数据包
            full_packet = len(encrypted).to_bytes(2, 'big') + encrypted
            
            # 发送数据
            self.sock.sendall(full_packet)
            print(f"成功发送协议ID: {protocol_id}")
            
        except Exception as e:
            print(f"发送协议包失败: {str(e)}")
            self.close()

    def connect(self):
        """建立TCP连接"""
        if self.is_connected():
            return
            
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.settimeout(5)  # 添加超时设置
            self.sock.connect((self.host, self.port))
            self.sock.settimeout(None)  # 重置超时
            print(f"Connected to {self.host}:{self.port}")
        except socket.error as e:
            print(f"连接失败: {str(e)}")
            self.close()
            raise

    def close(self):
        """关闭连接"""
        if self.sock:
            self.sock.close()
            self.sock = None  # 重要！重置socket为None
            print("Connection closed")
    
    def register_handler(self, proto_id, handler):
        """注册协议处理函数（新增方法）"""
        self.protocol_handlers[proto_id] = handler

    def server_to_client(self):
        """仿照Agent的server_to_client实现"""
        while getattr(self, 'alive', True):
            try:
                # 确保socket已连接
                if self.sock is None:
                    time.sleep(0.1)
                    continue
                    
                data = self.sock.recv(8192)
                if not data:
                    print("连接已关闭")
                    self.alive = False
                    break
                
                self.buffer += data
                
                # 处理完整消息包
                while len(self.buffer) >= 2:
                    msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                    if len(self.buffer) < msg_len + 2:
                        break
                    
                    packet = self.buffer[:msg_len+2]
                    self.buffer = self.buffer[msg_len+2:]
                    
                    # 修改后的协议处理部分
                    parsed, name, pid = self.proto_mapper.parse_packet_server(
                        packet, 
                        is_server=True
                    )
                    # print(type(parsed))
                    self._dispatch_protocol(pid, parsed, name)  # 调用分发方法
            except Exception as e:
                print(f"server_to_client error: {str(e)}")
                # self.alive = False
                # break
            time.sleep(0.01)
    
    def _dispatch_protocol(self, proto_id, data, proto_name):
        """协议分发核心方法（新增）"""
        handler = self.protocol_handlers.get(proto_id)
        if handler:
            try:
                print(f"处理协议[{proto_id}]{proto_name}")
                handler(data)
            except Exception as e:
                print(f"处理协议{proto_id}异常: {str(e)}")
        else:
            print(f"未注册的协议处理: [{proto_id}]{proto_name}")

    def _handle_login_result(self, data):
        """登录结果处理（示例）"""
        print(data)
        # 提取角色信息（同样处理带空格的情况）
        role_blocks = re.findall(r'role_list\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            # 处理带空格的pid字段
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                self.has_role_data = True
                pid = int(pid_match.group(1)) 
                self.C2GSLoginRole(pid)        
                time.sleep(2)                   
    
    def _handle_create_result(self,data):
        print(data)
        role_blocks = re.findall(r'role\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            # 处理带空格的pid字段
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                self.has_role_data = True
                pid = int(pid_match.group(1)) 
                self.C2GSLoginRole(pid)        
                time.sleep(2)

    def _handle_heartbeat(self, data):
        """心跳响应处理（示例）"""
        # self.last_heartbeat = time.time()
        # print(data)
        # print(type(data))
        print(f"心跳响应时间: {data.time}")

    def _handle_enter_scene(self, data):
        """进入场景处理（示例）"""
        print(f"进入场景: {data.scene_id}")
        self.current_scene = data.scene_id

    def start_heartbeat(self):
        """启动心跳定时任务"""
        while True:
            time.sleep(10)
            self.send_packet("C2GSHeartBeat", timestamp=int(time.time()))
    
    def run(self):
        """运行机器人"""
        try:
            self.connect()
            self.alive = True
            
            # 使用daemon线程自动管理生命周期
            threading.Thread(target=self.server_to_client, daemon=True).start()
            
            # 登录流程封装
            self._execute_login_sequence()
            
            # 主循环简化
            while self.alive:
                time.sleep(1)

        except KeyboardInterrupt:
            print("用户中断")
        finally:
            self.close()

    def _execute_login_sequence(self):
        """执行登录流程"""
        sequence = [
            self.C2GSQueryLogin,
            self.login_account,
            # self.C2GSCreateRole,
            lambda: time.sleep(3),
            self.C2GSSyncPosQueue2,
            lambda: time.sleep(1),
            self.C2GSSyncPosQueue,
            lambda: time.sleep(1),
            self.C2GSSyncPosQueue2,
            lambda: time.sleep(1),
            self.C2GSSyncPosQueue,
            self.C2GSHeartBeat,



        ]
        
        for step in sequence:
            if callable(step):
                step()
            else:
                time.sleep(step)

    def _send_protocol(self, protocol_id: int, proto_class, field_data: dict = None, is_client_proto: bool = True):
        """通用协议发送方法"""
        print(f"开始执行{proto_class.DESCRIPTOR.name}协议发送")
        try:
            # 创建protobuf对象
            protocol_data = proto_class()
            
            # 动态设置字段
            if field_data:
                for field, value in field_data.items():
                    if isinstance(value, dict) and 'nested' in value:
                        # 处理repeated字段
                        nested_field = getattr(protocol_data, field)
                        for item in value['nested']:
                            nested_obj = nested_field.add()
                            for k, v in item.items():
                                if isinstance(v, dict):
                                    # 处理嵌套消息字段（如pos）
                                    sub_msg = nested_obj.DESCRIPTOR.fields_by_name[k].message_type._concrete_class()
                                    for sub_k, sub_v in v.items():
                                        setattr(sub_msg, sub_k, sub_v)
                                    getattr(nested_obj, k).CopyFrom(sub_msg)
                                else:
                                    setattr(nested_obj, k, v)
                    elif isinstance(value, dict):
                        # 处理单个嵌套消息字段
                        sub_msg = protocol_data.DESCRIPTOR.fields_by_name[field].message_type._concrete_class()
                        for k, v in value.items():
                            setattr(sub_msg, k, v)
                        getattr(protocol_data, field).CopyFrom(sub_msg)
                    else:
                        setattr(protocol_data, field, value)
            
            self.send_protobuf_packet(
                protocol_id=protocol_id,
                data=protocol_data,
                is_client_proto=is_client_proto
            )
        except AttributeError as e:
            print(f"字段设置错误: {str(e)}")
            raise

    def C2GSQueryLogin(self):
        """查询登录"""
        self._send_protocol(
            protocol_id=1008,
            proto_class=login_pb2.C2GSQueryLogin,
            field_data={
                'res_file_version': {
                    'nested': [
                        {'file_name': 'achievedata', 'version': 1508158680},
                        {'file_name': 'arenadata', 'version': 1508158680},
                        {'file_name': 'itemdata', 'version': 1508158680}
                    ]
                }
            }
        )

    def login_account(self):
        """登录账号"""
        account=time.strftime("%Y%m%d%H%M%S", time.localtime())
        self._send_protocol(
            protocol_id=1001,
            proto_class=login_pb2.C2GSLoginAccount,
            field_data={'account': account}
        )
        time.sleep(2)
        print(f"[DEBUG] 当前角色数据状态: {self.has_role_data}")
        if not self.has_role_data:
            print("没有账号数据")
            name=time.strftime("%Y%m%d%H%M%S", time.localtime())
            print(f"[DEBUG] 创建角色: {name}")
            self.C2GSCreateRole(name)
            time.sleep(2)
            
        else:
            print("有账号数据")

    def C2GSCreateRole(self,name):
        """创建角色"""
        self._send_protocol(
            protocol_id=1003,
            proto_class=login_pb2.C2GSCreateRole,
            field_data={
                'name': name,
                'role_type': 3,
                'school': 6
            }

        )

    def C2GSLoginRole(self,pid):
        """登录角色"""
        self._send_protocol(
            protocol_id=1002,
            proto_class=login_pb2.C2GSLoginRole,
            field_data={'pid': pid}
        )

    def C2GSHeartBeat(self):
        """心跳协议"""
        print("10秒发送1次心跳")
        while True:
            self._send_protocol(
                protocol_id=3001,
                proto_class=other_pb2.C2GSHeartBeat
            )
            time.sleep(10)
    def C2GSSyncPosQueue(self):
        """同步位置队列"""
        print("同步位置队列")
        self._send_protocol(
            protocol_id=2005,
            proto_class=scene_pb2.C2GSSyncPosQueue,
            field_data={
                'scene_id': 9,
                'eid': 4,
                'poslist': {
                    'nested': [  # 对应repeated字段
                        {
                            'pos': {  # 嵌套消息使用字典
                                'x': 5743,
                                'y': 5561,
                                'face_y': 1100178
                            },
                            'time': 100  # 修正时间值
                        },
                        {
                            'pos': {
                                'x': 5464,
                                'y': 2964,
                                'face_y': 1100178
                            }
                        }
                    ]

                }
            }
        )
    def C2GSSyncPosQueue2(self):
        """同步位置队列"""
        print("同步位置队列11111111111111111111111111111111111111111")

        self._send_protocol(
            protocol_id=2005,
            proto_class=scene_pb2.C2GSSyncPosQueue,
            field_data={
                'scene_id': 9,
                'eid': 4,
                'poslist': {
                    'nested': [  # 对应repeated字段
                        {
                            'pos': {  # 嵌套消息使用字典
                                'x': 5464,
                                'y': 2964,
                                'face_y': 1100178
                            },


                            'time': 100  # 修正时间值
                        },
                        {
                            'pos': {
                                'x': 5743,
                                'y': 5561,
                                'face_y': 1100178

                            }
                        }
                    ]

                }
            }
        )    
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
            cipher = XORCipher()
            
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
            # display_text = f'Custom message sent: {final_message}\n'
            # display_text += f'Message ID: {message_id}\n'
            # self.ui_thread.send_signal.emit(display_text)
            
        except Exception as e:
            print(f"send_custom_message error: {e}")

    def is_connected(self):
        """检查连接状态"""
        return self.sock is not None and self.alive

# 使用示例
if __name__ == "__main__":
    robot = SimpleRobot("192.168.56.101", 7011)
    robot.run()
   