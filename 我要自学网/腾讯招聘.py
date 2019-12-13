#-*- coding:utf-8 -*-
import urllib
from urllib import request
from bs4 import BeautifulSoup

headers={"User-Agent":"Mozilla/5.0\
(Windows NT 6.1; WOW64) AppleWe\
bKit/537.36 (KHTML, like Gecko) \
Chrome/57.0.2987.98 Safari/537.\
36 LBBROWSER"}

for i in range(0,3):
    pn=i*10
    start={"start":pn}
    start=urllib.parse.urlencode(start)
    url="https://hr.tencent.com/position.php?&"+start+"#a"
    req=request.Request(url,headers=headers)
    response=request.urlopen(req).read().decode()
    soup=BeautifulSoup(response,"lxml")
    souplist=soup.select('td a[target="_blank"]')

    for i in souplist:
        myurl="https://hr.tencent.com/"+i.attrs["href"]
        req1=request.Request(myurl,headers=headers)
        response1=request.urlopen(req1).read()
        soup1=BeautifulSoup(response1,"lxml")
        name=soup1.select('tr td[colspan="3"]')[0].get_text()

        neirong=soup1.select('ul[class="squareli"] li')
        listl=""
        for i in neirong:
            listl=listl+i.text

        print(name)
        print(listl)
        print("------------------------------分割线------------------------")







