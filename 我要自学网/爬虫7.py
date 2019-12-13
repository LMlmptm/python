#-*- coding:utf-8 -*-
# import re
# strr="slseswsd"
# pat="sw"#正则表达式
# ss=re.search(pat,strr)
# print(ss)
'''import re
with open(r"F:\python视频\电脑快捷键.txt","r") as f:
    data=f.read()

pa1="电脑"
pa2="窗口"
a=re.findall(pa1,data)
b=re.findall(pa2,data)
print(len(a),len(b))
'''
# import re
# #原子是以正则表达式的基本
# #匹配通用字符（还有个普通字符）
# #\w 任意字母和数字下划线
# #\W 非字母和数字下划线
# #\d  十进制的数字
# #\D 除了十进制的数字以外的值
# #\s 空白字符
# #\S  非空白字符
# c="sdds@@@#@!sdoushyi132568ds"
# pat="\w\w\w\W\W"
# s=re.search(pat,c)
# print(s)
'''import re
e="1387557953"
pat="1[3587]\d\d\d\d\d"#原子表
print(re.search(pat,e))
r="ksoielhls"
pat1="e[lhe]\w\w\w\w\w"#原子表
print(re.search(pat1,r))'''
# import re
# d="1356897451597513541897551358795"
# pat="..."
# pat1="^13"
# pat2="795$"
# pat3="*5"
# pat4="5?"
# pat5="5+"
# print(re.search(pat5,d))
'''
import re
#{n}表示匹配n个原子
#{n,}表示匹配出现的至少n个原子
#{n,m}表示匹配出现次数在n到m之间的原子
a="1687945498sfbgew5344"
pat="\d{12,16}"
print(re.search(pat,a))
'''
# import re
# a="1346598564"
# b="0213-56795"
# pat="1[3578]\d{8}|\d{4}-\d{5}"
# print(re.search(pat,b))
'''import re
a="@#&%$*^&^%python$*&%$&%^157246843*&^%%&%(*"
pat=".{0,}(python).{0,}(1[3578]\d{7})"#括号中表示要找的内容
print(re.search(pat,a).group(1))#分组（找到目标）
print(re.findall(pat,a))'''
# import re
# a="<div>text1</div>dd<div>text2</div>nn"
# pat=r"<div>(.*)</div>"#贪婪模式  （尽可能多的把所有爬下来）
# print(re.findall(pat,a))
# patq=r"<div>(.*?)</div>"#非贪婪模式  （只爬取目标内容）
# print(re.findall(patq,a))
'''import re
#compile 函数将正则表达式转换为内部格式
a="546PYTHON48dfe"
pat=re.compile("python",re.I)# re.I表示可以忽略大小写
print(pat.findall(a))'''

# import re
# #match函数只匹配开头 信息
# #search函数匹配任意位置
# #match和search函数都是只搜索目标一个
# a="pythonjavaphppythonjava"
# # pat=re.compile("python",re.I)
# # print(pat.match(a))
# pat2=re.compile("(java)",re.I)
# print(pat2.search(a).group())
'''import re
A="---------python==-=-=-=-==-=-=-python-----------------------------python" \
  "---------------==========python===========&^$%*^(%*&%(^$^&%$&*("
pat=re.compile("python",re.I)
print(pat.findall(A))#findall匹配所有目标内容并装到列表中  找到一起给
pat1=re.compile("python",re.I)
ss=pat1.finditer(A)#finditer匹配所有内容并装到迭代器中  找到一个就给一个
list=[]
for i in ss:
    list.append(i.group())
print(list)'''
# import re
# a="张三,,,,王五,,,赵柳,,,,,"
# pat=re.compile(r",+",re.I)
# print(pat.split(a))#匹配的字串将字符串分割后到列表中
# b="hellow 6894,hellow 412"
# pat2=re.compile("\d+")
# res=pat2.sub("666",b)#sub替换目标内容
# print(res)

import re
import requests
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
#<tr bgcolor="#EFF7F0"><td>摩托罗拉</td><td>800-810-5050</td></tr>
#https://changyongdianhuahaoma.51240.com/
response=requests.get("https://changyongdianhuahaoma.51240.com/",headers=header).text
pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
a=re.compile(pat1)
b=re.compile(pat2)
data1=a.findall(response)
data2=b.findall(response)
list=[]
for i in range(0,len(data1)):
    list.append(data1[i]+data2[i])
print(list)