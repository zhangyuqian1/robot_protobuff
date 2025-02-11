from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from Agent import Agent

class BeginAgentService(QThread):
    """
     启动转发代理的thread类
     """
    # 定义两个信号，信号参数类型为str，在信号触发的时候，会将str参数传给绑定的ui方法
    send_signal = pyqtSignal(str)
    recv_signal = pyqtSignal(str)

    def __init__(self,agent_host, agent_port, server_host, server_port,parent=None, ui=None):
        super(BeginAgentService,self).__init__(parent=None)
        self.ui = ui
        self.agent_host = agent_host
        self.agent_port = agent_port
        self.server_host = server_host
        self.server_port = server_port

    def run (self):
        self.ui.agent = Agent(self.agent_host, self.agent_port, self.server_host, self.server_port, self)
        self.ui.agent.start()

