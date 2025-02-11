class XORCipher:
    XOR_KEY: bytes = bytes.fromhex("e07aea3911363aa9")
    
    @staticmethod
    def mod_key(k):
        return XORCipher.XOR_KEY[k]
    
    def __init__(self, key=0xAC):
        self.key = key
        self.orx_key_map = [
            self.mod_key(7), self.mod_key(6), self.mod_key(5), self.mod_key(4),
            self.mod_key(3), self.mod_key(2), self.mod_key(1), self.mod_key(0)
        ]
    
    def encode(self, data):
        if not data:
            return b""
        
        length = len(data)
        mark = length % 10 + 1
        sp_mark = length % 20 if length % 2 != 0 else length // 7
        
        result = bytearray()
        for i in range(length):
            if i % mark != 0:
                if i == sp_mark:
                    asi = data[i] ^ 0xa3
                else:
                    asi = data[i] ^ self.orx_key_map[i % 8]
            else:
                asi = data[i]
            
            result.append(asi)
            
        return bytes(result)

if __name__ == "__main__":
    print(1111111)