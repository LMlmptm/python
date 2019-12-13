# -*- coding:utf-8 -*-
# import socket
#
# kehu=socket.socket()
# kehu.connect(("localhost",57632))
# kehu.send("nihao".encode())
# # kehu.close()

# 邮箱:lm19970713@126.com
# SMTP服务器:smtp.126.com
# 授权密码为:123456lm
import smtplib
from email.mime.text import MIMEText

msg_from = "lm19970713@126.com"
pwd = "123456lm"
to = "1852509672@qq.com"

subject = "懿曼"
context = "你有没有来北京了吗"
# 构造邮件
msg = MIMEText(context)
msg["Subject"] = subject
msg["From"] = msg_from
msg["To"] = to
# 发送邮件
ss = smtplib.SMTP_SSL("smtp.126.com", 465)
ss.login(msg_from,pwd)
ss.sendmail(msg_from,to,msg.as_string())

