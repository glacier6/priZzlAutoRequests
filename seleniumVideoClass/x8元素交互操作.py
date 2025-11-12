# 元素交互操作
# 元素点击
# 元素输入
# 元素清空

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# 设置浏览器、启动浏览器
def she():
    q1 = Options()
    q1.add_argument("--no-sandbox")
    q1.add_experimental_option("detach", True)
    a1 = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=q1)
    return a1


a1 = she()
a1.get('https://baidu.com')
a2 = a1.find_element(By.ID, 'kw')
# 元素输入
a2.send_keys('dafait')
time.sleep(2)
# 元素清空
a2.clear()
time.sleep(2)
# 元素输入
a2.send_keys('dafait')
time.sleep(2)
a2 = a1.find_element(By.ID, 'su')
# 元素点击
a2.click()









