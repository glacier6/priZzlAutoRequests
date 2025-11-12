# 元素定位-PARTIAL_LINK_TEXT

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
# 元素定位-PARTIAL_LINK_TEXT
# 通过模糊链接文本找到标签a的元素[模糊文本定位]
# 有重复的文本，需要切片
a1.find_elements(By.PARTIAL_LINK_TEXT, '3')[1].click()






