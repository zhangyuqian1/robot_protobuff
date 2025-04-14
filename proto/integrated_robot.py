import asyncio
import logging
import random
import time
import os
import platform
import signal
import gc
import psutil
import struct
import configparser
from async_protocol_handler import AsyncProtocolHandler
from async_game_client import AsyncGameClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('IntegratedRobot')

class IntegratedRobot:
    """整合了网络功能的异步机器人类，不再依赖外部网络管理器"""
    
    # 类变量，用于管理账号列表
    _accounts = []
    _current_account_index = 0
    _accounts_loaded = False
    
    @classmethod
    def load_accounts(cls):
        """加载账号配置文件"""
        if cls._accounts_loaded:
            return
            
        config = configparser.ConfigParser()
        config_file = os.path.join('conf', 'account.ini')
        
        try:
            if os.path.exists(config_file):
                config.read(config_file, encoding='utf-8')
                if 'Accounts' in config:
                    # 按顺序加载账号
                    accounts = []
                    for key in sorted(config['Accounts'], 
                                   key=lambda x: int(x.replace('account',''))):
                        accounts.append(config['Accounts'][key])
                    cls._accounts = accounts
                    logger.warning(f"已加载 {len(cls._accounts)} 个账号")
                else:
                    logger.error("账号配置文件格式错误，缺少[Accounts]段")
            else:
                logger.error(f"账号配置文件 {config_file} 不存在")
                
        except Exception as e:
            logger.error(f"加载账号配置失败: {str(e)}")
            
        cls._accounts_loaded = True
    
    @classmethod
    def get_next_account(cls):
        """获取下一个账号"""
        if not cls._accounts_loaded:
            cls.load_accounts()
            
        if not cls._accounts:
            return None
            
        # 循环使用账号列表
        account = cls._accounts[cls._current_account_index]
        cls._current_account_index = (cls._current_account_index + 1) % len(cls._accounts)
        return account
    
    def __init__(self, host, port, robot_id=None):
        self.host = host
        self.port = port
        self.robot_id = robot_id or f"Robot_{random.randint(1, 1000)}"
        
        # 确保账号列表已加载
        if not self.__class__._accounts_loaded:
            self.__class__.load_accounts()
        
        # 获取分配的账号
        self.assigned_account = self.__class__.get_next_account()
        if not self.assigned_account:
            raise ValueError("没有可用的配置账号")
        
        # 网络连接相关属性
        self.reader = None
        self.writer = None
        self.is_alive = False
        self.connection_id = f"{self.robot_id}_{int(time.time())}"
        self.last_activity = 0
        self.buffer = bytearray()
        self._receive_task = None
        
        # 协议处理器
        self.protocol = AsyncProtocolHandler()
        
        # 游戏客户端 - 传入self作为网络接口
        self.game = AsyncGameClient(self, self.protocol, self.robot_id)
        
        # 运行状态
        self.is_running = False
        
        logger.info(f"创建机器人 {self.robot_id}，分配账号: {self.assigned_account}")
        
    # ===== 网络连接功能 =====
    
    async def connect(self):
        max_retries = 5  # 最大重试次数
        retry_delay = 1  # 初始重试延迟（秒）
        for i in range(1,max_retries+1):
            """连接到服务器"""
            try:
                self.reader, self.writer = await asyncio.open_connection(
                    self.host, self.port)
                self.is_alive = True
                self.last_activity = time.time()
                logger.info(f"机器人 {self.robot_id} 连接到服务器 {self.host}:{self.port} 成功")
                return True
            except (ConnectionRefusedError, TimeoutError) as e:
                if i < max_retries:
                    logger.warning(f"机器人 {self.robot_id} 连接失败（{str(e)}），{retry_delay}秒后重试...")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 2  # 指数退避
                else:
                    logger.error(f"机器人 {self.robot_id} 连接失败（{str(e)}），已达最大重试次数")
                    break
            except Exception as e:
                logger.error(f"机器人 {self.robot_id} 连接服务器失败: {str(e)}")
                self.is_alive = False
                return False
    
    async def close(self):
        """简化的关闭方法"""
        self.is_running = False
        
        # 取消接收任务
        if self._receive_task and not self._receive_task.done():
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass
        
        # 关闭网络连接
        if self.is_alive and self.writer:
            self.is_alive = False
            try:
                self.writer.close()
                await self.writer.wait_closed()
                logger.info(f"机器人 {self.robot_id} 连接已关闭")
            except Exception as e:
                logger.error(f"机器人 {self.robot_id} 关闭连接时出错: {str(e)}")
    
    async def send_data(self, data):
        """发送数据到服务器"""
        if not self.is_alive or not self.writer:
            logger.warning(f"机器人 {self.robot_id} 尝试发送数据但连接未建立或已关闭")
            return False
            
        try:
            self.writer.write(data)
            await self.writer.drain()
            self.last_activity = time.time()
            return True
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 发送数据失败: {str(e)}")
            self.is_alive = False
            return False
    
    async def receive_data(self, timeout=None):
        """接收数据，处理分包和粘包"""
        if not self.is_alive or not self.reader:
            return None
        
        try:
            # 读取可用数据
            data = await asyncio.wait_for(self.reader.read(8192), timeout)
            
            if not data:
                logger.warning(f"机器人 {self.robot_id} 服务器关闭了连接")
                self.is_alive = False
                return None
            
            # 将新数据添加到缓冲区
            self.buffer.extend(data)
            self.last_activity = time.time()
            
            # 处理完整消息包
            if len(self.buffer) >= 2:
                # 解析消息长度（前2个字节）
                msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                # 检查是否有完整的消息
                if len(self.buffer) >= msg_len + 2:
                    # 提取完整消息包
                    packet = bytes(self.buffer[:msg_len+2])
                    # 更新缓冲区，移除已处理的消息
                    self.buffer = self.buffer[msg_len+2:]
                    # logger.info(f"机器人 {self.robot_id} 接收数据: {packet}")
                    return packet
            
            # 没有完整消息，返回None
            return None
        
        except asyncio.TimeoutError:
            # 超时不是错误，只是当前没有数据
            return None
        except (asyncio.IncompleteReadError, ConnectionError):
            logger.warning(f"机器人 {self.robot_id} 连接已关闭")
            self.is_alive = False
            return None
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 接收数据失败: {str(e)}")
            self.is_alive = False
            return None
    
    async def start_receive_loop(self):
        """启动异步接收循环"""
        # 确保旧任务已取消
        if self._receive_task and not self._receive_task.done():
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass
        
        # 创建新的接收任务
        self._receive_task = asyncio.create_task(self._receive_loop())
        return self._receive_task
    
    async def _receive_loop(self):
        """简化的接收循环 - 直接处理消息"""
        logger.info(f"机器人 {self.robot_id} 开始接收数据循环")
        
        try:
            while self.is_alive and self.is_running:
                # 接收消息
                packet = await self.receive_data(timeout=1)
                
                # 如果有完整消息，直接处理
                if packet:
                    # 解析协议
                    parsed, name, pid = await self.protocol.parse_packet(packet)
                    if parsed:
                        logger.info(f"机器人 {self.robot_id} 处理消息: [{pid}]{name}")
                        # 直接分发协议
                        await self.protocol.dispatch_protocol(pid, parsed, name)
                
                # 处理缓冲区中的其他完整消息
                while len(self.buffer) >= 2:
                    msg_len = int.from_bytes(self.buffer[:2], byteorder='big')
                    if len(self.buffer) < msg_len + 2:
                        break  # 没有完整消息了
                    
                    # 提取下一个完整消息
                    next_packet = bytes(self.buffer[:msg_len+2])
                    self.buffer = self.buffer[msg_len+2:]
                    
                    # 直接处理消息
                    parsed, name, pid = await self.protocol.parse_packet(next_packet)
                    if parsed:
                        # logger.info(f"机器人 {self.robot_id} 处理缓冲消息: [{pid}]{name}")
                        await self.protocol.dispatch_protocol(pid, parsed, name)
                
                # 短暂休眠，避免CPU占用过高
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            logger.info(f"机器人 {self.robot_id} 接收循环被取消")
            raise
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 接收循环中出错: {str(e)}")
        finally:
            logger.info(f"机器人 {self.robot_id} 接收数据循环已结束")
    
    # ===== 机器人控制功能 =====
    
    async def run(self):
        """简化的运行方法"""
        try:
            self.is_running = True
            
            # 连接服务器
            if not await self.connect():
                logger.error(f"机器人 {self.robot_id} 连接服务器失败，机器人退出")
                return
                
            # 启动接收循环
            await self.start_receive_loop()
            logger.info(f"机器人 {self.robot_id} 接收循环已启动，等待稳定...")
            await asyncio.sleep(0.5)  # 给接收循环一点时间稳定
            
            # 执行登录流程（使用分配的账号）
            logger.info(f"分配的账号{self.assigned_account}")
            await self.game.execute_login_sequence(self.assigned_account)
            
            # 主循环，保持程序运行
            logger.info(f"机器人 {self.robot_id} 已启动，运行中...")
            while self.is_alive and self.is_running:
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            logger.info(f"机器人 {self.robot_id} 被取消")
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 运行错误: {str(e)}")
        finally:
            await self.close()
            logger.info(f"机器人 {self.robot_id} 已关闭")


class RobotManager:
    """机器人管理器，管理多个机器人实例"""
    
    def __init__(self, host, port, robot_count=1000):
        self.host = host
        self.port = port
        self.robot_count = robot_count
        self.robots = []
        self.is_running = False
        self.start_time = None
        self.next_id = 1
        
        # 性能指标
        self.metrics = {
            'started_robots': 0,
            'active_robots': 0,
            'failed_robots': 0
        }
        
        # 预加载账号配置
        IntegratedRobot.load_accounts()
        
        # 检查账号数量是否足够
        available_accounts = len(IntegratedRobot._accounts)
        if available_accounts < robot_count:
            logger.error(f"账号不足！需要 {robot_count} 个，但配置中只有 {available_accounts} 个")
            raise ValueError("账号数量不足")
            
    async def start_robots(self, batch_size=5, delay_between_batches=0):
        """分批启动机器人"""
        self.is_running = True
        self.start_time = time.time()
        
        # 保守的批次设置
        actual_batch = max(0, batch_size)
        actual_delay = max(0.0000001, delay_between_batches)
        
        logger.info(f"开始启动 {self.robot_count} 个机器人，批次大小: {actual_batch}")
        
        try:
            for i in range(0, self.robot_count, actual_batch):
                # 计算当前批次需要启动的机器人数量
                current_batch = min(actual_batch, self.robot_count - i)
                batch_robots = []
                
                # 创建并启动当前批次的机器人
                for j in range(current_batch):
                    try:
                        robot_id = self.next_id
                        # 使用新的整合机器人类
                        robot = IntegratedRobot(self.host, self.port, robot_id)
                        self.next_id += 1
                        # 启动机器人
                        task = asyncio.create_task(robot.run())
                        batch_robots.append((robot, task))
                        self.robots.append((robot, task))
                        self.metrics['started_robots'] += 1
                        
                        # 每个机器人启动间隔
                        await asyncio.sleep(0.05)
                        
                    except Exception as e:
                        logger.error(f"创建机器人 {robot_id} 失败: {str(e)}")
                        self.metrics['failed_robots'] += 1
                
                # 打印当前批次信息
                logger.warning(f"已启动批次 {i//actual_batch + 1}/{(self.robot_count-1)//actual_batch + 1}，"
                          f"当前批次 {current_batch} 个机器人")
                
                #等待指定时间再启动下一批
                if i + actual_batch < self.robot_count:
                    logger.warning(f"等待 {actual_delay} 秒启动下一批")
                    await asyncio.sleep(actual_delay)
                    
            logger.warning(f"所有机器人启动完成，总计: {len(self.robots)}")
            
        except asyncio.CancelledError:
            logger.info("机器人启动过程被取消")
            raise
        except Exception as e:
            logger.error(f"启动机器人时发生错误: {str(e)}")
            
    async def stop_all_robots(self):
        """停止所有机器人"""
        logger.info("开始停止所有机器人...")
        
        stop_tasks = []
        for robot, task in self.robots:
            # 取消任务
            if not task.done():
                task.cancel()
            
            # 关闭机器人
            stop_tasks.append(robot.close())
        
        # 等待所有机器人关闭
        if stop_tasks:
            await asyncio.gather(*stop_tasks, return_exceptions=True)
            
        # 清空列表
        self.robots.clear()
        self.is_running = False
        logger.info("所有机器人已停止")
        
    async def monitor_status(self, interval=5):
        """监控所有机器人状态"""
        try:
            last_gc_time = time.time()
            gc_interval = 60  # 至少每60秒执行一次GC
            
            while self.is_running:
                # 计算内存使用
                process = psutil.Process(os.getpid())
                memory_mb = process.memory_info().rss / 1024 / 1024
                
                # 强制GC条件判断优化
                gc_conditions = [
                    (time.time() - last_gc_time) > gc_interval,  # 时间间隔条件
                    memory_mb > 1024 and (memory_mb % 200 < 5),  # 内存量条件
                    len(gc.garbage) > 100  # 存在未回收垃圾
                ]
                
                if any(gc_conditions):
                    logger.warning(f"执行垃圾回收(内存:{memory_mb:.1f}MB, 未回收对象:{len(gc.garbage)})")
                    gc.collect()
                    gc.garbage.clear()
                    last_gc_time = time.time()
                    logger.warning(f"GC后内存:{process.memory_info().rss/1024/1024:.1f}MB")
                
                # 计算活跃机器人数量
                active_count = sum(1 for robot, task in self.robots 
                                  if robot.is_alive and not task.done())
                self.metrics['active_robots'] = active_count
                
                # 计算运行时间
                runtime = time.time() - self.start_time if self.start_time else 0
                runtime_str = time.strftime("%H:%M:%S", time.gmtime(runtime))
                
                # 打印状态信息
                logger.info(f"状态报告 - 运行时间: {runtime_str}")
                logger.warning(f"\33[91m已启动: {self.metrics['started_robots']}, "
                           f"活跃: {active_count}, "
                           f"失败: {self.metrics['failed_robots']}\33[0m")
                
                # 收集内存使用情况
                memory_mb = process.memory_info().rss / 1024 / 1024
                logger.warning(f"内存使用: {memory_mb:.2f} MB")
                
                # 等待下一次监控
                await asyncio.sleep(interval)
                
        except asyncio.CancelledError:
            logger.info("状态监控被取消")
        except Exception as e:
            logger.error(f"监控状态时出错: {str(e)}")

# 主函数和其他辅助函数

async def run_multiple_robots(host, port, robot_count=1000, batch_size=50, delay=1):
    """运行多个机器人的主函数"""
    # 创建管理器
    manager = RobotManager(host, port, robot_count)
    
    try:
        # 在Windows上处理信号的替代方案
        if platform.system() != "Windows":
            # 非Windows系统使用标准信号处理
            loop = asyncio.get_running_loop()
            for sig in (signal.SIGINT, signal.SIGTERM):
                loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown(manager)))
        else:
            # Windows系统忽略信号处理
            logger.info("Windows系统不支持信号处理，使用Ctrl+C终止程序")
        
        # 启动状态监控
        monitor_task = asyncio.create_task(manager.monitor_status())
        
        # 启动机器人
        await manager.start_robots(batch_size, delay)
        
        # 保持运行直到收到信号
        while manager.is_running:
            await asyncio.sleep(1)
            
    except asyncio.CancelledError:
        logger.info("主程序被取消")
    except KeyboardInterrupt:
        logger.info("收到键盘中断")
    finally:
        # 停止监控
        if 'monitor_task' in locals() and not monitor_task.done():
            monitor_task.cancel()
            
        # 确保所有机器人都被正确关闭
        await manager.stop_all_robots()
        
    logger.info("程序结束")

async def shutdown(manager):
    """优雅关闭程序"""
    logger.info("接收到关闭信号，开始关闭...")
    manager.is_running = False
    await manager.stop_all_robots()

async def run_single_robot(host, port):
    """运行单个机器人的简化函数"""
    robot = IntegratedRobot(host, port)
    try:
        await robot.run()
    finally:
        await robot.close()

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='集成式异步游戏机器人')
    parser.add_argument('--host', default='192.168.56.101', help='服务器主机名')
    parser.add_argument('--port', type=int, default=7011, help='服务器端口')
    parser.add_argument('--count', type=int, default=1, help='机器人数量')
    parser.add_argument('--batch', type=int, default=5, help='批量启动大小')
    parser.add_argument('--delay', type=float, default=1, help='批次间延迟(秒)')
    args = parser.parse_args()
    
    # 设置日志级别
    if args.count >= 100:
        logging.getLogger().setLevel(logging.WARNING)
    
    # 运行机器人
    if args.count == 1:
        asyncio.run(run_single_robot(args.host, args.port))
    else:
        asyncio.run(run_multiple_robots(
            args.host, args.port, args.count, args.batch, args.delay))

if __name__ == "__main__":
    main() 