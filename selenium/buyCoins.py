
# .\venv\Scripts\Activate.ps1
from selenium import webdriver # 用于操作浏览器
from selenium.webdriver.chrome.options import Options # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service # 用于管理谷歌驱动
from selenium.webdriver.common.by import By
from CommonFunc import connectOneChrom,creatOneMyChrom,creatOneNomalChrom
import time
import threading

# 线程任务函数（每个线程对应一个端口，独立执行）
def runtest1():
    try:
        # 给线程1的 Chrome 分配独立位置（避免窗口重叠）
        creatOneMyChrom(port=7360, positionX=0, positionY=0)
    except Exception as e:
        print(f"线程1（7360 端口）执行失败：{str(e)}")

def runtest2():
    try:
        # 线程2的窗口位置错开（比如 X=800，避免和线程1重叠）
        creatOneMyChrom(port=7361, positionX=800, positionY=0)
    except Exception as e:
        print(f"线程2（7361 端口）执行失败：{str(e)}")

def runtest3():
    try:
        # 线程3的窗口位置再错开（X=0，Y=600）
        creatOneMyChrom(port=7362, positionX=0, positionY=600)
    except Exception as e:
        print(f"线程3（7362 端口）执行失败：{str(e)}")

if __name__ == "__main__":
    threading.Thread(target=runtest1, name="Thread-7360").start()
    threading.Thread(target=runtest2, name="Thread-7361").start()
    threading.Thread(target=runtest3, name="Thread-7362").start()
