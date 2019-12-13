#-*- coding:utf-8 -*-
import urllib
from urllib import request
import time

header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
#http://tieba.baidu.com/f?kw=%B0%D9%B6%C8&fr=ala0&loc=rec
#http://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6&ie=utf-8&pn=50
#http://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6&ie=utf-8&pn=100
def lode(fillname,page):
    print("正在打印："+page)
    req=request.Request(fillname,headers=header)
    response=request.urlopen(req).read()
    return response
def write(html,page):
    print("正在保存："+page)
    with open(page,"wb") as f:
        f.write(html)
    print("______分割线_______")

def teba(begin,end):
    for i in range(begin,end+1):
        p=(i-1)*50
        fillname = url + "&pn=" + str(p)
        page="F:\第"+str(i)+"页.html"
        html=lode(fillname,page)
        write(html,page)

if __name__=='__main__':
    begin=int(input("请输入你要爬取的起始页："))
    end=int(input("请输入你要爬取的末页:"))
    url="http://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6"
    teba(begin,end)
    time.sleep(4)
