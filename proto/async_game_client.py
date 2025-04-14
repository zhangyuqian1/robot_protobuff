import random
import re
import time
import asyncio
import logging
from client import login_pb2, other_pb2, scene_pb2,chat_pb2
from protocol_map_static import ProtocolMap
from datetime import datetime
import configparser
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncGameClient')
logger.setLevel(logging.WARNING)
class AsyncGameClient:
    """异步游戏客户端，实现具体游戏功能"""
    
    def __init__(self, network_manager, protocol_handler, robot_id):
        self.network = network_manager
        self.protocol = protocol_handler 
        self.has_role_data = False
        self.current_scene = None
        self.player_id = None
        self.heartbeat_task = None
        self.chat_task = None
        self.robot_id = robot_id
        
        # 不能直接在构造函数中调用异步方法
        # 创建一个协程任务，但不等待它完成
        self._register_task = asyncio.create_task(self._register_handlers())
        
        # 预创建心跳包对象
        self.heartbeat_msg = other_pb2.C2GSHeartBeat()
        self.chat_msg = chat_pb2.C2GSChat()
        
    async def _register_handlers(self):
        """注册所有协议处理器"""
        handlers = {
            1003: self._handle_login_result,
            1005: self._handle_create_result,
            3001: self._handle_heartbeat,
            # 13001: self._handle_chat,
            # 2014: self._handle_sync_pos_queue,
        }
        
        for proto_id, handler in handlers.items():
            await self.protocol.register_handler(proto_id, handler)
            
    async def send_message(self, protocol_id, message_class, field_data=None):
        # logger.info(f"发送消息: {protocol_id} {message_class} {field_data}")
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
                # logger.info(f"成功发送协议ID: {protocol_id}")
                pass
            
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
        logger.warning(f"Robot_{self.robot_id} 登录结果: {data}")
        role_blocks = re.findall(r'role_list\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                logger.warning(f"{pid_match} 有匹配到")
                self.has_role_data = True
                pid = int(pid_match.group(1))
                self.player_id = pid
                await self.login_role(pid)
                await asyncio.sleep(1)
            else:
                logger.warning(f"{self.robot_id} 没有角色数据")

    async def _handle_create_result(self, data):
        """创建角色结果处理"""
        logger.warning(f"{self.robot_id} 创建角色结果: {data}")
        role_blocks = re.findall(r'role\s*{([^}]+)}', str(data), re.DOTALL)
        for block in role_blocks:
            pid_match = re.search(r'pid\s*:\s*(\d+)', block)
            if pid_match:
                # self.has_role_data = True
                pid = int(pid_match.group(1))
                self.player_id = pid
                await self.login_role(pid)
                await asyncio.sleep(2)
        
    async def _handle_heartbeat(self, data):
      """心跳响应处理"""
      logger.warning(f"Robot_{self.robot_id} 心跳响应: {data}")
    
    async def _handle_chat(self, data):
        """聊天响应处理"""
        # logger.info(f"Robot_{self.robot_id} 聊天响应: {data}")
        return None

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
        
    async def login_account(self,account):
        logger.warning(f"{self.robot_id} 开始登录账号{account}")
        """登录账号"""
        if not account:
            account = time.strftime("%Y%m%d%H%M%S", time.localtime())+str(random.randint(1000, 9999))

        result = await self.send_message(
            protocol_id=1001,
            message_class=login_pb2.C2GSLoginAccount,
            field_data={'account': account}
        )
        
        
        logger.warning(f"{self.robot_id} 当前角色数据状态: {self.has_role_data}")
        if not self.has_role_data:
            logger.warning(f"{self.robot_id} 没有账号数据")
            name = time.strftime("%Y%m%d%H%M%S", time.localtime())
            logger.warning(f"{self.robot_id} 创建角色: {name}")
            await self.create_role(name)
            await asyncio.sleep(0.5)
        else:
            logger.info(f"{self.robot_id} 有账号数据")
        
        return account
        
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
        logger.warning(f"{self.robot_id} 登录角色: {pid}")
        """登录角色"""
        return await self.send_message(
            protocol_id=1002,
            message_class=login_pb2.C2GSLoginRole,
            field_data={'pid': pid}
        ),pid
        
    async def send_heartbeat(self):
        """复用心跳包对象"""
        return await self.send_message(
            protocol_id=3001,
            message_class=lambda: self.heartbeat_msg  # 使用lambda避免新建
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
    
    async def start_chat_task(self,account):
        """启动聊天任务"""              
        # 取消之前的聊天任务（如果有）
        if self.chat_task and not self.chat_task.done():
            self.chat_task.cancel()
            
        # 创建新的聊天任务
        self.chat_task = asyncio.create_task(self._chat_loop(account))
        return self.chat_task
    
    async def gm_command(self,command):
        """gm命令"""
        return await self.send_message(
            protocol_id=3002,
            message_class=other_pb2.C2GSGMCmd,
            field_data={'cmd': command}
        )
    
    async def chat(self,message):   
        """聊天"""
        # logger.warning(f"发送聊天消息: {message}")
        return await self.send_message(
            protocol_id=12001,
            message_class=lambda: self.chat_msg,
            field_data={'cmd': message,
                        'type': 1,
                        }
        )
    

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

    async def _chat_loop(self,account):
        """聊天循环"""
        try:
            logger.info(f"{self.robot_id} 启动聊天任务")
            while self.network.is_alive:
                await self.chat(f'我是机器人{account}')
                await asyncio.sleep(40)
        except asyncio.CancelledError:
            logger.info(f"{self.robot_id} 聊天任务已取消")
        except Exception as e:
            logger.error(f"{self.robot_id} 聊天任务异常: {str(e)}")
        
    async def execute_login_sequence(self,account):
        """执行登录流程"""
        logger.warning(f"{self.robot_id} 开始执行登录流程...{account}")
        
        # 查询登录
        await self.query_login()
        
        # 登录账号
        account= await self.login_account(account)
        logger.warning(f"登录账号{account}")
        # 此时应该已经有角色并登录了
        await asyncio.sleep(3) 
        


        await self.gm_command('toprole')
        # await asyncio.sleep(1)

        # 同步位置
        # positions1 = [
        #     {
        #         'pos': {'x': 5743, 'y': 5561, 'face_y': 1100188},
        #         'time': 100
        #     },
        #     {
        #         'pos': {'x': 5464, 'y': 2964, 'face_y': 1100188}
        #     }
        # ]
        
        # positions2 = [
        #     {
        #         'pos': {'x': 5464, 'y': 2964, 'face_y': 1100188},
        #         'time': 100
        #     },
        #     {
        #         'pos': {'x': 5743, 'y': 5561, 'face_y': 1100188}
        #     }
        # ]
        
        # #发送位置同步请求
        # await self.sync_position(9, 4, positions1)
        # await asyncio.sleep(2)
        # await self.sync_position(9, 4, positions2)
        # await asyncio.sleep(2)
        # await self.sync_position(9, 4, positions1)
        # await asyncio.sleep(2)
        # await self.sync_position(9, 4, positions2)
        
        # 启动心跳任务
        await self.start_heartbeat_task()
        await self.start_chat_task(account)
        logger.info(f"{self.robot_id} 登录流程执行完成")
        
    async def update(self):
        """更新游戏状态 - 可用于实现自动化操作"""
        # 这里可以添加定期执行的游戏逻辑
        pass 

    @classmethod
    def generate_batch_accounts(cls):
        """生成基于当前时间的批量账号并写入配置文件"""
        try:
            # 生成基础时间字符串（精确到小时）
            time_str = datetime.now().strftime("%Y%m%d%H")
            
            # 生成1000个账号（格式: 时间基础 + 4位序号）
            accounts = [f"{time_str}{i:04d}" for i in range(1, 1001)]
            
            # 创建配置解析器
            config = configparser.ConfigParser()
            config['Accounts'] = {}
            
            # 填充账号数据
            for idx, account in enumerate(accounts, 1):
                config['Accounts'][f'account{idx}'] = account
                
            # 写入配置文件（覆盖模式）
            with open(cls._accounts_file, 'w', encoding='utf-8') as f:
                config.write(f)
                
            logger.warning(f"已生成 {len(accounts)} 个账号到 {cls._accounts_file}")
            return True
            
        except Exception as e:
            logger.error(f"生成批量账号失败: {str(e)}")
            return False

    # 在 load_accounts 方法中添加自动生成逻辑
    @classmethod
    def load_accounts(cls):
        """加载账号列表配置文件"""
        if cls._accounts_loaded:
            return
            
        config = configparser.ConfigParser()
        cls._accounts = []  # 清空原有账号列表
        
        try:
            # 如果文件不存在，自动生成
            if not os.path.exists(cls._accounts_file):
                logger.warning("账号配置文件不存在，自动生成...")
                cls.generate_batch_accounts()
                
            # 读取配置文件
            config.read(cls._accounts_file, encoding='utf-8')
            
            if 'Accounts' in config:
                for key in sorted(config['Accounts'], 
                                key=lambda x: int(x.replace('account',''))):
                    cls._accounts.append(config['Accounts'][key])
                    
                logger.warning(f"已加载 {len(cls._accounts)} 个账号")
                
            # 如果加载失败或数量不足，重新生成
            if len(cls._accounts) != 1000:
                logger.warning("账号数量不足1000，重新生成...")
                cls.generate_batch_accounts()
                config.read(cls._accounts_file, encoding='utf-8')
                cls._accounts = list(config['Accounts'].values())
                
        except Exception as e:
            logger.error(f"加载账号失败: {str(e)}")
            cls.generate_batch_accounts()
            
        cls._accounts_loaded = True 