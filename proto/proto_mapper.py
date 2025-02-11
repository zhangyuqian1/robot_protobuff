from google.protobuf.descriptor import FieldDescriptor
import importlib
import sys
import os
from protocol_map import protocol_map, PROTOCOL_MAP_C2S
import logging
from typing import Optional, List, Dict, Type, Tuple
from google.protobuf.message import Message
import Xor

# 添加自定义异常类
class ProtocolNotFoundError(Exception):
    """当协议ID未找到时抛出"""

class ParseError(Exception):
    """当消息解析失败时抛出"""

class ProtobufMapper:
    def __init__(self, cipher_cls=Xor.XORCipher):
        """初始化Protobuf映射器"""
        self.server_messages: Dict[str, Type[Message]] = {}  # 服务端消息映射
        self.client_messages: Dict[str, Type[Message]] = {}  # 客户端消息映射
        self.type_map: Dict[int, Type[Message]] = {}        # 类型ID映射
        self.logger = logging.getLogger(__name__)
        self.cipher_cls = cipher_cls

    def load_proto_files(self) -> None:
        """加载所有proto文件"""
        # 加载服务端proto
        for module in self._get_proto_modules("server"):
            self._load_proto_module(module, is_server=True)
            
        # 加载客户端proto
        for module in self._get_proto_modules("client"):
            self._load_proto_module(module, is_server=False)
    
    def _get_proto_modules(self, directory: str) -> List[str]:
        """获取指定目录下的所有proto模块
        
        Args:
            directory: proto文件目录 ("server" 或 "client")
        """
        # 获取当前文件所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        proto_dir = os.path.join(current_dir, directory)
        
        if not os.path.exists(proto_dir):
            self.logger.warning(f"目录不存在: {proto_dir}")
            return []
            
        proto_modules = []
        for root, _, files in os.walk(proto_dir):
            proto_modules.extend(
                os.path.join(os.path.relpath(root, current_dir), file[:-3]).replace(os.sep, '.')
                for file in files if file.endswith('_pb2.py')
            )  
        return proto_modules

    def _load_proto_module(self, module_name: str, is_server: bool = True) -> None:
        """加载单个proto模块
        
        Args:
            module_name: proto模块名称
            is_server: 是否为服务端proto
        """
        try:
            module = importlib.import_module(module_name)
            message_map = self.server_messages if is_server else self.client_messages
            
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if not hasattr(attr, 'DESCRIPTOR'):
                    continue
                    
                if isinstance(attr.DESCRIPTOR, FieldDescriptor):
                    continue
                
                message_name = attr.DESCRIPTOR.name
                message_map[message_name] = attr
                
                # 处理类型ID映射
                self._handle_type_id_mapping(attr)
                    
        except ImportError as e:
            self.logger.error(f"无法导入模块 {module_name}: {e}")
        except Exception as e:
            self.logger.error(f"处理模块 {module_name} 时发生错误: {e}")

    def _handle_type_id_mapping(self, message_class: Type[Message]) -> None:
        """处理消息类的类型ID映射"""
        try:
            if hasattr(message_class.DESCRIPTOR.GetOptions(), 'Extensions'):
                type_id = message_class.DESCRIPTOR.GetOptions().Extensions._FindExtensionByName('type_id')
                if type_id:
                    self.type_map[type_id] = message_class
        except AttributeError:
            pass

    def get_server_message(self, protocol_id: int) -> Optional[Type[Message]]:
        """获取服务端消息类"""
        message_name = protocol_map.get(protocol_id)
        return self.server_messages.get(message_name) if message_name else None

    def get_client_message(self, protocol_id: int) -> Optional[Type[Message]]:
        """获取客户端消息类"""
        message_name = PROTOCOL_MAP_C2S.get(protocol_id)
        return self.client_messages.get(message_name) if message_name else None

    def serialize_message(self, message_name: str, data: Message, is_server: bool = False) -> bytes:
        """将protobuf消息对象序列化为二进制格式"""
        try:
            if not isinstance(data, Message):
                raise ValueError("必须传递protobuf消息对象")
                
            return data.SerializeToString()
        except Exception as e:
            self.logger.error(f"序列化消息失败: {str(e)}")
            raise

    def parse_message(
        self, 
        protocol_id: int, 
        data: bytes, 
        is_server: bool = True
    ) -> Tuple[str, str]:
        """解析二进制数据为protobuf消息
        
        Args:
            protocol_id: 协议ID
            data: 二进制数据
            is_server: True解析服务端消息，False解析客户端消息
            
        Returns:
            tuple: (解析后的消息内容, 消息名称)
            
        Raises:
            ProtocolNotFoundError: 协议ID不存在时
            ParseError: 解析失败时
        """
        message_class = (
            self.get_server_message(protocol_id) 
            if is_server 
            else self.get_client_message(protocol_id)
        )
        
        if not message_class:
            raise ProtocolNotFoundError(
                f"Unknown {'server' if is_server else 'client'} protocol ID: {protocol_id}"
            )
        
        try:
            message = message_class()
            message.ParseFromString(data)
            return self._format_message_str(message), message_class.DESCRIPTOR.name
        except Exception as e:
            self.logger.error(
                "Failed to parse message", 
                extra={"protocol_id": protocol_id, "is_server": is_server}
            )
            raise ParseError(f"Message parsing failed: {e}") from e

    def _format_message_str(self, message: Message) -> str:
        """统一格式化protobuf消息字符串"""
        raw_str = str(message)
        try:
            return raw_str.encode('latin1').decode('unicode_escape').encode('latin1').decode('utf-8')
        except UnicodeDecodeError:
            return raw_str

    def create_client_message(self, protocol_id: int) -> Optional[dict]:
        """根据协议ID创建客户端protobuf消息默认结构
        
        Args:
            protocol_id: 协议ID
            
        Returns:
            dict: 消息默认结构,如果协议ID不存在则返回None
        """
        message_class = self.get_client_message(protocol_id)
        if not message_class:
            return None
        
        # 创建消息实例
        message = message_class()
        
        # 将消息转换为字典结构
        result = {}
        
        # 遍历所有字段
        for field in message.DESCRIPTOR.fields:
            # 根据字段类型设置默认值
            if field.label == field.LABEL_REPEATED:
                result[field.name] = []
            elif field.type == field.TYPE_MESSAGE:
                result[field.name] = {}
            elif field.type in [field.TYPE_INT32, field.TYPE_INT64, 
                              field.TYPE_UINT32, field.TYPE_UINT64]:
                result[field.name] = 0
            elif field.type == field.TYPE_STRING:
                result[field.name] = ""
            elif field.type == field.TYPE_BOOL:
                result[field.name] = False
            elif field.type == field.TYPE_BYTES:
                result[field.name] = b""
            else:
                result[field.name] = None
        
        # 将字典转换为格式化的字符串，每个键值对一行
        formatted_result = "{\n" + ",\n".join([f'    "{k}": {v}' for k, v in result.items()]) + "\n}"
        return formatted_result

    def parse_message_client(self, message_id, content):
        """专门处理客户端协议解析"""
        # 这里可以添加客户端特有的解析逻辑
        return self.parse_message(message_id, content)  # 暂时复用通用解析

    def parse_packet(self, data: bytes, is_server: bool) -> tuple:
        """通用协议包解析"""
        if len(data) < 2:
            return None, None, None
            
        msg_len = int.from_bytes(data[:2], 'big')
        if len(data) < msg_len + 2:
            return None, None, None
            
        encrypted = data[2:2+msg_len]
        cipher = self.cipher_cls()
        decrypted = cipher.encode(encrypted)
        
        protocol_id = int.from_bytes(decrypted[:2], 'big')
        content = decrypted[2:]
        
        try:
            parsed, name = self.parse_message(
                protocol_id,
                content,
                is_server=is_server
            )
            return parsed, name, protocol_id
        except Exception as e:
            # raise ParseError(f"Parse packet failed: {str(e)}")
            print(f"Parse packet failed: {str(e)}")

    def parse_packet_server(self, data: bytes, is_server: bool) -> tuple:
        """通用协议包解析，未解密"""
        if len(data) < 2:
            return None, None, None
            
        msg_len = int.from_bytes(data[:2], 'big')
        if len(data) < msg_len + 2:
            return None, None, None
            
        encrypted = data[2:2+msg_len]
        cipher = self.cipher_cls()
        decrypted = cipher.encode(encrypted)
        
        protocol_id = int.from_bytes(decrypted[:2], 'big')
        content = decrypted[2:]
        
        try:
            parsed, name = self.parse_raw_message(
                protocol_id,
                content,
                is_server=is_server
            )
            return parsed, name, protocol_id
        except Exception as e:
            # raise ParseError(f"Parse packet failed: {str(e)}")
            print(f"Parse packet failed: {str(e)}")

    def parse_raw_message(
        self, 
        protocol_id: int,
        data: bytes,
        is_server: bool = True
    ) -> Tuple[Message, str]:
        """解析二进制数据为原始protobuf消息对象
        
        Args:
            protocol_id: 协议ID
            data: 二进制数据
            is_server: True解析服务端消息，False解析客户端消息
            
        Returns:
            tuple: (protobuf消息对象, 消息名称)
            
        Raises:
            ProtocolNotFoundError: 协议ID不存在时
            ParseError: 解析失败时
        """
        message_class = (
            self.get_server_message(protocol_id) 
            if is_server 
            else self.get_client_message(protocol_id)
        )
        
        if not message_class:
            raise ProtocolNotFoundError(
                f"Unknown {'server' if is_server else 'client'} protocol ID: {protocol_id}"
            )
        
        try:
            message = message_class()
            message.ParseFromString(data)
            return message, message_class.DESCRIPTOR.name  # 直接返回protobuf对象
        except Exception as e:
            self.logger.error(
                "Failed to parse raw message", 
                extra={"protocol_id": protocol_id, "is_server": is_server}
            )
            raise ParseError(f"Raw message parsing failed: {e}") from e

def main():
    logging.basicConfig(level=logging.INFO)
    mapper = ProtobufMapper()
    mapper.load_proto_files()
    
    logging.info("已加载的服务端消息类型: %s", list(mapper.server_messages.keys()))
    logging.info("已加载的客户端消息类型: %s", list(mapper.client_messages.keys()))

if __name__ == "__main__":
    main() 