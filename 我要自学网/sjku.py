#-*- coding:utf-8 -*-
import pymysql
import re
import requests
header={
"User-Agent":"Mozilla/5.0 (Linux; U; An\
droid 8.1.0; zh-cn; BLA-AL00 Build/HUAW\
EIBLA-AL00) AppleWebKit/537.36 (KHTML, l\
ike Gecko) Version/4.0 Chrome/57.0.2987.13\
2 MQQBrowser/8.9 Mobile Safari/537.36"
}
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="phone",charset="utf8")
cursor=db.cursor()
response=requests.get("https://changyongdianhuahaoma.51240.com/",headers=header).text
pat1=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>(.*?)</td>[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?</tr>'
pat2=r'<tr bgcolor="#EFF7F0">[\s\S]*?<td>[\s\S]*?</td>[\s\S]*?<td>(.*?)</td>[\s\S]*?</tr>'
a=re.compile(pat1)
b=re.compile(pat2)
data1=a.findall(response)
data2=b.findall(response)
list=[]
sqll="delete from myphone"
cursor.execute(sqll)
db.commit()
for i in range(0,len(data1)):
    list.append(data1[i]+data2[i])
    sql = "insert into myphone(name,phon) values('"+data1[i]+"','"+data2[i]+"')"
    cursor.execute(sql)
print(list)


db.commit()
db.close()

