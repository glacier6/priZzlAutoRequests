# 浏览器最大化 maximize_window()
# 浏览器最小化 minimize_window()

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
time.sleep(2)
# 浏览器最大化
a1.maximize_window()
time.sleep(2)
# 浏览器最小化
a1.minimize_window()
time.sleep(2)
a1.maximize_window()
