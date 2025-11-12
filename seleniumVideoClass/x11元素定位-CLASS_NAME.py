# 元素定位-CLASS_NAME

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
a1.get('https://www.bilibili.com/')
# 元素定位-CLASS_NAME
# 1, class值不能有空格，否则报错
# 2, class值重复的有很多，需要切片
# 3, class值有的网站是随机的
a1.find_elements(By.CLASS_NAME, 'channel-link')[1].click()








