class ProtocolMap:
    """静态协议映射，所有实例共享"""
    
    # 只定义实际使用的30个协议，减少内存占用
    # 使用静态字典，避免对象创建开销
    _ID_TO_NAME = {
        # 登录相关
        1001: "C2GSLoginAccount",
        1002: "C2GSLoginRole",
        1003: "C2GSCreateRole",
        1008: "C2GSQueryLogin",
        
        # 场景相关
        2005: "C2GSSyncPosQueue",
        2014: "C2GSEnterScene",
        
        # 系统相关
        3001: "C2GSHeartBeat",
        
        # 其他必要协议...
        # (只添加真正需要的协议，而不是全部)
    }
    
    # 预计算反向映射，避免运行时计算
    _NAME_TO_ID = {name: pid for pid, name in _ID_TO_NAME.items()}
    
    @staticmethod
    def get_name(protocol_id):
        """通过ID获取名称，直接返回，无需实例化"""
        return ProtocolMap._ID_TO_NAME.get(protocol_id)
    
    @staticmethod
    def get_id(name):
        """通过名称获取ID，直接返回，无需实例化"""
        return ProtocolMap._NAME_TO_ID.get(name)