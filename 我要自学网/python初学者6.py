#-*- coding:utf-8 -*-
# import threading
# import time
# def run(name):
#     print("线程呗至新浪：",name)
#     time.sleep(5)
# #创建线程
# a=threading.Thread(target=run,args=("a",))
# b=threading.Thread(target=run,args=("b",))
# time.sleep(3)
# a.start()#线程开始
# b.start()
# a.join()#子线程结束后才执行主线程
# b.join()

# import threading
# lock=threading.Lock()#线程锁搭建
# num=100
# def run(object):
#     lock.acquire()#锁住
#     global num
#     num=num-1
#     print("线程：",num,"执行的当前线程为：",num)
#     lock.release()#释放线程锁
# for i in range(0,100):
#     a=threading.Thread(target=run,args=(num,))
#     a.start()
'''from multiprocessing import Process
def run(name):
    print("进程被执行了：",name)
if __name__=='__main__':#win系统必须要这样写才会执行
    p1=Process(target=run,args=("p1",))
    p2=Process(target=run, args=("p2",))
    p3=Process(target=run, args=("p3",))
    p4=Process(target=run, args=("p4",))
    p1.start()
    p2.start()
    p3.start()
    p4.start()'''
import threading

num=50
lock=threading.Lock()

def sale(name):
    lock.acquire()
    global num
    if num>0:
        num=num-1
        print(name,"窗口还剩几张票：",num)
    lock.release()
while 1==1:
     if num>0:
         a=threading.Thread(target=sale, args=("A窗口",))
         b=threading.Thread(target=sale, args=("B窗口",))
         c=threading.Thread(target=sale, args=("C窗口",))
         a.start()
         b.start()
         c.start()
     else:
         break

print("一买完")











