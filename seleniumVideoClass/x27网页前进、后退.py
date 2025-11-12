# 网页前进、后退

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
a1.get('https://www.baidu.com/')
a1.find_element(By.XPATH, '//*[@id="kw"]').send_keys('dafait')
time.sleep(2)
a1.find_element(By.XPATH, '//*[@id="su"]').click()
time.sleep(2)
# 网页后退
a1.back()
time.sleep(2)
# 网页前进
a1.forward()
