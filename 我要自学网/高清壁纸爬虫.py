#-*- coding:utf-8 -*-
import re
import requests
#http://desk.zol.com.cn/
#http://desk.zol.com.cn/pc/
#/bizhi/265_1288_2.html
#
url="http://desk.zol.com.cn/"
response=requests.get(url).text
data=re.findall(r'<div class="down-img"><a href="(.*?)" target="_blank">',response)
x=1
for i in data:
    URL=url+i
    response1=requests.get(URL).text
    # print(response1)
    Data=re.findall(r'<img id="bigImg" src="(.*?)" width="960" height="600">',response1)
    for z in Data:
        response2=requests.get(z).content
        print("正在保存第{}图片".format(x))
        with open(r'D:\机械师官方壁纸\高清壁纸爬虫\{}.jpg'.format(x), 'wb') as f:
            f.write(response2)
        x += 1

