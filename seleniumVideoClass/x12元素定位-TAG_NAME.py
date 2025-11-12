# 元素定位-TAG_NAME

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
a1.get('https://www.baidu.com/')
# 元素定位-TAG_NAME
# 1, 查找<开头标签名字>
# 2, 重复的标签名字特别多，需要切片
a1.find_elements(By.TAG_NAME, 'a')[3].click()






