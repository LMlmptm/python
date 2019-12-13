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
response=requests.get(url,headers=header).text
html=etree.HTML(response)
#<a href="/article/121194522" class="content" onclick="_hmt.push(['_trackEvent', '10_multi_3_index', 'chick']);">
#<a href="/article/121222039" class="content" onclick="_hmt.push(['_trackEvent', '4_video_big_index', 'chick']);" >
#<a href="/gif/1-122541.html" class="content" onclick="_hmt.push(['_trackEvent', '9_gif_big_index', 'chick']);" >
#<div class="text-box">咏春春到底能不能实战，这视频告诉你……</div>
#https://www.qiushibaike.com/article/121173618
result1=html.xpath('//div//a[@class="recmd-content"]/@href')
#print(result1)
for site in result1:
    url1="https://www.qiushibaike.com"+site
    response2=requests.get(url1).text
    html2=etree.HTML(response2)
    result2=html2.xpath('//div[@class="content"]')
    print(result2[0].text)

