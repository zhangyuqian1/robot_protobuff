import random
import re
import time
import asyncio
import logging
from client import login_pb2, other_pb2, scene_pb2
from protocol_map_static import ProtocolMap

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncGameClient')

class AsyncGameClient:
    """异步游戏客户端，实现具体游戏功能"""
    
    def __init__(self, network_manager, protocol_handler):
        self.network = network_manager
        self.protocol = protocol_handler
        self.has_role_data = False
        self.current_scene = None
        self.player_id = None
        self.heartbeat_task = None
        self.robot_id = f"Robot_{int(time.time())}_{random.randint(1000, 9999)}"
        
        # 不能直接在构造函数中调用异步方法
        # 创建一个协程任务，但不等待它完成
        self._register_task = asyncio.create_task(self._register_handlers())
        
    async def _register_handlers(self):
        """注册所有协议处理器"""
        handlers = {
            1003: self._handle_login_result,
            1005: self._handle_create_result,
            3001: self._handle_heartbeat,
            # 2014: self._handle_sync_pos_queue,
        }
        
        for proto_id, handler in handlers.items():
            await self.protocol.register_handler(proto_id, handler)
            
    async def send_message(self, protocol_id, message_class, field_data=None):
        # logger.info(f"发送消息: {protocol_id}")
        """异步发送游戏消息"""
        try:
            # 获取协议名称
            protocol_name = ProtocolMap.get_name(protocol_id)
            
            if not protocol_name:
                raise ValueError(f"未知协议ID: {protocol_id}")

            # 创建protobuf对象
            protocol_data = message_class()
            
            # 动态设置字段
            if field_data:
                self._set_message_fields(protocol_data, field_data)
            
            # 序列化消息
            serialized =  await self.protocol.serialize_message(
                protocol_id=protocol_id,
                data=protocol_data
            )
            
            # 创建并发送数据包
            packet = await self.protocol.create_packet(protocol_id, serialized)
            success = await self.network.send_data(packet)
            if success:
                logger.info(f"成功发送协议ID: {protocol_id}")
            
            return success
                
        except Exception as e:
            logger.error(f"发送消息失败: {str(e)}")
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
                
    # 协议处理函数 - 现在是异步函数
    async def _handle_login_result(self, data):
        """登录结果处理"""
        logger.info(f"{self.robot_id} 登录结果: {data}")
        role_blocks = re.findall(r'role_list\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                self.has_role_data = True
                pid = int(pid_match.group(1))
                self.player_id = pid
                await self.login_role(pid)
                await asyncio.sleep(2)
    
    async def _handle_create_result(self, data):
        """创建角色结果处理"""
        logger.info(f"{self.robot_id} 创建角色结果: {data}")
        role_blocks = re.findall(r'role\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                self.has_role_data = True
                pid = int(pid_match.group(1))
                self.player_id = pid
                await self.login_role(pid)
                await asyncio.sleep(2)

    async def _handle_heartbeat(self, data):
        """心跳响应处理"""
        logger.debug(f"{self.robot_id} 心跳响应时间: {data.time}")

    async def _handle_sync_pos_queue(self, data):
        """进入场景处理"""
        logger.info(f"{self.robot_id} 进入场景: {data}")
        
    # 游戏功能实现 - 现在是异步函数
    async def query_login(self):
        logger.info(f"{self.robot_id} 查询登录")
        """查询登录"""
        return await self.send_message(
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
        
    async def login_account(self):
        logger.info(f"{self.robot_id} 登录账号")
        """登录账号"""
        account = time.strftime("%Y%m%d%H%M%S", time.localtime())+str(random.randint(1000, 9999))
        result = await self.send_message(
            protocol_id=1001,
            message_class=login_pb2.C2GSLoginAccount,
            field_data={'account': account}
        )
        
        logger.info(f"{self.robot_id} 当前角色数据状态: {self.has_role_data}")
        if not self.has_role_data:
            logger.info(f"{self.robot_id} 没有账号数据")
            name = time.strftime("%Y%m%d%H%M%S", time.localtime())
            logger.info(f"{self.robot_id} 创建角色: {name}")
            await self.create_role(name)
            await asyncio.sleep(2)
        else:
            logger.info(f"{self.robot_id} 有账号数据")
        
        return result
        
    async def create_role(self, name):
        logger.info(f"开始创建角色: {name}")
        """创建角色"""
        return await self.send_message(
            protocol_id=1003,
            message_class=login_pb2.C2GSCreateRole,
            field_data={
                'name': name,
                'role_type': 3,
                'school': 6
            }
        )
        
    async def login_role(self, pid):
        """登录角色"""
        return await self.send_message(
            protocol_id=1002,
            message_class=login_pb2.C2GSLoginRole,
            field_data={'pid': pid}
        )
        
    async def send_heartbeat(self):
        """发送心跳"""
        return await self.send_message(
            protocol_id=3001,
            message_class=other_pb2.C2GSHeartBeat
        )
        
    async def sync_position(self, scene_id, eid, positions):
        """同步位置"""
        return await self.send_message(
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
        
    async def start_heartbeat_task(self):
        """启动心跳任务"""
        # 取消之前的心跳任务（如果有）
        if self.heartbeat_task and not self.heartbeat_task.done():
            self.heartbeat_task.cancel()
            
        # 创建新的心跳任务
        self.heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        return self.heartbeat_task
        
    async def _heartbeat_loop(self):
        """心跳循环"""
        try:
            logger.info(f"{self.robot_id} 启动心跳任务")
            while self.network.is_alive:
                await self.send_heartbeat()
                await asyncio.sleep(10)
        except asyncio.CancelledError:
            logger.info(f"{self.robot_id} 心跳任务已取消")
        except Exception as e:
            logger.error(f"{self.robot_id} 心跳任务异常: {str(e)}")
        
    async def execute_login_sequence(self):
        """执行登录流程"""
        logger.info(f"{self.robot_id} 开始执行登录流程...")
        
        # 查询登录
        await self.query_login()
        
        # 登录账号
        await self.login_account()
        
        # 此时应该已经有角色并登录了
        await asyncio.sleep(3)
        
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
        await self.sync_position(9, 4, positions1)
        await asyncio.sleep(2)
        await self.sync_position(9, 4, positions2)
        await asyncio.sleep(2)
        await self.sync_position(9, 4, positions1)
        await asyncio.sleep(2)
        await self.sync_position(9, 4, positions2)
        
        # 启动心跳任务
        await self.start_heartbeat_task()
        
        logger.info(f"{self.robot_id} 登录流程执行完成")
        
    async def update(self):
        """更新游戏状态 - 可用于实现自动化操作"""
        # 这里可以添加定期执行的游戏逻辑
        pass 