#-*- coding:utf-8 -*-
import urllib
from urllib import request
import re
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
key="手电筒"
url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
fromdata={
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "15544389324176",
    "sign": "50aa21b620471c4785cf978741a94b0f",
    "ts": "1554438932417",
    "bv": "481b92af8a7ca0023c6f0ab1d2bd5fa6",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
    "typoResult": "false"
}
data=urllib.parse.urlencode(fromdata).encode(encoding='utf-8')
req=request.Request(url,data,headers=header)
resp=request.urlopen(req).read().decode()
pat=r'"tgt":".*?"'
a=re.findall(pat,resp)
print(a[0])