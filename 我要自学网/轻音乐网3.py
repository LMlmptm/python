#-*- coding:utf-8 -*-
#http://www.htqyy.com/top/hot
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

import requests
import re


startpage=int(input("请输入你要下载的起始页数："))
endpage=int(input("请输入你要下载的末页:"))
pat1list=[]
pat2lista=[]
for i in range(startpage,endpage+1):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    response=requests.get(url).text
    pat1=re.compile(r'title="(.*?)" sid')
    result1=pat1.findall(response)
    pat2=re.compile(r'sid="(.*?)"')
    result2=pat2.findall(response)
    pat2lista.extend(result2)
    pat1list.extend(result1)

#http://www.htqyy.com/play/176
#http://f2.htqyy.com/play7/45/mp3/4
for x in range(0,len(pat2lista)):
    ex="http://f2.htqyy.com/play7/"+str(pat2lista[x])+"/mp3/4"
    Pat1list=pat1list[x]
    response1=requests.get(ex).content
    print("正在保存第：",x+1,"首歌")

    with open(r'F:\自己写的\音乐\{}.mp3'.format(Pat1list),'wb') as f:
        f.write(response1)











