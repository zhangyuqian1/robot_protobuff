from panel import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from Qthread import *
import proto_mapper
import ast
from Xor import XORCipher  # 添加导入


class Tool_Panel(Ui_MainWindow, QMainWindow):
    def __init__(self,parent = None):
        super(Tool_Panel, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.agent = None  # 先给它个空对象，占个属性名
        self.proto_mapper = proto_mapper.ProtobufMapper()  # 创建实例
        self.proto_mapper.load_proto_files()  # 加载proto文件
        self.ui.pushButton.clicked.connect(self.start)
        self.ui.pushButton_2.clicked.connect(self.stop)
        self.ui.pushButton_3.clicked.connect(self.create_message)
        self.ui.pushButton_6.clicked.connect(self.send_custom_protobuf)
        self.ui.clearRecvBtn.clicked.connect(self.ui.textBrowser.clear)
        self.ui.clearSendBtn.clicked.connect(self.ui.textBrowser_2.clear)
        
    def start(self):
        """
            代理启动方法
            :return:
        """
        # 获取文本框中的ip和端口等信息
        # agent_host = self.ui.lineEdit.text()
        agent_host = "127.0.0.1"
        # agent_port = int(self.ui.lineEdit_2.text())
        agent_port = "7011"
        # server_host = self.ui.lineEdit_3.text()
        server_host = "192.168.56.66"
        # server_port = int(self.ui.lineEdit_4.text())
        server_port = 7011
        # 生成Q线程
        self.agent_thread = BeginAgentService(agent_host, agent_port, server_host, server_port, ui=self)
        self.agent_thread.send_signal.connect(self.send_proto_view)
        self.agent_thread.recv_signal.connect(self.recv_proto_view)
        # 启动Q线程
        self.agent_thread.start()



    def stop(self):
            """
            代理停止方法
            :return:
            """
            self.agent.stop()

    def recv_proto_view(self, recv_proto):
        """
        将收到协议的内容展示到文本框中
        :param send_proto::return:
        """
        self.ui.textBrowser.append(recv_proto)
    def send_proto_view(self, send_proto):
        """
        将发送协议的内容展示到文本框中
        :param recv_proto::return:
        """
        self.ui.textBrowser_2.append(send_proto)

    def create_message(self):
        """
        创建客户端消息并显示
        """
        input_text = self.ui.lineEdit_5.text()
        # 假设input_text是协议ID的数字
        try:
            protocol_id = int(input_text)
            result = self.proto_mapper.create_client_message(protocol_id)
            self.ui.textEdit.setText(str(result))
        except ValueError:
            self.ui.textEdit.setText("请输入有效的协议ID（数字）")

    def send_custom_protobuf(self):
        """
        发送自定义protobuf消息
        """
        try:
            # 获取协议ID
            protocol_id = int(self.ui.lineEdit_5.text())
            
            # 获取并验证消息内容
            input_text = self.ui.textEdit.toPlainText().strip()
            if not input_text:
                raise ValueError("消息内容不能为空")
                
            # 安全转换输入内容
            try:
                message_data = ast.literal_eval(input_text)
            except Exception as e:
                raise ValueError(f"消息格式错误: {str(e)}，请使用正确的Python字典格式")
            
            # 获取协议名称
            message_class = self.proto_mapper.get_client_message(protocol_id)
            if not message_class:
                raise ValueError(f"无效的协议ID: {protocol_id}")
            message_name = message_class.DESCRIPTOR.name
            print("准备创建protobuf消息")
            # 填充消息数据
            message_obj = message_class()
            for field_name, value in message_data.items():
                if hasattr(message_obj, field_name):
                    setattr(message_obj, field_name, value)
                else:
                    raise AttributeError(f"字段 {field_name} 不存在于 {message_class.DESCRIPTOR.name} 协议中")
            
            # 序列化消息
            protobuf_data = self.proto_mapper.serialize_message(message_name,message_obj,is_server=True)
            print("创建protobuf消息成功")
            if protobuf_data:
                self.agent.send_custom_protobuf(protocol_id, protobuf_data)
                self.ui.textBrowser_2.append(
                    f"✅ 成功发送 {message_name} (ID: {protocol_id})\n"
                    f"消息内容: {message_data}"
                )
                
        except Exception as e:
            error_msg = f"❌ 发送失败: {str(e)}\n" \
                       f"请检查：\n" \
                       f"1. 协议ID是否正确\n" \
                       f"2. 消息内容是否为有效的Python字典格式\n" \
                       f"3. 字段名称和类型是否匹配协议定义"
            self.ui.textBrowser_2.append(error_msg)











if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Tool_Panel()
    main.show()
    sys.exit(app.exec_())


