#-*- coding:utf-8 -*-
import re
import requests

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"
}
start=int(input("请输入你要爬取的起始页:"))
end=int(input("请输入你要爬取的末页:"))
r=1
for i in range(start,end+1):
    url='http://www.jj20.com/bz/nxxz/shxz/list_62_'+str(i)+'.html'
    response=requests.get(url,headers=headers).text
    html=re.findall(r'<a href="(.*?)" target="_blank"><img loadsrc',response)
    #print(html)

    for x in html:
        zurl="http://www.jj20.com"+x
        #print(zurl)
        response1=requests.get(zurl,headers=headers).text
        img=re.findall(r'<img id="bigImg" src="(.*?)" alt=".*?"></a>',response1)
        #print(img)
        for v in img:
            response2=requests.get(v,headers=headers).content
            print("正在保存{}".format(r))
            with open(r'D:\机械师官方壁纸\高清壁纸爬虫\360\{}.jpg'.format(r), "wb") as f:
                f.write(response2)
            r+=1
