#-*- coding:utf-8 -*-
from urllib import request
import urllib

#https://www.baidu.com/s?wd=%E4%BA%91%E5%8D%97
wd={"wd":"云南"}
wdd=urllib.parse.urlencode(wd)

#https://","http://"));\r\n\t</script>\r\n</head>\r\n<body>\r\n\t<noscript><meta http-equiv="refresh" content="0;url=http://www.baidu.com/"></noscript>\r\n</body>\r\n</html>'

#url="https://www.baidu.com/s?"
#urls=url+wdd
#req=request.Request(urls)
#reponse=request.urlopen(req).read()
#print(reponse)
print(wdd)

