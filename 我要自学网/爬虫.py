#-*- coding:utf-8 -*-
#import urllib.request
from urllib import request
import re
import random
Agent1={"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"}
Agent2={"Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.83 Mobile Safari/537.36 T7/10.13 baiduboxapp/10.13.0.10 (Baidu; P1 6.0.1)"}
Agent3={"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
Agent4={"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"}
list=[Agent1,Agent2,Agent3,Agent4]
agent=random.choice(list)
print(agent)
header={
"User-Agent":agent}
url=r"http://www.baidu.com/"
req=request.Request(url)
response=request.urlopen(req).read().decode()
tab=r"<title>(.*?)</title>"
wen=re.findall(tab,response)
print(wen[0])