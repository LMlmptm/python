#-*- coding:utf-8 -*-
#https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&from=result#%E5%85%A8%E9%83%A8
#https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&from=result#%E5%85%A8%E9%83%A8
#https://pic.sogou.com/pics/recommend?category=%C3%C0%C5%AE&from=result
#https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%85%A8%E9%83%A8&start=15&len=15
#
import requests
import re
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"
}
start=int(input("请输入你要爬取的起始页:"))
end=int(input("请输入你要爬取的末页:"))
r=1
for i in range(start,end+1):
    url="https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=%E7%BE%8E%E5%A5%B3&tag=%E5%85%A8%E9%83%A8&start="+str(i)+"&len=15"
    response=requests.get(url,headers=headers).text
    data=re.findall(r'"thumbUrl":"(.*?)"',response)
    for i in data:

        print("正在保存第{}张图片".format(r))
        response1=requests.get(i,headers=headers).content
        with open(r'D:\机械师官方壁纸\高清壁纸爬虫\360\{}.jpg'.format(r),"wb") as f:
            f.write(response1)
        r+=1




