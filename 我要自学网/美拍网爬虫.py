#-*- coding:utf-8 -*-
import re
import requests
#http://www.netbian.com/s/chaogaoqing/index_1.htm
#http://www.netbian.com/s/chaogaoqing/index_2.htm
#http://www.netbian.com/s/chaogaoqing/index_3.htm

#http://www.netbian.com/desk/21754.htm
#<a href="/desk/21754.htm" title=
#<div class="pic"><p><a href="/desk/21754-1920x1080.htm" target="_blank"><img src="http://img.netbian.com/file/2019/0402/5250ecb6d25fa07af734c1d6d2bd61ca.jpg" alt="lol英雄联盟官方佐伊壁纸" title="lol英雄联盟官方佐伊壁纸">
#<div class="pic"><p><a href="/desk/21750-1920x1080.htm" target="_blank"><img src="http://img.netbian.com/file/2019/0401/b5f6d7e765dfc8a70e9aed2783784203.jpg" alt="星愿 女孩子 夜空 星空 唯美动漫壁纸" title=
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"


}
start=int(input("------------------------曼哥在线飙车------------------------- \n"
                "\t*******曼哥教你怎么做黑客********\n"
                "\t+++++怎么来盗取别人的资源++++++\n"
                
                "\t请输入你要爬取的起始页:"))
end=int(input("请输入你要爬取的末页:"))
p=1
for i in range(start,end+1):
    url="http://www.netbian.com/s/chaogaoqing/index_"+str(i)+".htm"
    response=requests.get(url,headers=headers).text
    html=re.findall(r'<a href="(.*?)" title=".*?" target="_blank"><img src=',response)
    #<a href="/desk/21789.htm" title="牛魔-御旌 王者荣耀电脑壁纸 更新时间：2019-04-17" target="_blank"><img src="http://img.netbian.com/file/2019/0417/small74701e6764d8cd589c122729d5be45bb1555475487.jpg" alt="牛魔-御旌 王者荣耀电脑壁纸"><b>牛魔-御旌 王者荣耀电脑壁纸</b></a>
    for x in html:
        URL="http://www.netbian.com"+x
        response1=requests.get(URL,headers=headers).text
        data1=re.findall(r'<div class="pic"><p><a href=".*?" target="_blank"><img src="(.*?)" alt=".*?">',response1)
        for z in data1:
            response2=requests.get(z).content
            print("正在保存第{}张图片".format(p))
            with open(r'D:\机械师官方壁纸\高清壁纸爬虫\超高清壁纸1\{}.jpg'.format(p), 'wb') as f:
                f.write(response2)
            p += 1



