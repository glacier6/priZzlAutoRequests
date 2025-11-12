# 警告框(alert)元素交互
# 演示地址：https://sahitest.com/demo/alertTest.htm
# 获取弹窗内的文本内容
# 点击弹窗确定按钮

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
a1.get('https://sahitest.com/demo/alertTest.htm')
a1.find_element(By.XPATH, '/html/body/form/input[1]').clear()
time.sleep(1)
a1.find_element(By.XPATH, '/html/body/form/input[1]').send_keys('大发程序员')
time.sleep(1)
a1.find_element(By.XPATH, '/html/body/form/input[3]').click()
time.sleep(3)
# 获取弹窗内的文本内容
print(a1.switch_to.alert.text)
# 点击弹窗确定按钮
a1.switch_to.alert.accept()


