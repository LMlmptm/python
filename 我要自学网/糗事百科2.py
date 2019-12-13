#-*- coding:utf-8 -*-
import requests
from lxml import etree
header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0\
	.2743.116 Safari/537.36',
	'Accept-Language': 'zh-CN,zh;q=0.8'
}
url='https://www.qiushibaike.com/'
response=requests.get(url).text#<a class="recmd-content" href="/article/121165527"
html=etree.HTML(response)
result=html.xpath('//div//a[@class="recmd-content"]/@href')
for i in result:
    url1="https://www.qiushibaike.com"+i
    response1=requests.get(url1).text
    html1=etree.HTML(response1)
    result1=html1.xpath("//div[@class='content']")
    print(result1[0].text)