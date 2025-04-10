from locust import HttpUser, TaskSet, task, between
import random
import logging

class UserBehavior(TaskSet):
    # 搜索关键词列表
    search_keywords = [
        "Python",
        "性能测试",
        "Locust教程",
        "软件测试",
        "自动化测试"
    ]

    def on_start(self):
        """每个用户开始时执行"""
        logging.info("用户行为开始")

    @task(3)  # 权重为3，表示执行概率更高
    def baidu_home(self):
        """访问百度首页"""
        with self.client.get("/", 
                           verify=False,
                           catch_response=True) as response:
            if response.status_code == 200:
                if "百度一下" in response.text:
                    response.success()
                    logging.info("首页访问成功")
                else:
                    response.failure("首页内容校验失败")
            else:
                response.failure(f"首页访问失败: {response.status_code}")

    @task(2)  # 权重为2
    def baidu_search(self):
        """百度搜索"""
        # 随机选择一个关键词
        keyword = random.choice(self.search_keywords)
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        }
        
        params = {
            "wd": keyword,
            "ie": "utf-8"
        }
        
        with self.client.get("/s", 
                           params=params, 
                           headers=headers, 
                           verify=False,
                           catch_response=True,
                           name=f"/s?wd={keyword}") as response:
            if response.status_code == 200:
                if keyword in response.text:
                    response.success()
                    logging.info(f"搜索 '{keyword}' 成功")
                else:
                    response.failure(f"搜索结果中未找到关键词: {keyword}")
            else:
                response.failure(f"搜索请求失败: {response.status_code}")

    @task(1)  # 权重为1，执行概率最低
    def baidu_image(self):
        """访问百度图片"""
        with self.client.get("/image", 
                           verify=False,
                           catch_response=True) as response:
            if response.status_code == 200:
                response.success()
                logging.info("图片页面访问成功")
            else:
                response.failure(f"图片页面访问失败: {response.status_code}")

class BaiduUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(3, 5)  # 思考时间3-5秒
    
    def on_start(self):
        """用户启动时执行"""
        logging.info("用户开始运行")
    
    def on_stop(self):
        """用户停止时执行"""
        logging.info("用户停止运行")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
