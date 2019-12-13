#-*- coding:utf-8 -*-
# import pymysql
# #打开数据库连接  主机地址 端口号 用户名 用户密码  数据库名
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="stu",charset="utf8")
# #创建游标对象
# cursor=db.cursor()
# sql="""create table student(
#     id int not null,
#     name varchar(20),
#     age int
# )"""
# cursor.execute(sql)
# db.close()

#print(db)
'''import pymysql
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="stu",charset="utf8")
cursor=db.cursor()
sql="""insert into student(id,name,age)
       values (3,"lm",19)
"""
cursor.execute(sql)
db.commit()
db.close()'''
# import pymysql
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="stu",charset="utf8")
# cursor=db.cursor()
# sql="select * from student"
# cursor.execute(sql)
# a=cursor.fetchone()#查询一个元组的信息
# b=cursor.fetchall()#查询所有表中的信息
# print(b)
'''
import pymysql
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="stu",charset="utf8")
sursor=db.cursor()
sql="update student set age=age+1"
sursor.execute(sql)
db.commit()
db.close()'''
# import pymysql
# db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",db="stu",charset="utf8")
# sursor=db.cursor()
# sql="delete from student where name='lm'"
# sursor.execute(sql)
# db.commit()
# db.close()
import pymysql
db=pymysql.Connect(host="localhost",port=3306,user="root",passwd="root",charset="utf8")
cursor=db.cursor()
sql1="delete from student where name='pu'"
sql2="delete from student where name='li'"
try:
    cursor.execute(sql1)#对数据库进行操作
    cursor.execute(sql2)
    db.commit()#开始提交事务
except Exception as e:
    #db.rollback()#回滚  都不执行
    print("出现异常")
db.close()