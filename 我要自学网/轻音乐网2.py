#-*- coding:utf-8 -*-
#http://www.htqyy.com/top/hot
#http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20
#http://www.htqyy.com/top/musicList/hot?pageIndex=3&pageSize=20
#http://f2.htqyy.com/play7/28/mp3/4
#http://f2.htqyy.com/play7/21/mp3/4
import requests
import re
import time
sid=[]
sna=[]
star=int(input("请输入你要下载的起始页："))
page=int(input("曼为你选择 ：请输入你要爬取的页数:"))
for i in  range(star,page):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
    res=requests.get(url)
    strr=res.text
    pat1=r'title="(.*?)" sid'#title="夜的钢琴曲五" sid="56"
    pat2=r'sid="(.*?)"'
    idlist=re.findall(pat2,strr)
    namelist=re.findall(pat1,strr)
    sid.extend(idlist)
    sna.extend(namelist)
for i in range(0,len(sid)):
    url1="http://f2.htqyy.com/play7/"+str(sid[i])+"/mp3/4"
    sname=sna[i]
    ress=requests.get(url1).content
    print("正在下载第",i+1,"首歌")
    with open(r"D:\网易云音乐\GamePatch\{}.mp3".format(sname),"wb") as f:
        f.write(ress)
    time.sleep(1)


