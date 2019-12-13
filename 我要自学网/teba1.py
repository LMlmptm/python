#-*- coding:utf-8 -*-
#http://tieba.baidu.com/f?kw=python&fr=ala0&tpl=5&traceid=
#http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
#http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
#http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150
#Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/66.0
import urllib
from urllib import request
#import urllib.request
import time

header={
    "User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
def loadpage(fullurl,filename):
    print("正在下载：",filename)
    req=urllib.request.Request(fullurl,headers=header)
    resp=urllib.request.urlopen(req).read()
    return resp

def writepage(html,filename):
    print("正在保存:",filename)
    with open(filename,"wb") as f:
             f.write(html)
    print("--------")
def tiebaSpider(url,begin,end):
    for page in range(begin,end+1):
        pn=(page-1)*50
        fullurl=url+"&pn="+str(pn)
        filename = "D:\第" + str(page) + "页.html"
        html=loadpage(fullurl,filename)
        writepage(html,filename)

        #print("谢谢使用")


if __name__ == '__main__':
    kw=input("请输入贴吧名：")
    begin=int(input("请输入你要下载的起始页："))
    end=int(input("请输入你要下载的末页："))
    url="http://tieba.baidu.com/f?"
    key=urllib.parse.urlencode({"kw":kw})
    url=url+key
    tiebaSpider(url,begin,end)
    #tiebaSpider(url1,begin,end)
    time.sleep(5)


#for i in range(1,4):
#print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))
