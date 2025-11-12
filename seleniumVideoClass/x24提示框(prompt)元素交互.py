# 提示框(prompt)元素交互
# 演示地址：https://sahitest.com/demo/promptTest.htm
# 弹窗输入内容

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
    a1.implicitly_wait(30)
    return a1


a1 = she()
a1.get('https://sahitest.com/demo/promptTest.htm')
a1.find_element(By.XPATH, '/html/body/form/input[1]').click()
time.sleep(2)
# 弹窗输入内容
a1.switch_to.alert.send_keys('大发程序员')
time.sleep(2)
# 弹窗点击确定
a1.switch_to.alert.accept()

