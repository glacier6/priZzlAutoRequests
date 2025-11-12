# 元素定位隐性等待
# 演示地址：https://bahuyun.com/bdp/form/1327923698319491072

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
a1.get('https://bahuyun.com/bdp/form/1327923698319491072')
# 元素定位隐性等待(多少秒内找到元素就立刻执行，没找到元素就报错)
a1.implicitly_wait(30)
a1.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[1]/div[1]/i').click()






