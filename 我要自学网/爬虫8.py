# #-*- coding:utf-8 -*-
# from lxml import etree
# text ='''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">张三</a></li>
#          <li class="item-1"><a href="link2.html">李四</a></li>
#          <li class="item-inactive"><a href="link3.html">王五</a></li>
#          <li class="item-1"><a href="link4.html">赵六</a></li>
#          <li class="item-0"><a href="link5.html">老七</a>
#      </ul>
#  </div>
# '''
# #etree.HTML将字符串解析成特别的HTML对象
# html=etree.HTML(text)
# #将HTML转换为字符串
# result=etree.tostring(html,encoding="utf8").decode()
# print(result)

'''
(以下内容报错 )
# from lxml import etree
# html=etree.parse("D:\lm.html")
# result=etree.tostring(html,encoding="utf-8").decode()
# print(result)
from lxml import etree

#获取本地html文档
from lxml import etree
html=etree.parse(r"F:\第1页.html")

result=etree.tostring(html,encoding="utf-8").decode()
print(result)
'''
# from lxml import etree
# # # # html=etree.parse(r"C:\hello.html")
# # # # a=html.xpath("//a")#//标签名  拿取标签名内的内容
# # # # print(a[1].text)

# from lxml import etree
# html=etree.parse(r"C:\hello.html")
# b=html.xpath("//li/a[@href='link3.html']")
# print(b[0].text)

# from lxml import etree
# html=etree.parse(r"C:\hello.html")
# c=html.xpath("//li/a/@href")
# print(c)

# from lxml import etree
# html=etree.parse(r"C:\hello.html")
# d=html.xpath("//li/a")
# print(d[0].text)

from lxml import etree
html=etree.parse(r"C:\hello.html")
e=html.xpath("//li[last()-1]/a")
print(e[0].text)
f=html.xpath("//li/a")
print(f[-2].text)
t=html.xpath("//*[@class='item-0']")
print(t[0].tag)#tag表示获取标签名 text表示获取标签内容