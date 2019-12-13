#-*- coding:utf-8 -*-
# import requests
# # res=requests.get("http://www.baidu.com").content.decode()#content获取以二进制的形式
# # res=requests.get("http://www.baidu.com").text#text获取以字符串的形式
# res=requests.request("get","http://www.baidu.com").content.decode()
# print(res)
'''import requests
import re
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
key="你好"
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
response=requests.post(url,headers=header,data=fromdata)
# print(rest.json())
pat=r'"tgt":"(.*?)"}]]'
res=re.findall(pat,response.text)
print(res)
'''
# import requests
# proxy={
#     "http":"http://101.248.64.72:80"
#
# }
# resp=requests.get("http://www.baidu.com",proxies=proxy)
# print(resp.content.decode())
'''import requests
resp=requests.get("http://www.baidu.com")
cookijar=resp.cookies
cook=requests.utils.dict_from_cookiejar(cookijar)
print(cook)'''
import requests
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
#http://www.renren.com/880151247/profile
ss=requests.session()
data={"email":"13064205179","password":"199707lm"}
ss.post("http://www.renren.com/PLogin.do",data=data)#创建cookies
resp=ss.get("http://www.renren.com/880151247/profile")#要爬取的目标
print(resp.text)