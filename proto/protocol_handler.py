from google.protobuf import message as pb_message
from proto_mapper import ProtobufMapper
from protocol_map import PROTOCOL_MAP_C2S, protocol_map
from Xor import XORCipher

class ProtocolHandler:
    """协议处理器，处理协议的序列化与反序列化"""
    
    def __init__(self):
        self.proto_mapper = ProtobufMapper(cipher_cls=XORCipher)
        self.cipher = XORCipher()
        self.protocol_handlers = {}
        self._init_protobuf()
        
    def _init_protobuf(self):
        """初始化protobuf相关配置"""
        try:
            self.proto_mapper.load_proto_files()
        except Exception as e:
            print(f"加载proto文件失败: {str(e)}")
            raise
            
    def register_handler(self, proto_id, handler):
        """注册协议处理函数"""
        self.protocol_handlers[proto_id] = handler
        
    def serialize_message(self, protocol_id, data, is_client_proto=True):
        """序列化消息"""
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
            
    def create_packet(self, protocol_id, serialized_data):
        """创建完整数据包"""
        # XOR加密处理
        encrypted = self.cipher.encode(
            protocol_id.to_bytes(2, 'big') + serialized_data
        )
        
        # 构造完整数据包
        return len(encrypted).to_bytes(2, 'big') + encrypted
        
    def parse_packet(self, packet):
        """解析数据包"""
        try:
            parsed, name, pid = self.proto_mapper.parse_packet_server(
                packet, 
                is_server=True
            )
            return parsed, name, pid
        except Exception as e:
            print(f"解析数据包失败: {str(e)}")
            return None, None, None
            
    def dispatch_protocol(self, proto_id, data, proto_name):
        """协议分发"""
        handler = self.protocol_handlers.get(proto_id)
        if handler:
            try:
                print(f"处理协议[{proto_id}]{proto_name}")
                handler(data)
            except Exception as e:
                print(f"处理协议{proto_id}异常: {str(e)}")
        else:
            print(f"未注册的协议处理: [{proto_id}]{proto_name}") 