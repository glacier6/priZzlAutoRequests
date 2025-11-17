
# .\venv\Scripts\Activate.ps1
from selenium import webdriver # 用于操作浏览器
from selenium.webdriver.chrome.options import Options # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
from CommonFunc import connectOneChrom,creatOneMyChrom,creatOneNomalChrom,RunCase,is_port_listening,Person
from selenium.webdriver.support import expected_conditions as EC  # 导入等待条件
from selenium.webdriver.support.ui import WebDriverWait
import time
import threading

# openUrl = r'file:///C:/Users/11367/Desktop/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BD%AF%E4%BB%B6/priZzlAutoRequests/%E6%B5%8B%E8%AF%95%E7%95%8C%E9%9D%A2/%E9%A2%84%E7%BA%A6%E6%B5%8B%E8%AF%95/%E7%BA%AA%E5%BF%B5%E5%B8%81%E9%A2%84%E7%BA%A6%E5%B7%A5%E5%95%86.html'
openUrl = r'https://static.jnb.icbc.com.cn/ICBC/ICBCCOIN/roccentryPC.html'
# openUrl = r'https://element.eleme.cn/#/zh-CN/component/select'


# 注意这个里面不会默认有self（就算是加给了某个对象）
def coinsRunFunc(person, port=7360, positionX=0, positionY=0, maxWaitTime=120):
    if is_port_listening(port):
        nowDriver = connectOneChrom(port)
    else:
        oneRunCase = RunCase(port=port, positionX=positionX, positionY=positionY, openUrl=openUrl, maxWaitTime=maxWaitTime)
        nowDriver = oneRunCase.driver
    print(nowDriver.title)
    # NOTE:下面就可以写操作了
    # 1.等待进入（同步北京时间 或 轮询页面）
    goBookBtn = nowDriver.find_element(By.ID, 'goBooking') # 或者用完整XPATH /html/body/div[1]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[4]/div/div
    goBookBtn.click() # 这个会自动阻塞！！

    # 2.填入信息
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请输入客户")]').send_keys(person.name)
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请输入证件")]').send_keys(person.IDCard)
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "手机号码")]').send_keys(person.phone)
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "预约数量")]').send_keys(person.appointmentNum)

    if nowDriver.find_element(By.XPATH, '//li[contains(., "按关键字查询")]').is_displayed():
        nowDriver.find_element(By.XPATH, '//li[contains(., "按关键字查询")]').click()

    # 请选择省份
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请选择省份")]').click()
    nowDriver.find_element(By.XPATH, f'//li/span[text()="{person.province}"]').click()
    
    # 请选择城市
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请选择城市")]').click()
    nowDriver.find_element(By.XPATH, f'//li/span[text()="{person.city}"]').click()

    # 请选择区县
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请选择区县")]').click()
    nowDriver.find_element(By.XPATH, f'//li/span[text()="{person.county}"]').click()

    # 请选择网点
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请选择网点")]').click()
    nowDriver.find_element(By.XPATH, f'//li[contains(., "{person.hall}")]').click()

    # 3.确认预约
    # el-checkbox__input
    nowDriver.find_element(By.XPATH, "//span[@class='el-checkbox__input']").click() # 同意服务须知

    # 4.弹框点击获取验证码

    # 5.自动判断短信验证码
    # 请输入短信验证码

if __name__ == "__main__":
    person1 = Person(name='渣渣辉',IDCard='425684198805468216',phone='11263956658',province='1',city='2',county='3',hall='4')
    person2 = Person(name='渣渣辉',IDCard='425684198805468216',phone='11263956658',province='1',city='2',county='3',hall='4')
    person3 = Person(name='渣渣辉',IDCard='425684198805468216',phone='11263956658',province='1',city='2',county='3',hall='4')
    person4 = Person(name='渣渣辉',IDCard='425684198805468216',phone='11263956658',province='1',city='2',county='3',hall='4')
    threading.Thread(target=coinsRunFunc, args=(person1,7360,0,0), name="Thread-7360").start()
    threading.Thread(target=coinsRunFunc, args=(person2,7361,600,0), name="Thread-7361").start()
    threading.Thread(target=coinsRunFunc, args=(person3,7362,1200,0), name="Thread-7362").start()
    threading.Thread(target=coinsRunFunc, args=(person4,7363,1800,0), name="Thread-7363").start()
