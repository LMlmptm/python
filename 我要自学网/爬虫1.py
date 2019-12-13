#-*- coding:utf-8 -*-
from urllib import request

http_hander=request.HTTPHandler
opener=request.build_opener(http_hander)
req=request.Request("http://www.baidu.com/")
#reponse=opener.open(req).read().decode()
request.install_opener(opener)
reponse=request.urlopen(req).read()
print(reponse)