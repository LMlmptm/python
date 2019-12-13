#-*- coding:utf-8 -*-
import requests
import time
from lxml import etree
import queue
import threading

class thread1(threading.Thread):
    def __init__(self,threadname,page,data):
        threading.Thread.__init__(self)
        self.threadname=threadname#线程名
        self.page=page#页码
        self.data=data#每一页上面的数据
        self.headers={"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        print("线程开始执行:", self.threadname)
        while not flagt1:
            try:
                page1 = self.page.get()#把每个数字取出来
                url = "https://www.qiushibaike.com/8hr/page/" + str(page1) + "/"
                response = requests.get(url,headers=self.headers).text#爬取每一页的数据
                time.sleep(1)
                self.data.put(response)#把爬取到的数据存入data里面

            except Exception as e:
                pass
        print("线程结束了:", self.threadname)

class thread2(threading.Thread):
    def __init__(self,threadname,data,filename):
        threading.Thread.__init__(self)
        self.threadname=threadname
        self.data=data
        self.filename=filename

    def run(self):
        print("解析线程:",self.threadname)
        while not flagt2:
            try:
                data1=self.data.get()#把data里面的数据一个一个取出来
                html=etree.HTML(data1)
                list=html.xpath('//div/a[@class="recmd-content"]')#解析data里面的数据并清洗
                for i in list:
                    s=i.text#把list里面的数据一个一个拿出来放在s里面并text
                    self.filename.write(s+"\n")


            except Exception as e:
                pass
        print("解析结束:", self.threadname)



flagt1=False
flagt2=False

def main():
    page=queue.Queue(10)
    for i in range(1,11):
        page.put(i)
        data = queue.Queue()
    filename = open(r"C:\Users\黎曼\Desktop\贴吧图片\懿曼.txt", "a")


    t1 = thread1("线程开始执行", page, data)
    t1.start()
    t2 = thread2("解析线程", data, filename)

    t2.start()

    while not page.empty():
        pass
    global flagt1
    flagt1=True

    while not data.empty():
        pass
    global flagt2
    flagt2=True
    t1.join()
    t2.join()


    filename.close()

    print("结束所有")

if __name__=='__main__':
    main()


