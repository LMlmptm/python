#-*- coding:utf-8 -*-
import requests
from lxml import etree
import queue
import threading
import time

class Thread1(threading.Thread):
    def __init__(self,threadname,page,data):
        threading.Thread.__init__(self)
        self.threadname=threadname
        self.page=page
        self.data=data
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

    def run(self):
        print("线程执行了:", self.threadname)
        while not flag1:
            try:
                page1=self.page.get()
                url="https://www.qiushibaike.com/8hr/page/"+str(page1)+"/"
                response=requests.get(url,headers=self.headers).text
                time.sleep(1)
                self.data.put(response)
                print("线程结束:",self.threadname)
            except Exception as  e:
                pass

class thread2(threading.Thread):
    def __init__(self,threadname,data,filename):
        threading.Thread.__init__(self)
        self.threadname=threadname
        self.data = data
        self.filename = filename

    def run(self):
        print("线程执行了：",self.threadname)

        while not flag2:
            try:
                data1=self.data.get()
                shu=etree.HTML(data1)
                list=shu.xpath('//div/a[@class="recmd-content"]')
                for i in list:
                    data=i.text
                    self.filename.write(data+"\n")

            except Exception as e:
                pass


flag1 = False
flag2 = False
def main():
    page=queue.Queue(10)

    for i in range(1,11):
        page.put(i)

    data=queue.Queue()

    filename=open(r"C:\Users\黎曼\Desktop\贴吧图片\dianzi.txt", "a")

    t1=Thread1("线程爬取",page,data)
    t1.start()
    t2=thread2("线程解析",data,filename)
    t2.start()

    while not page.empty():
        pass
    global flag1
    flag1=True

    while not data.empty():
        pass
    global flag2
    flag2=True
    t1.join()
    t2.join()

    filename.close()

    print("结束所有")


if __name__ == '__main__':
    main()
















