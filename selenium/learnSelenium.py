# 设置浏览器
# 保持浏览器打开状态：add_experimental_option('detach', True)
# 创建并启动浏览器：webdriver.Chrome()

# 导包：from selenium import webdriver
# 导包：from selenium.webdriver.chrome.options import Options
# 导包：from selenium.webdriver.chrome.service import Service

from selenium import webdriver # 用于操作浏览器
from selenium.webdriver.chrome.options import Options # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
import time


# 设置浏览器、启动浏览器
def she():
    q1 = Options() # 创建设置浏览器对象
    q1.add_argument("--no-sandbox") # 禁用沙盒模式(增加兼容性)
    q1.add_experimental_option("detach", True) # 保持浏览器打开状态(默认是代码执行完毕自动关闭)
    a1 = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=q1) # 创建并启动浏览器
    a1.implicitly_wait(30) # 阻塞等待加载，即元素定位隐性等待(多少秒内找到元素就立刻执行，没找到元素就报错)
    return a1

a1 = she() # 一个a1在实际上对应一个浏览器win窗口（可以包含多个标签页）

# NOTE:浏览器操作

a1.set_window_position(0, 0) # 浏览器位置
a1.set_window_size(600, 600) # 浏览器尺寸
a1.forward() # 网页前进
a1.back() # 网页后退

a1.get('https://baidu.com') # 打开标签页
a1.close() # 关闭当前标签页

# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:定位
# 普通定位元素(找到的话返回结果，找不到的话报错)
a2 = a1.find_element(By.ID, 'kw1')   # 把By.ID改成By.NAME就成为按NAME定位

# 普通定位多个元素(找到的话返回列表形式，找不到的话返回空列表)
a2 = a1.find_elements(By.ID, 'kw')   # 同By.CLASS_NAME，By.TAG_NAME

# By.LINK_TEXT
a1.find_element(By.LINK_TEXT, '音乐') # 指定<a></a>中的文本内容来精确找，可能返回多个（find_element会默认调用第一个）

# By.PARTIAL_LINK_TEXT
a1.find_element(By.PARTIAL_LINK_TEXT, '音') # 指定<a></a>中的文本内容来模糊找，可能返回多个（find_element会默认调用第一个）

# By.CSS_SELECTOR （复合定位，本质是用的学过的那个css样式选择器来定位元素）
# 在谷歌控制台可以直接 （右键元素 -> 复制 -> 复制selector） 然后直接得
a1.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(5)").click()

# By.XPATH
# 在谷歌控制台可以直接 （右键元素 -> 复制 -> 复制(完整)XPath） 然后直接得
# 1, 复制谷歌浏览器 Xpath (通过属性+路径定位, 属性如果是随机的，可能定位不到)
a1.find_element(By.XPATH, '//*[@id="s-top-left"]/a[4]').click()
# 2, 复制谷歌浏览器 Xpath 完整路径 (缺点是定位值 比较长，优点是基本100%准确)
a1.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/a[1]').click()

# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:元素的输入，清空，点击, 获取
# 普通元素输入
a2 = a1.find_elements(By.ID, '输入框')
a2.send_keys('dafait')

# 时间元素输入
a2 = a1.find_elements(By.ID, '日期选择')
a2.send_keys('0020251212')

# 上传文件（必须绝对路径）
a2 = a1.find_elements(By.ID, '上传')
a2.send_keys(r'C:\Users\11367\Desktop\绘图1.png')

# 元素清空
a2.clear()

# 元素点击 （注意如果是下拉或者单选多选什么的，也用click就可以了）
a2 = a1.find_element(By.ID, '点击')
a2.click()

# 特殊的弹框操作
print(a1.switch_to.alert.text) # 获取弹窗内的文本内容
a1.switch_to.alert.accept() # 点击当前展示标签页弹出的弹窗确定按钮
a1.switch_to.alert.dismiss() # 点击当前展示标签页弹出的弹窗取消按钮
a1.switch_to.alert.send_keys('大发程序员') # 弹窗输入内容

# 元素文本获取
a2 = a1.find_element(By.XPATH, '//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/p').text

# 元素是否可见 is_displayed()
a3 = a1.find_element(By.XPATH, '//*[@id="ssr-content"]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]/p').is_displayed()

# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:获取句柄，切换标签页
# 获取全部标签页句柄
a2 = a1.window_handles # 是一个字符串数组
a1.close() # 关闭当前标签页
a1.switch_to.window(a2[1]) # 切换标签页
a2 = a1.current_window_handle # 获取当前标签页句柄

# ----------------------------------------------------------------------------------------------------------------------------------------

# NOTE:iframe嵌套页面进入、退出
a2 = a1.find_element(By.XPATH, '/html/body/iframe') # 获取iframe元素
a1.switch_to.frame(a2) # 进入iframe嵌套页面
a1.find_element(By.XPATH, '/html/body/table/tbody/tr/td[1]/a[1]').click() # 进入iframe页面操作元素点击
a1.switch_to.default_content() # 退出iframe嵌套页面(返回到默认页面)
a1.find_element(By.XPATH, '/html/body/input[2]').click()
