#-*- coding:utf-8 -*-
import requests
import re

img_input=int(input("请输入你要下载的首页:"))
end_input=int(input("请输入你要下载的末页:"))
st=1
for i in range(img_input,end_input+1):
    url="http://pic.netbian.com/4kmeinv/index_"+str(i)+".html"
    response=requests.get(url).text
    result=re.findall(r'<a href="(.*?)" target="_blank"><img src=".*?" alt=',response)
    for j in range(len(result)):
        info_url="http://pic.netbian.com"+str(result[j])
        response2=requests.get(info_url).text
        result2=re.findall(r'<img src="(.*?)" data-pic=',response2)
        for z in range(len(result2)):
            end_url="http://pic.netbian.com"+str(result2[z])
            response3=requests.get(end_url).content
            print("正在保存第{}张图片".format(st))
            with open("D:\机械师官方壁纸\高清壁纸爬虫\超高清壁纸8\{}.jpg".format(st),"wb") as f:
                f.write(response3)
            st+=1
print("结束爬虫")



