#-*- coding:utf-8 -*-
#https://movie.douban.com/j/subject_abstract?subject_id=1292052
#https://movie.douban.com/j/subject_abstract?subject_id=1291546
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=20
#https://movie.douban.com/j/subject_abstract?subject_id=1296141
#https://movie.douban.com/j/subject_abstract?subject_id=1291858
#https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=60
import re
from urllib import request
import urllib
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"

}#"rate":"9.6"   "title":"肖申克的救赎"
url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%BB%8F%E5%85%B8&sort=recommend&page_limit=20&page_start=0"
req=request.Request(url,headers=header)
response=request.urlopen(req).read().decode()
pat1=r'"title":"(.*?)"'
pat2=r'"rate":"(.*?)"'
a1=re.compile(pat1,re.I)
b1=re.compile(pat2,re.I)
a2=a1.findall(response)
b2=b1.findall(response)
#print(c,d)
for i in range(len(a2)):
    print("排行第",i+1,"版的电影是：",a2[i],"评分为：",b2[i])