
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

# NOTE:下面的是按照直接选网点操作的，推荐用这个，已经过测试！

# openUrl = r'file:///C:/Users/11367/Desktop/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BD%AF%E4%BB%B6/priZzlAutoRequests/%E6%B5%8B%E8%AF%95%E7%95%8C%E9%9D%A2/%E9%A2%84%E7%BA%A6%E6%B5%8B%E8%AF%95/%E7%BA%AA%E5%BF%B5%E5%B8%81%E9%A2%84%E7%BA%A6%E5%B7%A5%E5%95%86.html'
openUrl = r'https://static.jnb.icbc.com.cn/ICBC/ICBCCOIN/roccentryPC.html'
# openUrl = r'https://element.eleme.cn/#/zh-CN/component/select'

# 注意要操作的元素必须在界面上，需要滚动才显示的不会点击到！！所以最好缩小到50%（或者更低）
# 而且有些点击的元素他不能立马再去操作（如下拉列表），因为如下拉会有消失时间，可能会有层级问题，所以在下面加了个0.1的等待时间
# 注意这个里面不会默认有self（就算是加给了某个对象）
def coinsRunFunc(person, port=7360, positionX=0, positionY=0, maxWaitTime=180):
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

    # 同意服务须知 OK
    nowDriver.find_element(By.XPATH, "//label[@class='el-checkbox']/span").click()

    try:
        # 2. 临时设置隐式等待为 0 秒（非阻塞：找不到元素立即返回，不等待）
        nowDriver.implicitly_wait(0)
        # 3. 尝试定位元素：找到则返回 True，找不到则抛 NoSuchElementException
        nowDriver.find_element(By.XPATH, "//div[@class='el-form-item__content']/span[contains(., '按关键字查询')]").is_displayed()
        nowDriver.find_element(By.XPATH, "//div/span[@class='keyWordQuery']").click()
        print("改为按关键字查询")
        # 注意更改之后会把除了预约数量以外的 兑换信息 均清空（包括兑换时间，所以兑换时间应该在最后再选择）
    except :
        # 4. 捕获“元素不存在”异常，返回 False
        print("已经是按关键字查询")
    
    finally:
        # 5. 无论结果如何，恢复原隐式等待时间（必须执行）
        print("恢复隐式等待时间为设定值")
        nowDriver.implicitly_wait(maxWaitTime)

    # 设置营业厅
    time.sleep(0.1)
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请输入关键字查询")]').send_keys(person.serchKey)
    time.sleep(1)
    nowDriver.find_element(By.XPATH, f'//li[contains(., "{person.hall}")]').click()

    # 设置兑换时间
    time.sleep(0.1)
    nowDriver.find_element(By.XPATH, '//input[contains(@placeholder, "请选择兑换时间")]').click()
    time.sleep(0.2)
    nowDriver.find_element(By.XPATH, f'//li/span[text()="{person.time}"]').click()

    # 点击 确认预约 按钮
    nowDriver.find_element(By.XPATH, f"//div[@class='el-form-item__content']/div[@class='mybutton']").click()

    # 下面这个是弹出来的普通验证码
    # <div data-v-0df9a2f0="" class="catpha-message-box"><div data-v-0df9a2f0="" class="message-wrap"><div data-v-0df9a2f0="" class="img-box"><img data-v-0df9a2f0="" id="validateCode" src="data:image/png;base64,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" alt=""></div> <div data-v-0df9a2f0="" class="input-box"><input data-v-0df9a2f0="" placeholder="请输入验证码" type="text" maxlength="20" onpaste="return false"></div> <div data-v-0df9a2f0="" class="tips-confirm">确认</div></div> <img data-v-0df9a2f0="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAEJUlEQVRoQ+2Z3VHcMBDHd9cFABUEKgCP9A6pIFABoQIuFYRUkKMCoAIuFUDerfFRAVABRwHWZtYjzzg+2ZJ1dyTMoBkegDvr/9svrdYI73zhO9cPHwD/2oNr90BZlgfMvIWI29baAwEkojkzLxDxNc/z+TqhVwYoy3IbAA6ttccAID/y+9BaAMCMiGYA8DvPc/k9eSUDiHBr7TkATFqiH0QcADwR0VNblbV2FwDkRyD33f9E/JSILlNBkgCKojhFxKkT/gwAF2LRWBEOXkAuAOCTADPzhdb6ZqwrRgG4jX8CwFcAqIUrpa7Hbtr+vDFGntWAXBPRt1hDyHOiAcqy3K2q6hYRJUlvtNay8dpWURTXiHjKzPMsy07yPP8rBPs2igIQ8dba0oXM2apW7xNjjJF8Eg8viCiPgQgCSNhUVXXnLH+itZYk3dgqiuIYEW+dJz6HwikIYIy5cjG/Mct3rdHyxLVS6mzIWoMALsGuNhHzIRc2OQEAg4brBXAV5xEAXpVSUr/ffBljJJHZ5YP3wOsFMMZIafs+ZAHnocOQm/vInZXv+4pCEwEA8EMpJXqWlhcg1votNwdjtbtzq2wOlmTnhS0i2vMltBegqQSh+BNRKRCx4uX5rTz0VsA+gPpQIaKdUBkbCzFGvDzbRcNLXyHxAhhjXqRVUErV7XDMivHEWPHNvsYYacG3lFJ7XS1LANLPu1O3N3ECSXkKAEs5kSrehVFdUFw1+us+4QM4stbexcS/D8TniVXEt/OAiORkvm/vuwTQJI3vwzGh1M0JZkbXpCU3gGVZ1kZl5qVE9gE07lqijQXoQMCqJ3kD4DsP3gTAlxNjjDEWQPr8q3WEkFhehEoIrQIxKoRatEndpy9hY0rskEeG8nIjZdQX86tANH1ZVBl1CSid36PWOo+N1ZhSmQpRFIXcBve01ksjm7W2EjHVZixEUiuR0szFiG+8OQYiqZlz9+AnRHzx9R9dIWPEj4Uwxjwy806WZbvR7XS7/whdaJj5KHXEsrELTdPGVlUV9EJskqd8TqwvxwgRHfS19VGX+lUOoRThLgKipiHBsUrsdCBVqO97zVglJreCAK6MSQu77+sG1yncnUH1YAsAHojoKHQjDAK4fJC56BwRt5h5orW+XLdwJ/5cpt7M/NpXdYI3sj5hbj4qY0WZ7Y+eQoSAWxNAsfxxzFy0bhRDD27/350PU9ddJs/028907xrkDrIrMZ9l2SQUNu3vjwJovtiZ6dcgWZb9it3YGeILItbCV3nXkATQnBPW2onkhOSG/E0myog4Y2bvKyZEFCtLktbTDol1iXkimsbCJ+fAQG7I+P3IvfsScTXMwHpmZqlqsyzL7lOFN89P9sAAkFhXoLZblpa3LtKiL/6716xjisAmPrt2D2xC5NAzPwDe2uLd/f4AQbkhXgmzcMcAAAAASUVORK5CYII=" class="imgcode-box-close"></div>

if __name__ == "__main__":
    person1 = Person(name='1234',IDCard='23132532',phone='23132532',province='广东省',city='阳江市',county='江城区',hall='兴华街支行',time='2025-11-25',serchKey='兴华街')
    person2 = Person(name='1234',IDCard='23132532',phone='23132532',province='广东省',city='阳江市',county='江城区',hall='兴华街支行',time='2025-11-25',serchKey='兴华街')
    person3 = Person(name='1234',IDCard='23132532',phone='23132532',province='广东省',city='阳江市',county='江城区',hall='兴华街支行',time='2025-11-25',serchKey='兴华街')
    person4 = Person(name='1234',IDCard='23132532',phone='23132532',province='广东省',city='阳江市',county='江城区',hall='兴华街支行',time='2025-11-25',serchKey='兴华街')
    threading.Thread(target=coinsRunFunc, args=(person1,7360,-200,0), name="Thread-7360").start()
    threading.Thread(target=coinsRunFunc, args=(person2,7361,250,0), name="Thread-7361").start()
    threading.Thread(target=coinsRunFunc, args=(person3,7362,650,0), name="Thread-7362").start()
    threading.Thread(target=coinsRunFunc, args=(person4,7363,1050,0), name="Thread-7363").start()
