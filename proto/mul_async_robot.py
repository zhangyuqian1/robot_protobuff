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
import sys
import multiprocessing
from async_protocol_handler import AsyncProtocolHandler
from async_game_client import AsyncGameClient

# 配置基本日志
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MultiprocessRobot')
logger.setLevel(logging.WARNING)  # 显式设置logger级别

class IntegratedRobot:
    """整合了网络功能的异步机器人类，不再依赖外部网络管理器"""
    
    def __init__(self, host, port, robot_id=None):
        self.host = host
        self.port = port
        self.robot_id = robot_id or f"Robot_{random.randint(1, 1000)}"
        
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
        
        logger.info(f"创建机器人 {self.robot_id}")
        
    # ===== 网络连接功能 =====
    
    async def connect(self):
        """连接到服务器（含重试机制）"""
        max_retries = 5  # 最大重试次数
        retry_delay = 1  # 初始重试延迟（秒）
        
        for attempt in range(1, max_retries+1):
            try:
                self.reader, self.writer = await asyncio.open_connection(
                    self.host, self.port)
                self.is_alive = True
                self.last_activity = time.time()
                logger.warning(f"机器人 {self.robot_id} 连接成功（第{attempt}次尝试）")  # 使用warning级别
                return True
            except (ConnectionRefusedError, TimeoutError) as e:
                if attempt < max_retries:
                    logger.warning(f"机器人 {self.robot_id} 连接失败（{str(e)}），{retry_delay}秒后重试...")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 2  # 指数退避
                else:
                    logger.error(f"机器人 {self.robot_id} 连接失败（{str(e)}），已达最大重试次数")
                    break
            except Exception as e:
                logger.error(f"机器人 {self.robot_id} 连接遇到意外错误: {str(e)}")
                break
                
        self.is_alive = False
        return False
    
    async def close(self):
        """关闭连接和任务"""
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
        """接收循环 - 直接处理消息"""
        # logger.info(f"机器人 {self.robot_id} 开始接收数据循环")
        
        try:
            while self.is_alive and self.is_running:
                # 接收消息
                packet = await self.receive_data(timeout=1)
                
                # 如果有完整消息，直接处理
                if packet:
                    # 解析协议
                    parsed, name, pid = await self.protocol.parse_packet(packet)
                    if parsed:
                        # logger.info(f"机器人 {self.robot_id} 处理消息: [{pid}]{name}")
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
                await asyncio.sleep(0.01)
                
        except asyncio.CancelledError:
            logger.info(f"机器人 {self.robot_id} 接收循环被取消")
            raise
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 接收循环中出错: {str(e)}")
        finally:
            logger.info(f"机器人 {self.robot_id} 接收数据循环已结束")
    
    # ===== 机器人控制功能 =====
    
    async def run(self):
        """运行机器人"""
        try:
            self.is_running = True
            
            # 连接服务器
            if not await self.connect():
                logger.error(f"机器人 {self.robot_id} 连接服务器失败，机器人退出")
                return
                
            # 启动接收循环
            await self.start_receive_loop()
            # logger.info(f"机器人 {self.robot_id} 接收循环已启动，等待稳定...")
            await asyncio.sleep(0.5)  # 给接收循环一点时间稳定
            
            # 执行登录流程
            await self.game.execute_login_sequence()
            
            # 主循环，保持程序运行
            # logger.info(f"机器人 {self.robot_id} 已启动，运行中...")
            while self.is_alive and self.is_running:
                await asyncio.sleep(1)
                
        except asyncio.CancelledError:
            logger.info(f"机器人 {self.robot_id} 被取消")
        except Exception as e:
            logger.error(f"机器人 {self.robot_id} 运行错误: {str(e)}")
        finally:
            await self.close()
            logger.info(f"机器人 {self.robot_id} 已关闭")


class ProcessRobotManager:
    """单个进程内的机器人管理器"""
    
    def __init__(self, host, port, robot_count, start_id, process_id):
        self.host = host
        self.port = port
        self.robot_count = robot_count
        self.start_id = start_id
        self.process_id = process_id
        self.robots = []
        self.is_running = False
        self.start_time = None
        
        # 性能指标
        self.metrics = {
            'started_robots': 0,
            'active_robots': 0,
            'failed_robots': 0
        }
        
        logger.warning(f"进程 {process_id} 初始化, 将管理 {robot_count} 个机器人, ID范围: {start_id}~{start_id+robot_count-1}")
        
    async def start_robots_sequential(self):
        """逐个启动机器人，确保稳定性"""
        self.is_running = True
        self.start_time = time.time()
        
        next_id = self.start_id
        end_id = self.start_id + self.robot_count
        
        logger.warning(f"进程 {self.process_id} 开始启动 {self.robot_count} 个机器人")
        
        try:
            while next_id < end_id:
                try:
                    # 创建单个机器人
                    robot_id = next_id
                    robot = IntegratedRobot(self.host, self.port, robot_id)
                    next_id += 1
                    
                    # 启动机器人
                    task = asyncio.create_task(robot.run())
                    self.robots.append((robot, task))
                    self.metrics['started_robots'] += 1
                    
                    # 每个机器人启动后等待一小段时间确保完全初始化
                    delay_time = 0.5  # 固定的启动间隔
                    
                    # logger.info(f"启动机器人 {robot_id}，等待 {delay_time}秒")
                    await asyncio.sleep(delay_time)
                    
                    # 每启动10个机器人打印一次进度
                    if self.metrics['started_robots'] % 10 == 0:
                        logger.warning(f"进程 {self.process_id} 已启动 {self.metrics['started_robots']}/{self.robot_count} 个机器人")
                    
                except Exception as e:
                    logger.error(f"创建机器人 {next_id} 失败: {str(e)}")
                    self.metrics['failed_robots'] += 1
                    await asyncio.sleep(1)  # 失败后稍微多等一会
            
            logger.warning(f"进程 {self.process_id} 机器人启动完成，总计: {self.metrics['started_robots']}")
            
        except asyncio.CancelledError:
            logger.info(f"进程 {self.process_id} 机器人启动过程被取消")
            raise
        except Exception as e:
            logger.error(f"启动机器人时发生错误: {str(e)}")
            
    async def stop_all_robots(self):
        """停止所有机器人"""
        logger.info(f"进程 {self.process_id} 开始停止所有机器人...")
        
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
        logger.info(f"进程 {self.process_id} 所有机器人已停止")
        
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
                    logger.warning(f"进程 {self.process_id} 执行垃圾回收(内存:{memory_mb:.1f}MB)")
                    gc.collect()
                    gc.garbage.clear()
                    last_gc_time = time.time()
                    logger.warning(f"进程 {self.process_id} GC后内存:{process.memory_info().rss/1024/1024:.1f}MB")
                
                # 计算活跃机器人数量
                active_count = sum(1 for robot, task in self.robots 
                                  if robot.is_alive and not task.done())
                self.metrics['active_robots'] = active_count
                
                # 计算运行时间
                runtime = time.time() - self.start_time if self.start_time else 0
                runtime_str = time.strftime("%H:%M:%S", time.gmtime(runtime))
                
                # 打印状态信息
                logger.info(f"进程 {self.process_id} 状态报告 - 运行时间: {runtime_str}")
                logger.warning(f"进程 {self.process_id} \33[91m已启动: {self.metrics['started_robots']}, "
                           f"活跃: {active_count}, "
                           f"失败: {self.metrics['failed_robots']}\33[0m")
                
                # 收集内存使用情况
                memory_mb = process.memory_info().rss / 1024 / 1024
                logger.warning(f"进程 {self.process_id} 内存使用: {memory_mb:.2f} MB")
                
                # 等待下一次监控
                await asyncio.sleep(interval)
                
        except asyncio.CancelledError:
            logger.info(f"进程 {self.process_id} 状态监控被取消")
        except Exception as e:
            logger.error(f"进程 {self.process_id} 监控状态时出错: {str(e)}")

# 异步进程入口函数
async def process_main(host, port, robot_count, start_id, process_id):
    """每个进程的异步主函数"""
    logger.info(f"进程 {process_id} 开始运行，管理 {robot_count} 个机器人")
    
    manager = ProcessRobotManager(host, port, robot_count, start_id, process_id)
    
    try:
        # 启动状态监控
        monitor_task = asyncio.create_task(manager.monitor_status())
        
        # 启动机器人
        await manager.start_robots_sequential()
        
        # 保持运行直到收到信号
        while manager.is_running:
            await asyncio.sleep(1)
            
    except asyncio.CancelledError:
        logger.info(f"进程 {process_id} 被取消")
    except KeyboardInterrupt:
        logger.info(f"进程 {process_id} 收到键盘中断")
    finally:
        # 停止监控
        if 'monitor_task' in locals() and not monitor_task.done():
            monitor_task.cancel()
            
        # 确保所有机器人都被正确关闭
        await manager.stop_all_robots()
        
    logger.info(f"进程 {process_id} 结束")

# 进程启动函数
def run_process(host, port, robot_count, start_id, process_id):
    """进程入口函数，设置日志并启动异步循环"""
    # 设置进程特定的日志文件
    log_filename = f"robot_process_{process_id}.log"
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    file_handler.setLevel(logging.WARNING)  # 设置文件handler级别
    logger.addHandler(file_handler)
    
    # 大量机器人时降低日志级别
    if robot_count > 100:
        logger.setLevel(logging.WARNING)
    
    # 调整进程名称以便于识别
    try:
        import setproctitle
        setproctitle.setproctitle(f"robot_process_{process_id}")
    except ImportError:
        pass
    
    print(f"进程 {process_id} 启动: 管理 {robot_count} 个机器人，ID范围 {start_id}~{start_id+robot_count-1}")
    
    # 启动异步主循环
    asyncio.run(process_main(host, port, robot_count, start_id, process_id))

# 主函数
def main():
    
    import argparse
    
    parser = argparse.ArgumentParser(description='多进程游戏机器人')
    parser.add_argument('--host', default='192.168.56.101', help='服务器主机名')
    parser.add_argument('--port', type=int, default=7011, help='服务器端口')
    parser.add_argument('--count', type=int, default=10, help='机器人总数量')
    parser.add_argument('--processes', type=int, default=2, help='进程数量')
    parser.add_argument('--log-dir', default='logs', help='日志目录')
    args = parser.parse_args()
    
    # 创建日志目录
    os.makedirs(args.log_dir, exist_ok=True)
    
    # 写入主进程日志到文件
    main_log_handler = logging.FileHandler(f"{args.log_dir}/main_process.log")
    main_log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    main_log_handler.setLevel(logging.WARNING)  # 设置主进程日志级别
    logger.addHandler(main_log_handler)
    
    # 单进程模式
    if args.processes == 1 or args.count <= 5:
        logger.info(f"使用单进程模式运行 {args.count} 个机器人")
        asyncio.run(process_main(args.host, args.port, args.count, 1, 1))
    else:
        # 多进程模式
        logger.info(f"使用 {args.processes} 个进程运行共 {args.count} 个机器人")
        
        # 计算每个进程的机器人数量和起始ID
        robots_per_process = args.count // args.processes
        remainder = args.count % args.processes
        
        processes = []
        start_id = 1
        
        # 创建和启动进程
        for i in range(args.processes):
            # 分配机器人数量，最后一个进程处理余数
            if i == args.processes - 1:
                process_robot_count = robots_per_process + remainder
            else:
                process_robot_count = robots_per_process
            
            # 创建进程
            p = multiprocessing.Process(
                target=run_process,
                args=(args.host, args.port, process_robot_count, start_id, i+1)
            )
            
            # 更新下一个进程的起始ID
            start_id += process_robot_count
            
            # 启动进程
            p.start()
            processes.append(p)
            
            # 等待一小段时间再启动下一个进程
            time.sleep(3)
        
        logger.warning(f"已启动 {len(processes)} 个进程")
        
        try:
            # 等待所有进程完成
            for p in processes:
                p.join()
        except KeyboardInterrupt:
            logger.warning("收到键盘中断，正在终止所有进程...")
            for p in processes:
                if p.is_alive():
                    p.terminate()
            # 等待进程终止
            for p in processes:
                p.join()
        
        logger.info("所有进程已结束")

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Windows多进程支持
    main()