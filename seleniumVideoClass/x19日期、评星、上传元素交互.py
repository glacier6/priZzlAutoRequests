# 日期、评星、上传元素交互

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
a1.get('https://bahuyun.com/bdp/form/1327923698319491072')
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[2]/div/div[2]/div/div/div[3]').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[1]').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[2]').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[3]').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[4]/div/div[2]/div/div/div/select/option[2]').click()
a1.find_element(By.XPATH, '//*[@id="input-cG2LA_WGt0D0ic623V7ua"]').send_keys('0020251212')
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[6]/div/div[2]/div/div[1]/div[2]/div[5]/i').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[6]/div/div[2]/div/div[2]/div[2]/div[5]/i').click()
a1.find_element(By.XPATH, '//*[@id="my-node"]/div[7]/div/div[2]/div/div/div/div/div/input').send_keys(r'D:\xue1\Selenium\logo2.png')






