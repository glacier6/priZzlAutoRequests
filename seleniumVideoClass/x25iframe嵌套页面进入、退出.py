# iframe嵌套页面进入、退出
# 演示地址：https://sahitest.com/demo/iframesTest.htm

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
a1.get('https://sahitest.com/demo/iframesTest.htm')

# 获取iframe元素
a2 = a1.find_element(By.XPATH, '/html/body/iframe')
# 进入iframe嵌套页面
a1.switch_to.frame(a2)
time.sleep(2)
# 进入iframe页面操作元素点击
a1.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click()
# 退出iframe嵌套页面(返回到默认页面)
a1.switch_to.default_content()
time.sleep(2)
a1.find_element(By.XPATH, '/html/body/input[2]').click()
