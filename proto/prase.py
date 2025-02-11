import login_pb2
import Xor  # 导入自定义的XOR加密模块

# 创建加密对象并设置加密数据
cipher = Xor.XORCipher() # 创建XOR加密器实例
encrypted_data = b'\x00\x08\x03J>\xc8\xfc\x7f\xc6\xe6' # 原始的加密二进制数据

# 解析消息长度和内容
message_length = int.from_bytes(encrypted_data[:2], byteorder='big') # 从前2个字节解析出消息长度
message_content = encrypted_data[2:] # 获取消息长度之后的实际消息内容

# 解密并解析消息
decrypted_data = cipher.encode(message_content) # 使用XOR解密消息内容
message_id = int.from_bytes(decrypted_data[:2], byteorder='big') # 从解密后的数据中获取消息ID
actual_content = decrypted_data[2:] # 获取消息ID之后的实际消息内容

# 使用protobuf解析消息
login_message = login_pb2.GS2CHello() # 创建protobuf消息对象
login_message.ParseFromString(actual_content) # 将二进制数据解析为protobuf消息
print(f"解析后的消息: {login_message}") # 打印解析后的消息内容