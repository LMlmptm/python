#-*- coding:utf-8 -*-
import re
import requests
#http://www.aigei.com/view/72246.html
url="http://www.aigei.com/view/72246.html"
response=requests.get(url).text
result1=re.findall(r'src=(.*?) class="radius0 ">',response)
x=1
for i in result1:
    i = re.sub("'", '', i)
    response1=requests.get(i).content
    print("正在保存第{}张图片".format(x))
    with open(r"C:\Users\黎曼\Desktop\飞机大战蔬菜\{}.jpg".format(x),"wb") as f:
        f.write(response1)

    x+=1

#<img width=".*?" height=".*?" style=".*?" src="http://s.aigei.com/src/img/png/2a/2a420ffd259e47b49d0e925d55b8786f.png?imageMogr2/auto-orient/thumbnail/!75x113r/gravity/Center/crop/75x113/quality/85/&amp;e=1735488000&amp;token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:kFxuSt21mcpTXvX0EGJac-VkVLI=" class="radius0 ">
#http://s.aigei.com/src/img/png/2a/2a420ffd259e47b49d0e925d55b8786f.png?imageMogr2/auto-orient/thumbnail/!75x113r/gravity/Center/crop/75x113/quality/85/&amp;e=1735488000&amp;token=P7S2Xpzfz11vAkASLTkfHN7Fw-oOZBecqeJaxypL:kFxuSt21mcpTXvX0EGJac-VkVLI=

