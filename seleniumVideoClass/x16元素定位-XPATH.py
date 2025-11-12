# 元素定位-XPATH

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
# 元素定位-XPATH
# 1, 复制谷歌浏览器 Xpath (通过属性+路径定位, 属性如果是随机的，可能定位不到)
# 2, 复制谷歌浏览器 Xpath 完整路径 (缺点是定位值 比较长，优点是基本100%准确)
a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').click()






