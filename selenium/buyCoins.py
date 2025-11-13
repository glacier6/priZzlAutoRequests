
# .\venv\Scripts\Activate.ps1
from selenium import webdriver # 用于操作浏览器
from selenium.webdriver.chrome.options import Options # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
from CommonFunc import connectOneChrom,creatOneMyChrom,creatOneNomalChrom,RunCase
import time
import threading

openUrl = r'https://www.bilibili.com/'
# 注意这个里面不会默认有self（就算是加给了某个对象）
def coinsRunFunc(port=7360, positionX=0, positionY=0):
    oneRunCase = RunCase(port=port, positionX=positionX, positionY=positionY, openUrl=openUrl)
    nowDriver = oneRunCase.driver
    print(nowDriver.title)
    # NOTE:下面就可以写操作了

if __name__ == "__main__":
    threading.Thread(target=coinsRunFunc, args=(7360,0,0), name="Thread-7360").start()
    threading.Thread(target=coinsRunFunc, args=(7361,800,0), name="Thread-7361").start()
    threading.Thread(target=coinsRunFunc, args=(7362,0,600), name="Thread-7362").start()
    threading.Thread(target=coinsRunFunc, args=(7363,800,600), name="Thread-7363").start()
