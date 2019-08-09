#-*- coding:utf-8 -*-
from pyquery import PyQuery as pq
import requests

html=requests.get("http://news.4399.com/gonglue/lscs/kptj/").content.decode('gb2312')
doc=pq(html)

items=doc('#dq_list > li').items()
for item in items:
    url=item.find('img').attr('lz_src')
    response=requests.get(url).content
    name=item.find('.kp-name').text()
    print("下载的图像为：",url,"名称为：",name)

    with open(r"C:\Users\黎曼\Desktop\贴吧图片\\"+name+".jpg",'wb') as f:
        f.write(response)

print("下载完毕")







