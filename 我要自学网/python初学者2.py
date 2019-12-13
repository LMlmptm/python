#-*- coding:utf-8 -*-
# a=open("F:\新建文件夹\电脑快捷键.txt","r")#r 指读的操作  读写操作简称IO操作
# b=a.read()
# print(b)
# a.close()
'''

p=open(r"D:\机械师官方壁纸\222.jpg","rb")
g=p.read()
print(g)
a=open(r"F:\python\limandexifu.jpg","wb")
a.write(g)

p.close()
a.close()
'''
# a=open(r"F:\python\5.py","rb")
# b=a.read()
# print(b)
# c=open(r"D:\机械师官方壁纸\l.py","wb")
# c.write(b)
# a.close()
# c.close()
a=open("D:\第1页.html","rb")
c=a.read()
b=open("D:\网速\z.html","wb")
b.write(c)
#print()