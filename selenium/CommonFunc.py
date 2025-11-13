# 多线程执行自动化(四开浏览器)
# 导包：import threading
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###
# 该教程内出现的演示地址均不能做任何破坏行为，否则后果自负###


import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading
import socket

# 普通方式调用，即自己直接打开一个，不设置用户目录
def creatOneNomalChrom(x,y,ipPort,openUrl=r'https://www.bilibili.com/'):
    op = Options()
    op.add_argument("--no-sandbox")
    op.add_experimental_option("detach", True)
    chromW = webdriver.Chrome(service=Service(r'chromedriver.exe'), options=op)
    chromW.set_window_position(x, y)
    chromW.set_window_size(200, 400)
    chromW.implicitly_wait(30)
    chromW.get(openUrl)
    return chromW

# 判断端口是否正在被监听（用于判断chrome是否已经启动）
def is_port_listening(port, host="localhost", timeout=1):
    """检查指定端口是否已被监听（判断 Chrome 是否启动就绪）"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        sock.close()
        return True  # 端口已监听（Chrome 就绪）
    except (ConnectionRefusedError, TimeoutError):
        return False  # 端口未监听（Chrome 未就绪）
    
chrome_drivers = []

# 第一步：以 “远程调试模式” 启动 Chrome
#   需先关闭所有已打开的 Chrome 窗口（避免端口冲突），再通过命令行启动 Chrome，并指定调试端口（如9222，可自定义未被占用的端口）。
#   操作系统	操作步骤
#   Windows	
#     1. 按下 Win + R，输入 cmd 打开命令提示符；
#     2. 输入 Chrome 安装路径命令（需根据实际安装路径调整）：
#     cd C:\Program Files\Google\Chrome\Application & chrome.exe --remote-debugging-port=9222 --user-data-dir="E:\seleniumUserDate\zzlUser"
#     - --remote-debugging-port=9222：指定调试端口为 9222（关键参数）；
#     - --user-data-dir：指定一个独立的用户配置文件夹（避免干扰默认 Chrome 数据，可选但推荐）。
#     NOTE:user-data-dir不能直接指定为本地默认已有的那个文件夹，但可以把那个文件夹复制一份放在别处然后指定

#   Mac	
#     1. 打开 “终端”（Launchpad→其他→终端）；
#     2. 输入命令（默认安装路径）：
#     /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/你的用户名/ChromeDebugProfile"
#   Linux	
#     1. 打开终端；
#     2. 输入命令（默认安装路径）：
#     google-chrome --remote-debugging-port=9222 --user-data-dir="/home/你的用户名/ChromeDebugProfile"
#     执行命令后，会弹出一个新的 Chrome 窗口，此时该窗口已处于 “可被 Selenium 连接” 的状态。

# 第二步：Selenium 连接已启动的 Chrome
#   通过ChromeOptions配置 “调试端口”，让 Selenium 跳过 “启动新浏览器”，直接连接第一步打开的 Chrome 窗口。代码示例如下：
#   python
# 连接一个已经打开的Chrome
def connectOneChrom(port):
    """连接指定端口的 Chrome，返回驱动实例（无全局变量覆盖）"""
    driver_path = "./chromedriver.exe"  # 确保路径正确
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{port}")
    
    # 等待 Chrome 端口就绪（最多等 10 秒，避免无限等待）
    wait_time = 0
    max_wait = 10
    while not is_port_listening(port) and wait_time < max_wait:
        print(f"等待 {port} 端口的 Chrome 启动...（已等 {wait_time} 秒）")
        time.sleep(1)
        wait_time += 1
    if wait_time >= max_wait:
        raise Exception(f"{port} 端口的 Chrome 启动超时（超过 {max_wait} 秒）")
    
    # 连接 Chrome 并返回驱动
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print(f"成功连接 {port} 端口的 Chrome")
    return driver


# 先用CMD创建一个可监听的chrome，然后再连接进行操作
def creatOneMyChrom(
    port=9222, 
    positionX=0, 
    positionY=0, 
    sizeX=800, 
    sizeY=600, 
    maxWaitTime=30, 
    userDataDir=r'E:\seleniumUserDate\zzlUser', 
    openUrl=r'https://www.bilibili.com/'
):
    """启动 Chrome 并完成初始化（独立操作，不依赖全局变量）"""
    # 1. 构造启动命令（注意：每个 Chrome 实例的 userDataDir 必须独立！否则会冲突）
    # 关键：给不同端口的 Chrome 分配不同的 userDataDir（避免数据目录冲突）
    unique_user_dir = f"{userDataDir}_port{port}"  # 比如 E:\seleniumUserDate\zzlUser_port7360
    cmd = (
        f'cd "C:\\Program Files\\Google\\Chrome\\Application" '
        f'& chrome.exe --remote-debugging-port={port} --user-data-dir="{unique_user_dir}"'
        # NOTE:注意同时启动多个窗口时，dir目录必须不同，否则操作的都只会是一个，所以，如果想用同一个用户的界面，需要先复制多个相同的用户目录
    )
    
    # 2. 启动 Chrome（异步，不阻塞）
    try:
        subprocess.Popen(
            cmd,
            shell=True,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
            close_fds=True
        )
        print(f"已触发 {port} 端口的 Chrome 启动命令")
    except Exception as e:
        raise Exception(f"{port} 端口的 Chrome 启动失败：{str(e)}")
    
    # 3. 连接 Chrome 并执行操作（独立驱动，不覆盖）
    driver = connectOneChrom(port)
    # 窗口操作（只针对当前驱动对应的 Chrome）
    driver.set_window_position(positionX, positionY)
    driver.set_window_size(sizeX, sizeY)
    driver.implicitly_wait(maxWaitTime)
    driver.get(openUrl)
    
    # 4. 将驱动添加到全局列表（后续可通过列表操作多个实例）
    chrome_drivers.append({"port": port, "driver": driver})
    return driver


# 一个实际的运行实例
class RunCase:
    def __init__(
        self,    
        port=7360, 
        positionX=0, 
        positionY=0, 
        sizeX=800, 
        sizeY=600, 
        maxWaitTime=30, 
        userDataDir=r'E:\seleniumUserDate\zzlUser', 
        openUrl=r'https://www.bilibili.com/'):
        self.port = port
        self.positionX = positionX
        self.positionY = positionY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.maxWaitTime = maxWaitTime
        self.userDataDir = userDataDir
        self.openUrl = openUrl
        self.driver = creatOneMyChrom(    
            port=port, 
            positionX=positionX, 
            positionY=positionY, 
            sizeX=sizeX, 
            sizeY=sizeY, 
            maxWaitTime=maxWaitTime, 
            userDataDir=userDataDir, 
            openUrl=openUrl
        )