# 元素定位-ID

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
# 元素定位-ID
# 1, 通过ID定位元素，一般比较准确。
# 2, 并不是所有网页或者元素 都有ID值
a1.find_element(By.ID, 'kw').send_keys('dafait')







