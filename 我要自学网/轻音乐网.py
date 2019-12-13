#-*- coding:utf-8 -*-
#http://www.htqyy.com/top/hot
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20
#http://www.htqyy.com/play/33
import requests
import re
import time
page=int(input("请输入你要爬取的页数："))
songID=[]
songName=[]
for i in range(0,page):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    html=requests.get(url)
    strr=html.text
    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    idlist=re.findall(pat2,strr)
    titlelist=re.findall(pat1,strr)
    songID.extend(idlist)
    songName.extend(titlelist)

#http://f2.htqyy.com/play7/28/mp3/4     http://www.htqyy.com/play/176

for i in range(0,len(songID)):
    songurl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/4"
    songname=songName[i]
    data=requests.get(songurl).content
    print("正在下载第：",i+1,"首歌")
    with open(r"D:\网易云音乐\{}.mp3".format(songname),"wb") as f:
        f.write(data)
    time.sleep(1)