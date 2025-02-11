-- 设置C语言扩展库的搜索路径
package.cpath = package.cpath .. ";../../build/clualib/?.so"
-- 设置Lua模块搜索路径，包含多个目录
package.path = package.path .. ";../../lualib/base/?.lua;../../cs_common/proto/?.lua;../../skynet/lualib/?.lua;../../skynet/examples/?.lua"..";./?.lua"

-- 引入依赖库
local socket = require "clientsocket"  -- 网络套接字库
local tprint = require('extend').Table.print  -- 表格打印工具
local protobuf = require "protobuf"     -- Google Protocol Buffers
local netdefines = require "netdefines" -- 网络协议定义
local xor = require "xor"               -- 异或加密模块

-- 协议文件路径配置
local sProtoPath = "../../cs_common/proto/proto.pb"
-- 注册协议描述文件
protobuf.register_file(sProtoPath)

-- 调试追踪函数（打印调用栈）
local function Trace(sMsg)
    print(debug.traceback(sMsg))
end

-- 安全调用函数（使用xpcall捕获异常）
function safe_call (func, ...)
    return xpcall(func, Trace, ...)
end

-- 模块定义
local M = {}

-- 全局会话计数器
local g_session = 0
-- 生成新会话ID的函数
local function new_session()
    g_session = g_session + 1
    return g_session
end

-- 递归打印表格结构的函数
function printTable(t)
    for k, v in pairs(t) do
        if type(v) == "table" then
            print(k, "{")     -- 打印表开始
            printTable(v)      -- 递归打印子表
            print(k, "}")      -- 打印表结束
        else
            print(k, v)       -- 打印键值对
        end
    end
end

-- 测试表格数据
local myTable = {
    name = "Kimi", 
    age = 5, 
    details = {
        height = "5ft", 
        weight = "150lbs"
    }
}
-- 执行表格打印测试
printTable(myTable)

--[[ 服务器到客户端协议解包函数
参数s: 二进制数据字符串 ]]
local function s2c_unpack_req(s)
    assert(#s >= 2, "s2c_unpack_req error")  -- 至少包含2字节协议头
    -- 解析协议类型（前两个字节大端序）
    local iType = s:byte(1)*(2^8) + s:byte(2)
    -- 获取协议定义
    local m = netdefines.GS2C[iType]
    assert(m, "s2c_unpack_req error")
    -- 解码protobuf数据（从第3字节开始）
    local args, sErr = protobuf.decode(m[2], string.sub(s, 3))
    printTable(args)  -- 打印解码结果
    assert(args, sErr)
    return m[2], args  -- 返回协议名和参数表
end

--[[ 客户端到服务器协议打包函数
参数name: 协议名称 
   args: 协议参数表
   session: 会话ID ]]
local function c2s_pack_req(name, args, session)
    -- 验证协议名称是否存在
    local iType = netdefines.C2GS_BY_NAME[name]
    assert(iType, "c2s_pack_req error")
    -- 编码protobuf数据
    local sEncode = protobuf.encode(name, args)
    
    -- 构建协议头（2字节大端序）
    local iPow = 8  -- 初始位移量
    local lst = {}
    for i = 1, 2 do
        -- 计算并插入协议类型字节
        table.insert(lst, string.char((iType//(2^iPow))%256))
        iPow = iPow - 8  -- 更新位移量
    end
    -- 合并协议头和内容
    table.insert(lst, sEncode)
    sEncode = table.concat(lst, "")
    return sEncode
end

--[[ 大数据包分片打包函数
参数name: 协议名称
   args: 协议参数
   session: 会话ID ]]
local function c2s_big_pack_req(name, args, session)
    -- 获取协议类型
    local iType = netdefines.C2GS_BY_NAME[name]
    assert(iType, "c2s_big_pack_req error")
    -- 编码完整数据
    local sEncode = protobuf.encode(name, args)

    -- 分片处理参数
    local iLen = #sEncode        -- 数据总长度
    local iSplit = 10*1024       -- 分片大小10KB
    local iStart = 1             -- 起始位置
    local l = {}                 -- 分片存储列表
    local lRet = {}              -- 最终结果列表
    
    -- 分片循环
    while iStart <= iLen do
        local iNext = iStart + iSplit
        -- 截取分片数据
        local s = string.sub(sEncode, iStart, iNext - 1)
        iStart = iNext  -- 更新起始位置
        table.insert(l, s)
    end
    
    -- 构建分片协议包
    for k, v in ipairs(l) do
        table.insert(lRet, c2s_pack_req("C2GSBigPacket", {
            type = iType,   -- 原始协议类型
            total = #l,     -- 总片数
            index = k,      -- 当前片序号
            data = v,       -- 分片数据
        }))
    end
    return lRet
end

-- IP地址正则表达式
local ip_regex = "([0-9]+.[0-9]+.[0-9]+.[0-9]+)"
-- 主机名转IP函数
function host2ip(host)
    -- 直接匹配IP格式
    local ip = string.match(host, ip_regex)
    if ip then
        return ip
    end

    -- 通过系统命令查询DNS
    local tmp_file = os.tmpname()  -- 创建临时文件
    -- 构造host命令
    local cmd = string.format('host -4 %s|egrep -o "%s" > %s', host, ip_regex, tmp_file)
    os.execute(cmd)  -- 执行命令
    
    -- 读取结果
    local fp = io.open(tmp_file)
    local ip = fp:read("*a")
    fp:close()
    os.remove(tmp_file)  -- 清理临时文件

    -- 处理查询结果
    if #ip <= 0 then
        return nil
    end
    local ip = string.sub(ip, 1, #ip - 1)  -- 去除末尾换行符
    print("host to ip suc:", host, ip)
    return ip
end

-- 机器人类定义
local Robot = {}

-- 构造函数
function Robot:new(host, port, opts)
    local opts = opts or {}  -- 默认参数
    -- 初始化对象属性
    local obj = {
        host = host,          -- 服务器地址
        port = port,          -- 服务器端口
        fd = assert(socket.connect(host, port)),  -- 网络连接描述符
        last = "",            -- 未处理完的残留数据
        slient = opts.slient, -- 静默模式标志
        shield = opts.shield or {},  -- 协议屏蔽列表
        coroutines = {},      -- 协程列表
        timers = {},          -- 定时器列表
        callers = {},         -- 调用者列表
        server_request_handlers = {},  -- 服务器请求处理器
        running = true,       -- 运行状态标志
        bigpacket_cache = {},  -- 大数据包缓存
    }
    -- 设置元表
    setmetatable(obj, {__index = Robot})
    return obj
end

-- 创建协程方法
function Robot:fork(func, ...)
    local args = {...}  -- 获取可变参数
    -- 创建安全协程
    local func_co = coroutine.create(
        function()
            safe_call(func, table.unpack(args))  -- 安全执行
        end
    )
    table.insert(self.coroutines, func_co)  -- 加入协程列表
end

-- 协程休眠方法
function Robot:sleep(n)
    -- 创建等待器对象
    local waiter = {
        co = coroutine.running(),  -- 当前协程
        done = false,              -- 完成标志
        time = os.time() + n,      -- 唤醒时间戳
    }
    -- 加入定时器队列
    table.insert(self.timers, waiter)
    -- 挂起协程直到唤醒
    while true do
        if waiter.done then
            break
        end
        coroutine.yield()
    end
end

-- 协议字段掩码方法
function Robot:mask(sMessage, mData)
    assert(not mData.mask, "Mask fail should has no mask field")
    -- 获取协议字段编号映射
    local m = protobuf["name_fields"](sMessage)
    assert(m.mask == 1, "Mask fail mask field should be id 1")
    
    local mRet = {}  -- 返回结果
    local mMod = {}  -- 掩码计算临时存储
    local iMax = 0   -- 最大字段组号
    
    -- 遍历数据字段
    for k, v in pairs(mData) do
        local iNo = assert(m[k], string.format("Mask fail %s error", k))
        -- 计算字段组和位偏移
        local iMod, iRet = (iNo-1)//4, iNo%4
        local iMask = mMod[iMod] or 0
        
        mRet[k] = v  -- 保留原始值
        
        -- 设置掩码位
        if iRet > 0 then
            iMask = iMask | (2^(iRet-1))
        else
            iMask = iMask | (2^3)  -- 处理余数为0的情况
        end
        mMod[iMod] = iMask
        iMax = math.max(iMod, iMax)  -- 更新最大组号
    end
    
    -- 生成掩码字符串
    local sMask = ""
    for i = iMax, 0, -1 do
        sMask = sMask .. string.format("%x", mMod[i] or 0)
    end
    mRet.mask = sMask
    return mRet
end

-- 协议字段解掩码方法
function Robot:unmask(sMessage, mData)
    if not mData.mask then
        mData.mask = ""  -- 默认空掩码
    end
    -- 获取协议字段名称映射
    local m = protobuf["id_fields"](sMessage)
    assert(m[1] == "mask", "Mask fail mask field should be id 1")
    
    local sMask = mData.mask
    local iLen = #sMask
    local mRet = {}  -- 返回结果
    
    -- 解析掩码字符串
    for i = 1, iLen do
        local iByte = tonumber(string.char(sMask:byte(i)), 16)
        -- 处理每个字节的4个位
        for j = 1, 4 do
            local k = (iLen - i) * 4 + j  -- 计算字段编号
            if k == 1 then
                goto continue  -- 跳过掩码字段本身
            end
            -- 检查位是否设置
            local b = (2 ^ (j - 1)) & iByte
            if b~=0 then
                local sKey = assert(m[k], string.format("UnMask fail %s error", k))
                mRet[sKey] = mData[sKey]  -- 保留有效字段
            end
            ::continue::
        end
    end
    return mRet
end

-- 发送普通请求方法
function Robot:send_client_request(name, args, session)
    -- 非静默模式且未屏蔽的协议打印日志
    if not self.slient and not self.shield[name] then
        print("[REQUEST]", name, session)
        if args then
            tprint(args)  -- 打印参数详情
        end
        print()
    end
    -- 打包协议数据
    local s = c2s_pack_req(name, args, session)
    s= xor.code(s)  -- 异或加密
    -- 发送数据（大端序2字节长度头）
    socket.send(self.fd, string.pack(">s2", s))
end

-- 发送大数据请求方法
function Robot:send_big_client_request(name, args, session)
    -- 日志打印（同普通请求）
    if not self.slient and not self.shield[name] then
        print("[REQUEST]", name, session)
        if args then
            tprint(args)
        end
        print()
    end
    -- 分片打包
    local l = c2s_big_pack_req(name, args, session)
    -- 逐片发送
    for _, v in ipairs(l) do
        v= xor.code(v)  -- 异或加密
        socket.send(self.fd, string.pack(">s2", v))
    end
end

-- 处理服务器请求方法
function Robot:handle_server_request(name, args)
    local bFlag = true  -- 是否立即处理标志
    
    -- 大数据包特殊处理
    if name == "GS2CBigPacket" then
        bFlag = false
        local ty = args.type     -- 原始协议类型
        local total = args.total -- 总片数
        local index = args.index -- 当前片序号
        local d = args.data      -- 分片数据
        
        -- 首片初始化缓存
        if index == 1 then
            self.bigpacket_cache[ty] = nil
        end
        -- 创建分片缓存
        if not self.bigpacket_cache[ty] then
            self.bigpacket_cache[ty] = {}
        end
        -- 存入分片数据
        table.insert(self.bigpacket_cache[ty], d)
        local l = self.bigpacket_cache[ty]
        
        -- 检查序号连续性
        if #l ~= index then
            self.bigpacket_cache[ty] = nil
            assert(false, "handle_server_request index error")
        else
            -- 收到最后一片时处理
            if index == total then
                bFlag = true
                self.bigpacket_cache[ty] = nil
                -- 合并数据
                local sd = table.concat(l, "")
                -- 解码原始协议
                local m = netdefines.GS2C[ty]
                assert(m, "handle_server_request error")
                local nargs, sErr = protobuf.decode(m[2], sd)
                assert(nargs, sErr)
                name = m[2]   -- 更新协议名
                args = nargs  -- 更新参数
            end
        end
    end

    -- 需要立即处理的协议
    if bFlag then
        -- 打印协议日志
        if not self.slient and not self.shield[name] then
            print("[NOTIFY]", name)
            if args then
                tprint(args)
            end
        end

        -- 合并包处理
        if name == "GS2CMergePacket" then
            local lPackets = args.packets
            -- 创建协程处理子包
            self:fork(function ()
                for _,sPacket in pairs(lPackets) do
                    local name, args = s2c_unpack_req(sPacket)
                    self:handle_server_request(name, args)
                end
            end)
        else
            -- 查找注册的处理器
            local func = self.server_request_handlers[name]
            if func then
                self:fork(func, self, args)
            end
            -- 登录成功后启动心跳协程
            if name == "GS2CLoginRole" then
                self:fork(function ()
                    while 1 do
                        self:sleep(10)  -- 每10秒心跳
                        self:run_cmd("C2GSHeartBeat", {})
                    end
                end)
            end
        end
    end
end

-- 解包网络数据方法
function Robot:unpack_package(text)
    local size = #text
    if size < 2 then
        return nil, text  -- 数据不足
    end
    -- 读取大端序长度头
    local s = text:byte(1) * 256 + text:byte(2)
    if size < s+2 then
        return nil, text  -- 数据不完整
    end
    -- 返回有效数据和剩余数据
    return text:sub(3,2+s), text:sub(3+s)
end

-- 接收完整数据包方法
function Robot:recv_package(lfd)
    -- 尝试从缓存解析完整包
    local result
    result, self.last = self:unpack_package(self.last)
    if result then 
        return result
    end
    -- 接收新数据
    local r = socket.recv(lfd)
    if not r then
        return nil
    end
    if r == "" then
        error "Server closed"  -- 连接关闭
    end
    -- 合并数据并再次尝试解析
    result, self.last = self:unpack_package(self.last .. r)
    return result
end

-- 解析控制台输入命令
function Robot:parse_cmd(s)
    if s == "" or s == nil then
        return false
    end

    local cmd = ""
    local args_data = nil
    -- 分割命令和参数
    local b, e = string.find(s, " ")
    if b then
        cmd = s:sub(0, b - 1)
        args_data = s:sub(e + 1)
    else
        cmd = s
    end

    -- 处理脚本命令
    if cmd == "script" then
        if not args_data then
            print("illegal cmd", s)
            return false
        end
        return true, cmd, args_data
    end

    -- 解析参数为Lua表
    local args
    if args_data then
        local f, err = load("return " .. args_data)
        if f == nil then
            print("illegal cmd", s)
            return false
        end

        local ok, _args = pcall(f)
        if (not ok) or (type(_args) ~= 'table') then
            print("illegal cmd", s)
            return false
        end
        args = _args
    end

    return true, cmd, args
end

-- 执行控制台命令
function Robot:run_cmd(cmd, args)
    -- 打印命令日志
    if not self.slient and not self.shield[cmd] then
        print('[COMMAND]', cmd, args)
    end
    local session = new_session()  -- 生成新会话ID
    local ok, err
    -- 判断是否为大数据命令
    if string.sub(cmd, 1, 3) == "big" then
        ok, err = pcall(self.send_big_client_request, self, string.sub(cmd, 5), args, session)
    else
        ok, err = pcall(self.send_client_request, self, cmd, args, session)
    end
    -- 错误处理
    if not ok then
        print('run cmd fail', cmd, args, err)
        return false
    end
end

-- 执行Lua脚本文件
function Robot:run_script(script)
    -- 打印脚本日志
    if not self.slient then
        print('[script]', script)
    end
    -- 创建独立环境
    local env = setmetatable(
        {
            client = self,  -- 暴露client对象
        },
        {__index = _ENV}    -- 继承全局环境
    )

    -- 加载脚本文件
    local func, err = loadfile(script, "bt", env)
    if not func then
        print('load script fail, err', err)
        return
    end
    -- 安全执行脚本
    safe_call(func)
end

-- 检查网络数据包
function Robot:check_net_package()
    while true do
        local v = self:recv_package(self.fd)  -- 接收数据包
        if not v then
            return
        end
        v=xor.code(v)  -- 异或解密
        local name, args = s2c_unpack_req(v)  -- 解包协议
        self:handle_server_request(name, args)  -- 处理协议
    end
end

-- 检查控制台输入
function Robot:check_console()
    local s = socket.readstdin()  -- 读取标准输入
    if s == "quit" then
        self.running = false  -- 退出指令
        return
    end

    -- 快捷指令处理
    if s == "." then
        s = [[C2GSGMCmd {cmd="runtest"}]]
    end
    if (s ~= nil and s ~= "") then
        -- 解析并执行命令
        local ok, cmd, args = self:parse_cmd(s)
        if ok then
            if cmd == "script" then
                self:fork(self.run_script, self, args)
            else
                self:fork(self.run_cmd, self, cmd, args)
            end
        end
    end
end

-- 主IO检查循环
function Robot:check_io()
    local ok, err = pcall(
        function()
            while self.running do
                self:check_net_package()  -- 处理网络数据
                self:check_console()     -- 处理控制台输入
                coroutine.yield()         -- 让出执行权
            end
        end
    )
    -- 异常处理
    if not ok then
        print("[ERROR]:", err)
        self.running = false
    end
end

-- 启动机器人主循环
function Robot:start()
    self:fork(self.check_io, self)  -- 启动IO协程
    while self.running do
        -- 协程状态维护
        local co_list = {}    -- 有效协程列表
        local removed = {}    -- 待移除协程标记
        
        -- 第一遍遍历：标记死亡协程
        for idx, co in ipairs(self.coroutines) do
            if coroutine.status(co) == "dead" then
                removed[co] = true
            else
                table.insert(co_list, co)                    
            end
        end

        -- 第二遍遍历：恢复协程执行
        for _, co in ipairs(co_list) do
            if coroutine.status(co) ~= "dead" then
                coroutine.resume(co)
            end
        end

        -- 第三遍遍历：清理死亡协程
        for co, v in pairs(removed) do
            local target_idx
            for idx, co2 in ipairs(self.coroutines) do
                if co == co2 then
                    target_idx = idx
                    break
                end
            end
            if target_idx then
                table.remove(self.coroutines, target_idx)
            end
        end

        -- 定时器处理
        local awake_list = {}  -- 需要唤醒的定时器
        local t_now = os.time()
        -- 倒序遍历定时器
        for idx=#self.timers, 1, -1 do
            local item = self.timers[idx]
            if coroutine.status(item.co) == "dead" then
                table.remove(self.timers, idx)
            elseif item.time <= t_now then
                table.remove(self.timers, idx)
                table.insert(awake_list, item)
            end
        end

        -- 唤醒到期定时器
        for _, waiter in ipairs(awake_list) do
            if coroutine.status(waiter.co) ~= "dead" then
                waiter.done = true
                coroutine.resume(waiter.co)
            end
        end

        coroutine.yield()  -- 让出CPU
    end
end

-- 停止机器人运行
function Robot:stop()
    self.running = false
end

-- 模块导出
return {
    Robot = Robot,
    host2ip = host2ip,
}