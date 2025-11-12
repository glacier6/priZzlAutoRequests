# 多线程执行自动化(四开浏览器)
# 导包：import threading
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading


class A1:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 设置浏览器、启动浏览器
    def she(self):
        q1 = Options()
        q1.add_argument("--no-sandbox")
        q1.add_experimental_option("detach", True)
        a1 = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=q1)
        a1.set_window_position(self.x, self.y)
        a1.set_window_size(200, 400)
        a1.implicitly_wait(30)
        a1.get('https://bahuyun.com/bdp/form/1327923698319491072')
        return a1

    # 执行代码
    def zhi(self):
        a1 = self.she()
        for x in range(3):
            time.sleep(2)
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[2]/div/div[2]/div/div/div[3]').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[1]').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[2]').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[3]/div/div[2]/div/div/div[3]').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[4]/div/div[2]/div/div/div/select/option[2]').click()
            a1.find_element(By.XPATH, '//*[@id="input-cG2LA_WGt0D0ic623V7ua"]').send_keys('0020251212')
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[6]/div/div[2]/div/div[1]/div[2]/div[5]/i').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[6]/div/div[2]/div/div[2]/div[2]/div[5]/i').click()
            a1.find_element(By.XPATH, '//*[@id="my-node"]/div[7]/div/div[2]/div/div/div/div/div/input').send_keys(
                r'D:\xue1\Selenium\logo2.png')

            time.sleep(2)
            a1.find_element(By.XPATH, '//*[@id="submit-button"]').click()
            time.sleep(2)
            a1.find_element(By.XPATH, '//*[@id="app"]/div/div/div[1]/div[2]/div[3]/button').click()

            time.sleep(2)
            a2 = a1.window_handles
            a1.close()
            a1.switch_to.window(a2[1])


s1 = A1(0, 0)
s2 = A1(800, 0)
s3 = A1(0, 500)
s4 = A1(800, 500)

threading.Thread(target=s1.zhi).start()
threading.Thread(target=s2.zhi).start()
threading.Thread(target=s3.zhi).start()
threading.Thread(target=s4.zhi).start()
