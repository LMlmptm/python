#-*- coding:utf-8 -*-
from urllib import request
import re
import random

Agent1="Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"
Agent2="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
Agent3="Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
list=[Agent1,Agent2,Agent3]
ra=random.choice(list)
print(ra)
header={
    "user-agent":ra
}
url="http://www.baidu.com/"
req=request.Request(url)
reponse=request.urlopen(req).read().decode()
tab="<title>(.*?)</title>"
tac=re.findall(tab,reponse)
print(tac)