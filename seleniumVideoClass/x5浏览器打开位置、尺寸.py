# 浏览器打开位置
# 浏览器打开尺寸

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
# 浏览器打开位置
a1.set_window_position(0, 0)
# 浏览器打开尺寸
a1.set_window_size(600, 600)
