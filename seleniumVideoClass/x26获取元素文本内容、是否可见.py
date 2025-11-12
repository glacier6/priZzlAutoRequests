# 获取元素文本内容、是否可见
# 演示地址：https://baijiahao.baidu.com/s?id=1814969914411764219

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
    a1.implicitly_wait(3)
    return a1


a1 = she()
a1.get('https://baijiahao.baidu.com/s?id=1814969914411764219')
# 获取元素文本内容 text
a2 = a1.find_element(By.XPATH, '//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/p').text
print(a2)
# 元素是否可见 is_displayed()
a3 = a1.find_element(By.XPATH, '//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/p').is_displayed()
print(a3)


