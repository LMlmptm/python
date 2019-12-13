#-*- coding:utf-8 -*-
import requests
import re

start=int(input("请输入你要爬取的起始页:"))
end=int(input("请输入你要爬取的末页:"))
z=1
for i in range(start,end+1):
    url="http://www.playke.com/page/"+str(i)
    #print(url)
    response=requests.get(url).text
    #print(response)
    result=re.findall(r"<a href='(.*?)' class='imageLink image loading' target='_blank'>",response)
    #print(result)
    for j in range(len(result)):
        response1=requests.get(result[j]).text
        #print(response1)
        result1=re.findall(r'<a href="(.*?)"><img alt=',response1)
        #print(result1)
        for x in range(len(result1)):
            response2=requests.get(result1[x]).content
            print("正在保存第{}张图片".format(z))
            with open(r"D:\机械师官方壁纸\高清壁纸爬虫\性感图片1\{}.jpg".format(z), "wb") as f:
                f.write(response2)
            z+=1


