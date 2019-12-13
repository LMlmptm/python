#-*- coding:utf-8 -*-
from bs4  import BeautifulSoup
import re
html = """
<html><head><title>The Dormouse's story</title><title>The Dormouse1's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html,"lxml")
#soup=BeautifulSoup(open("文件具体位置"))打开本地的HTML文件
#print(soup.prettify())
# print(soup.title)#获取title字符串
# print(soup.title.string)#获取title里面的信息
# print(soup.title.name)#获取title的标签
# print(soup.p.attrs)#获取p里面的所有子标签
# print(soup.p.attrs["name"])#获取p里面的name标签的信息
# print(soup.head.contents)#直接获取head的子标签字符串

#获取直接子标签 ，结果生成一个生成器中
# for i in soup.head.children:
#     print(i)

#获取所有子标签 并生成在一个生成器中
# for i in soup.descendants:
#     print(i)

#print(soup.find_all("a"))#获取a标签里面的信息

#print(soup.find_all(id="link2"))
# data=soup.find_all(re.compile("^b"))#find_all生成的是一个结果集resultset
# for i in data:
#     print(i.string)
# data1=soup.find_all(text="Lacie")
# data2=soup.find_all(text=re.compile("Do"))
# for i in data2:
#     print(i)
# #print(data2)

#css样式查找
#data=soup.select("a")#标签查找
#data=soup.select('#link1')#id查找
#data=soup.select(".sister")#类名查找
data=soup.select('a[href="http://example.com/elsie"]')
print(data)