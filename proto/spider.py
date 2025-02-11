from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib.request, urllib.error  # 定制URL，获取网页数据
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文件匹配
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作

# 初始化 Selenium WebDriver
driver = webdriver.Chrome()  # 确保已安装Chrome和对应的ChromeDriver
driver.get("https://kaijiang.78500.cn/p5/")
time.sleep(3)  # 等待页面加载完成

# 解析HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', {'id': 'history-data'})

# 提取数据
data = []
for row in table.find_all('tr')[1:]:  # 跳过表头
    cols = row.find_all('td')
    date = cols[0].get_text()
    numbers = cols[1].get_text()
    data.append([date, numbers])

df = pd.DataFrame(data, columns=["Date", "Winning Numbers"])
df.to_csv('pl5_history.csv', index=False, encoding='utf-8')

print("Data saved to pl5_history.csv")
driver.quit()
