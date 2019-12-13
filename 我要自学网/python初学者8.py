#-*- coding:utf-8 -*-
# import datetime
# now=datetime.datetime.now()
# print(now)
'''
import datetime
now=datetime.datetime.now()
d=now.strftime("%Y-%m-%d %H:%M:%S")#时间转字符串
print(d)
'''
# import datetime
# s="2020-12-12 22:29:32"
# d=datetime.datetime.strptime(s,"%Y-%m-%d %H:%M:%S")#字符串转时间
# print(d)
'''
import json
b='{"beijin":"北京","于娜娜娜娜":"与拉"}'
c=json.loads(b)
print(type(c))
'''
# import json
# c={"nihao":"你好","buhao":"不好"}
# d=json.dumps(c,ensure_ascii=False)
# print(type(d))
a="你好"
b=a.encode("gbk")#编码
#print(b)
c=b.decode("gb2312")#解码
print(c)