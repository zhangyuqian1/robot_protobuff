import argparse
import time
import asyncio
import logging
import random
import signal
import os
from async_network_manager import AsyncNetworkManager
from async_protocol_handler import AsyncProtocolHandler
from async_game_client import AsyncGameClient
import struct
import psutil
import gc
import platform

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AsyncRobot')

class AsyncRobot:
    """异步机器人类，支持异步操作"""
    
    def __init__(self, host, port, robot_id=None):
        self.host = host
        self.port = port
        self.robot_id = robot_id or f"Robot_{random.randint(1, 1000)}"
        
        # 确保完全独立的组件实例
        self.network = AsyncNetworkManager(host, port,self.robot_id)
        
        # 创建独立的协议处理器，并指定唯一ID
        self.protocol = AsyncProtocolHandler()
        
        # 传递协议处理器到游戏客户端
        self.game = AsyncGameClient(self.network, self.protocol, self.robot_id)
        
        logger.debug(f"机器人 {self.robot_id} 初始化: 网络组件ID={id(self.network)}, 协议处理器ID={id(self.protocol)}")
        
        self.is_running = False
        
    async def handle_packet(self, packet):
        """处理接收到的数据包"""
        parsed, name, pid = await self.protocol.parse_packet(packet)
        if parsed:
            await self.protocol.dispatch_protocol(pid, parsed, name)
        
    async def run(self):
        """运行机器人"""
        try:
            self.is_running = True
            
            # 连接服务器
            if not await self.network.connect():
                logger.error(f"{self.robot_id} 连接服务器失败，机器人退出")
                return
                
            # 启动接收线程
            await self.network.start_receive_loop(self.handle_packet)
            # logger.info("接收循环已启动，等待稳定...")
            await asyncio.sleep(1)  # 给接收循环一点时间稳定
            # 执行登录流程
            await self.game.execute_login_sequence()
            
            # 主循环，保持程序运行
            logger.info(f"{self.robot_id} 已启动，运行中...")
            while self.network.is_alive and self.is_running:
                # 更新游戏状态
                # await self.game.update()
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            logger.info(f"{self.robot_id} 被取消")
        except Exception as e:
            logger.error(f"{self.robot_id} 运行错误: {str(e)}")
        finally:
            await self.close()
            logger.info(f"{self.robot_id} 已关闭")
            
    async def close(self):
        """关闭机器人"""
        self.is_running = False
        if self.network:
            await self.network.close()

class RobotManager:
    """机器人管理器，管理多个机器人实例"""
    
    def __init__(self, host, port, robot_count=1000):
        self.host = host
        self.port = port
        self.robot_count = robot_count
        self.robots = []
        self.is_running = False
        self.start_time = None
        self.next_id = 1  # 新增顺序计数器
        
        # 性能指标
        self.metrics = {
            'started_robots': 0,
            'active_robots': 0,
            'failed_robots': 0
        }
        
    async def start_robots(self, batch_size=50, delay_between_batches=1):
        """分批启动机器人"""
        self.is_running = True
        self.start_time = time.time()
        
        logger.info(f"开始启动 {self.robot_count} 个机器人，批次大小: {batch_size}")
        
        try:
            for i in range(0, self.robot_count, batch_size):
                # 计算当前批次需要启动的机器人数量
                current_batch = min(batch_size, self.robot_count - i)
                batch_robots = []
                
                # 创建并启动当前批次的机器人
                for j in range(current_batch):
                    try:
                        robot_id = f"Robot_{self.next_id}"  # 使用顺序ID
                        # print(f"创建机器人 {robot_id}")
                        robot = AsyncRobot(self.host, self.port, self.next_id)
                        self.next_id += 1  # 递增计数器
                        task = asyncio.create_task(robot.run())
                        batch_robots.append((robot, task))
                        self.robots.append((robot, task))
                        self.metrics['started_robots'] += 1
                    except Exception as e:
                        logger.error(f"创建机器人 {robot_id} 失败: {str(e)}")
                        self.metrics['failed_robots'] += 1
                
                # 打印当前批次信息
                logger.warning(f"已启动批次 {i//batch_size + 1}/{(self.robot_count-1)//batch_size + 1}，"
                          f"当前批次 {current_batch} 个机器人")
                
                # 等待指定时间再启动下一批
                if i + batch_size < self.robot_count:
                    await asyncio.sleep(delay_between_batches)
                    
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
                                  if robot.network.is_alive and not task.done())
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
    robot = AsyncRobot(host, port)
    try:
        await robot.run()
    finally:
        await robot.close()

def main():

    
    
    parser = argparse.ArgumentParser(description='异步游戏机器人')
    parser.add_argument('--host', default='192.168.56.101', help='服务器主机名')
    parser.add_argument('--port', type=int, default=7011, help='服务器端口')
    parser.add_argument('--count', type=int, default=1, help='机器人数量')
    parser.add_argument('--batch', type=int, default=50, help='批量启动大小')
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
    #python robot_async.py --host 192.168.56.101 --port 7011 --count 1 --batch 1 --delay 1
if __name__ == "__main__":
    main()    