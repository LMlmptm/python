#-*- coding:utf-8 -*-
# import threading
# import time
# def run(name):
#     print(name,"执行了")
#
# t1=threading.Thread(target=run,args=("t1",))
# t2=threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# time.sleep(3)
# print("执行完毕")
# lock=threading.Lock()
# class mythread(threading.Thread):
#     def __init__(self,name):
#         threading.Thread.__init__(self)
#         self.name=name
#     def run(self):
#         lock.acquire()
#         print("线程执行了",self.name)
#         time.sleep(1)
#         print("正在执行中----2")
#         time.sleep(1)
#         print("正在执行中----3")
#         time.sleep(1)
#         print("正在执行中----4")
#         time.sleep(1)
#         print("正在执行中----5")
#         time.sleep(1)
#         print("正在执行中----5")
#         time.sleep(1)
#         print("线程执行结束",self.name)
#         lock.release()
# t1=mythread("t1")
# t2=mythread("t2")
# t3=mythread("t3")
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print("执行完毕所有线程")
'''import queue
q=queue.Queue(maxsize=6)
for i in range(1,7):
    q.put(i)
while not q.empty():
     print(q.get())
'''

# import re
# from aip import AipOcr
# APP_ID="15991515"
# API_KEY="7S8jYuPaOLEhK9rbECEvovjl"
# SELECK_KEY="WMx7nyqE1HlEPiE7sv0Rm2C8lX3uxrgE"
# client=AipOcr(APP_ID,API_KEY,SELECK_KEY)
# with open(r"C:\Users\黎曼\Desktop\贴吧图片\16.jpg","rb") as f:
#     img=f.read()
# data=str(client.basicGeneral(img)).replace(" ","")
# zhi=re.compile(r"{'words':'(.*?)'}")
# jieguo=zhi.findall(data)
# print(jieguo)






from aip import AipOcr
import re
import requests

APP_ID="15725370"
API_KEY="t85bppstXXudNNSU0klALWgj"
SECRET_KEY="Zt7z61AXutINgWS1lqWe3xsWp9uePSFF"

client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

data=requests.get(r"http://127.0.0.1:8020/登陆验证码/login.html").text

pat=re.compile(r'<img src="(.*?)" style')

url="http://127.0.0.1:8020/登陆验证码/"+pat.findall(data)[0]

image=requests.get(url).content


data=str(client.basicGeneral(image)).replace(" ","")

pat=re.compile(r"{'words':'(.*?)'}")

result=pat.findall(data)[0]

print(result)










