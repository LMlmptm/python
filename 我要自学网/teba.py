#-*- coding:utf-8 -*-
#http://tieba.baidu.com/f?kw=python
#http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50
#http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100
#
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
def lodepage(fullurl,filename):
    print("正在下载第"+filename+"页")
    req=request.Request(fullurl,headers=header)
    response=request.urlopen(req).read()
    return response


def writepage(html,filename):
    print("正在保存第"+filename+"页")
    with open(filename,"wb") as f:
        f.write(html)
    print("_________分割线_______")
def teba(key,begin,end):
    for page in range(begin,end+1):
        pn=(page-1)*50
        fullurl=key+"&pn="+str(pn)
        filename="D:\第"+str(page)+"页.html"
        html=lodepage(fullurl,filename)
        writepage(html,filename)



if __name__=='__main__':
    kw=input("请输入你的贴吧名：")
    begin=int(input("请输入你要下载的起始页:"))
    end=int(input("请输入你要下载的末页:"))
    url="http://tieba.baidu.com/f?"
    k=urllib.parse.urlencode({"kw:":kw})
    key=url+k
    teba(key,begin,end)
    time.sleep(6)

