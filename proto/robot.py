import time
from network_manager import NetworkManager
from protocol_handler import ProtocolHandler
from game_client import GameClient

class SimpleRobot:
    """机器人主类，整合网络和游戏功能"""
    
    def __init__(self, host, port):
        # 创建模块化组件
        self.network = NetworkManager(host, port)
        self.protocol = ProtocolHandler()
        self.game = GameClient(self.network, self.protocol)
        
    def handle_packet(self, packet):
        """处理接收到的数据包"""
        parsed, name, pid = self.protocol.parse_packet(packet)
        if parsed:
            self.protocol.dispatch_protocol(pid, parsed, name)
        
    def run(self):
        """运行机器人"""
        try:
            # 连接服务器
            if not self.network.connect():
                print("连接服务器失败，程序退出")
                return
                
            # 启动接收线程
            self.network.start_receive_loop(self.handle_packet)
            
            # 执行登录流程
            self.game.execute_login_sequence()
            
            # 主循环，保持程序运行
            print("机器人已启动，按Ctrl+C退出")
            while self.network.is_alive:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("用户中断，程序退出")
        finally:
            self.network.close()
            print("机器人已关闭")
            
    def close(self):
        """关闭机器人"""
        self.network.close()


# 使用示例
if __name__ == "__main__":
    robot = SimpleRobot("192.168.56.101", 7011)
    robot.run()
   