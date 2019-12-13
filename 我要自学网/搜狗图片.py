#-*- coding:utf-8 -*-
import requests
import re
import time
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"
}
url="https://pic.sogou.com/pics?query=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&ie=utf-8&bh=1&w=05002600"
response=requests.get(url,headers=headers).text
result=re.findall(r'"pic_url":"(.*?)"',response)
result1=re.findall(r'ThumbUrl":"(.*?)"',response)
x=1
for i in result:
    response1=requests.get(i,headers=headers).content
    print("正在保存第{}几张图片".format(x))
    with open(r'D:\新建文件夹\\{}.jpg'.format(x),'wb') as f:
        f.write(response1)

    time.sleep(1)

    x+=1



