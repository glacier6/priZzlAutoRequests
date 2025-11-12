# 元素定位-CSS_SELECTOR

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
# 元素定位-CSS_SELECTOR
# 1，#id = 井号+id值 通过id定位
# 2，.class = 点+class值 通过class定位
# 3，不加修饰符  = 标签头  通过标签头定位
# 4，通过任意类型定位："[类型='精准值']"
# 5，通过任意类型定位："[类型*='模糊值']"
# 6，通过任意类型定位："[类型^='开头值']"
# 7，通过任意类型定位："[类型$'结尾值']"
# 以上这些方法都属于理论定位法

# 8，更简单的定位方式：在谷歌控制台直接复制  SELECTOR  (各别元素定位值会比较长)

a1.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(5)").click()






