import configparser
from datetime import datetime
import os

def generate_hourly_accounts():
    """生成基于当前小时+序号的1000个账号到conf/account.ini"""
    # 创建conf目录（如果不存在）
    os.makedirs('conf', exist_ok=True)
    
    # 获取当前时间并格式化为年月日小时
    time_str = datetime.now().strftime("%Y%m%d%H")
    
    # 生成账号列表
    accounts = [f"{time_str}{i:04d}" for i in range(1, 1001)]
    
    # 创建配置解析器
    config = configparser.ConfigParser()
    config['Accounts'] = {}
    
    # 填充账号数据
    for idx, account in enumerate(accounts, 1):
        config['Accounts'][f'account{idx}'] = account
    
    # 构建文件路径
    file_path = os.path.join('conf', 'account.ini')
    
    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        config.write(f)
    
    print(f"已生成 {len(accounts)} 个账号到 {file_path}")
    print(f"时间基准: {time_str}0001 - {time_str}1000")

if __name__ == "__main__":
    # 构建完整文件路径
    file_path = os.path.join('conf', 'account.ini')
    
    # 检查文件是否存在
    if os.path.exists(file_path):
        confirm = input(f"检测到已存在 {file_path} 文件，是否覆盖？(y/n): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            exit()
    
    # 执行生成
    try:
        generate_hourly_accounts()
    except Exception as e:
        print(f"生成账号失败: {str(e)}")
        if not os.path.exists('conf'):
            print("提示: conf目录创建失败，请检查写入权限")
