#-*- coding:utf-8 -*-
import urllib
from urllib import request
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36",

"Cookie":" __cfduid=d551d805d36f3a060d3e9b3df7f3192831547391276; BDUSS=d0OUdFNVNhRmZ-TDh2Qm9TY2w2QXdyc2hCTENJbDBYRGFqWkhpLXRCZjVuc2xjQVFBQUFBJCQAAAAAAAAAAAEAAAAYGsDpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkRolz5EaJcbn; BAIDUID=084D2BB2DE6FB0AF2879C534256A7EC3:FG=1; PSTM=1554377025; BIDUPSID=BDC9615A9E716348235025B81CCC5A67; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; cflag=13%3A3; BDRCVFR[L_O2j-KLwCb]=9xWipS8B-FspA7EnHc1QhPEUf; delPer=0; PSINO=7; H_PS_PSSID="
}
url="https://mail.126.com/js6/main.jsp?sid=QBXpDiZZCREgDDEnIRZZqNcxnsTgelEq&df=webmail126#module=welcome.WelcomeModule%7C%7B%7D"
req=request.Request(url,headers=header)
rep=request.urlopen(req).read().decode()
print(rep)