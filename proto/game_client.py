import random
import re
import time
import threading
from client import login_pb2, other_pb2, scene_pb2
from protocol_map_static import ProtocolMap

class GameClient:
    """游戏客户端，实现具体游戏功能"""
    
    def __init__(self, network_manager, protocol_handler):
        self.network = network_manager
        self.protocol = protocol_handler
        self.has_role_data = False
        self.current_scene = None
        self.player_id = None
        
        # 注册协议处理器
        self._register_handlers()
        
    def _register_handlers(self):
        """注册所有协议处理器"""
        handlers = {
            1003: self._handle_login_result,
            1005: self._handle_create_result,
            3001: self._handle_heartbeat,
            # 2014: self._handle_sync_pos_queue,
        }
        
        for proto_id, handler in handlers.items():
            self.protocol.register_handler(proto_id, handler)
            
    def send_message(self, protocol_id, message_class, field_data=None):
        """发送游戏消息"""
        try:
            # 获取协议名称（无需创建实例，直接调用静态方法）
            protocol_name = ProtocolMap.get_name(protocol_id)
            
            if not protocol_name:
                raise ValueError(f"未知协议ID: {protocol_id}")

            # 创建protobuf对象
            protocol_data = message_class()
            
            # 动态设置字段
            if field_data:
                self._set_message_fields(protocol_data, field_data)
            
            # 序列化消息
            serialized = self.protocol.serialize_message(
                protocol_id=protocol_id,
                data=protocol_data
            )
            
            # 创建并发送数据包
            packet = self.protocol.create_packet(protocol_id, serialized)
            if self.network.send_data(packet):
                print(f"成功发送协议ID: {protocol_id}")
                return True
            return False
                
        except Exception as e:
            print(f"发送消息失败: {str(e)}")
            return False
            
    def _set_message_fields(self, message, field_data):
        """递归设置消息字段"""
        for field, value in field_data.items():
            if isinstance(value, dict) and 'nested' in value:
                # 处理repeated字段
                nested_field = getattr(message, field)
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
                sub_msg = message.DESCRIPTOR.fields_by_name[field].message_type._concrete_class()
                for k, v in value.items():
                    setattr(sub_msg, k, v)
                getattr(message, field).CopyFrom(sub_msg)
            else:
                setattr(message, field, value)
                
    # 协议处理函数
    def _handle_login_result(self, data):
        """登录结果处理"""
        print(data)
        # role_blocks = re.findall(r'role_list\s*{([^}]+)}', str(data), re.DOTALL)
        # for block in role_blocks:
        #     pid_match = re.search(r'pid\s*:\s*(\d+)', block)
        #     if pid_match:
        #         self.has_role_data = True
        #         pid = int(pid_match.group(1))
        #         self.player_id = pid
        #         self.login_role(pid)
        #         time.sleep(2)
    
    def _handle_create_result(self, data):
        """创建角色结果处理"""
        print(data)
        role_blocks = re.findall(r'role\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                self.has_role_data = True
                pid = int(pid_match.group(1))
                self.player_id = pid
                self.login_role(pid)
                time.sleep(2)

    def _handle_heartbeat(self, data):
        """心跳响应处理"""
        print(f"心跳响应时间: {data.time}")

    def _handle_sync_pos_queue(self, data):
        """进入场景处理"""
        print(f"进入场景: {data}")
        
    # 游戏功能实现
    def query_login(self):
        """查询登录"""
        return self.send_message(
            protocol_id=1008,
            message_class=login_pb2.C2GSQueryLogin,
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
        account = time.strftime("%Y%m%d%H%M%S", time.localtime())+str(random.randint(1000, 9999))
        result = self.send_message(
            protocol_id=1001,
            message_class=login_pb2.C2GSLoginAccount,
            field_data={'account': account}
        )
        
        
        print(f"[DEBUG] 当前角色数据状态: {self.has_role_data}")
        if not self.has_role_data:
            print("没有账号数据")
            name = time.strftime("%Y%m%d%H%M%S", time.localtime())
            print(f"[DEBUG] 创建角色: {name}")
            self.create_role(name)
            time.sleep(2)
        else:
            print("有账号数据")
        
        return result
        
    def create_role(self, name):
        """创建角色"""
        return self.send_message(
            protocol_id=1003,
            message_class=login_pb2.C2GSCreateRole,
            field_data={
                'name': name,
                'role_type': 3,
                'school': 6
            }
        )
        
    def login_role(self, pid):
        """登录角色"""
        return self.send_message(
            protocol_id=1002,
            message_class=login_pb2.C2GSLoginRole,
            field_data={'pid': pid}
        )
        
    def send_heartbeat(self):
        """发送心跳"""
        return self.send_message(
            protocol_id=3001,
            message_class=other_pb2.C2GSHeartBeat
        )
        
    def sync_position(self, scene_id, eid, positions):
        """同步位置"""
        return self.send_message(
            protocol_id=2005,
            message_class=scene_pb2.C2GSSyncPosQueue,
            field_data={
                'scene_id': scene_id,
                'eid': eid,
                'poslist': {
                    'nested': positions
                }
            }
        )
        
    def start_heartbeat_task(self):
        """启动心跳任务"""
        def heartbeat_task():
            while self.network.is_alive:
                self.send_heartbeat()
                time.sleep(10)
                
        thread = threading.Thread(target=heartbeat_task, daemon=True)
        thread.start()
        return thread
        
    def execute_login_sequence(self):
        """执行登录流程"""
        print("开始执行登录流程...")
        
        # 查询登录
        self.query_login()
        
        # 登录账号
        self.login_account()
        
        # 此时应该已经有角色并登录了
        time.sleep(3)
        
        # 同步位置
        positions1 = [
            {
                'pos': {'x': 5743, 'y': 5561, 'face_y': 1100188},
                'time': 100
            },
            {
                'pos': {'x': 5464, 'y': 2964, 'face_y': 1100188}
            }
        ]
        
        positions2 = [
            {
                'pos': {'x': 5464, 'y': 2964, 'face_y': 1100188},
                'time': 100
            },
            {
                'pos': {'x': 5743, 'y': 5561, 'face_y': 1100188}
            }
        ]
        
        # 发送位置同步请求
        self.sync_position(9, 4, positions1)
        time.sleep(2)
        self.sync_position(9, 4, positions2)
        time.sleep(2)
        self.sync_position(9, 4, positions1)
        time.sleep(2)
        self.sync_position(9, 4, positions2)
        
        # 启动心跳任务
        self.start_heartbeat_task()
        
        print("登录流程执行完成") 