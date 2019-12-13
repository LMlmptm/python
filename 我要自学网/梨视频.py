#-*- coding:utf-8 -*-
import re
import requests

#https://www.pearvideo.com/category_4
#<a href="video_1542160" class="vervideo-lilink actplay">
#https://www.pearvideo.com/video_1541294
#srcUrl="https://video.pearvideo.com/mp4/third/20190411/cont-1541246-10461536-171143-hd.mp4"
daihao=int(input("-----------------------------********************懿曼******************-------------------------------\n\n"
                 "10>新知\t"
                "1>社会\t"
                "2>世界\t"
                "9>体育\t"
                "5>生活\t"
                "8>科技\t"
                "4>娱乐\t"
                "3>财富\t"
                "31>汽车\t"
                "6>美食\n"
                 "\n"
                 "懿曼为你破解梨视频 请输入你要爬取的代号（进官网看准那个视频都可以发送你的代号）:"))
url="https://www.pearvideo.com/category_"
zurl=url+str(daihao)
res=requests.get(zurl).text
result=re.findall(r'<a href="(.*?)" class="vervideo-lilink actplay">',res)
x=1
for i in result:
    surl="https://www.pearvideo.com/{}".format(i)
    ress=requests.get(surl).text
    result1=re.findall(r'srcUrl="(.*?)"',ress)
    print(result1)
    print("正在保存第{}个视频".format(x))

    for z in result1:
        resss=requests.get(z).content
        with open(r'D:\腾讯视频\{}.mp4'.format(x),'wb') as f:
            f.write(resss)

    x += 1






