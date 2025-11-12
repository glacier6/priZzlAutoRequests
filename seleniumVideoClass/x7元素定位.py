# 定位一个元素
# 定位多个元素
# 浏览器查找多个元素：document.getElementById('元素值')
# 元素定位导包：from selenium.webdriver.common.by import By

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
# 定位一个元素(找到的话返回结果，找不到的话报错)
# a2 = a1.find_element(By.ID, 'kw1')
# 定位多个元素(找到的话返回列表形式，找不到的话返回空列表)
a2 = a1.find_elements(By.ID, 'kw')
print(a2)









