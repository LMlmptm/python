#-*- coding:utf-8 -*-
from urllib import request
import random

proxylist=[
    {"142.93.44.189":"3128"},
    {"128.140.225.49": "80"},
    {"211.23.149.28": "80"}

]
proxy=random.choice(proxylist)
proxyHandler=request.ProxyHandler(proxy)
#print(proxyHandler)
oponer=request.build_opener(proxyHandler)
req=request.Request("http://www.baidu.com/")
request.install_opener(oponer)
reponse=oponer.open(req)
print(reponse.read())
