#-*- coding:utf-8 -*-
import requests
import re
#http://desk.zol.com.cn/meinv/
#http://desk.zol.com.cn/meinv/2.html
#http://desk.zol.com.cn/meinv/3.html
#"/bizhi/7407_91896_2.html"           http://desk.zol.com.cn/meinv//bizhi/7407_91896_2.html
#http://desk.zol.com.cn//bizhi/7407_91896_2.html
start=int(input("请输入你要爬取的起始页:"))
end=int(input("请输入你要爬取的末页:"))
st=1
for i in range(start,end+1):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"
    }
    url="http://desk.zol.com.cn/meinv/"+str(i)+".html"
    response=requests.get(url,headers=headers).text
    data=re.findall(r'<a class="pic" href="(.*?)" target="_blank" hidefocus="true">',response)
    for x in data:
        URL = "http://desk.zol.com.cn/" + x
        response1 = requests.get(URL, headers=headers).text
        Data = re.findall(r'<img id="bigImg" src="(.*?)"', response1)
        for z in Data:
            response2 = requests.get(z).content
            print("正在保存第{}图片".format(st))
            with open(r'D:\机械师官方壁纸\高清壁纸爬虫\类型壁纸\{}.jpg'.format(st), 'wb') as f:
                f.write(response2)
            st += 1


