#-*- coding:utf-8 -*-
# a=24.0
# b=23
# c="lsh"
# #x=bool(a)
# print(type(c))
# list=["a","b","c",3421]
# list.append(324)
# list.remove(list[0])
# del list[3]
# list.insert(3,"o")
# list.pop(3)
#
# print(len(list))
'''a=3
b=5
#a+=3
a=a**2
print(a)'''
# a=("v","u","v")
# # c=a.pop(1)#tuple元组不能被修改  所以会报错
# # print(c)
'''a=["b","g","b","e",1,2,1,3,3]
f=set(a)#集合可以去重复
print(f)
'''
# a={"name":"zhangsan","age":"23"}
#
# print(a["name"])#字典键不可以重复
# cunkun=int(input("请输入你的钱："))
# yuer=int(input("输入你的余额:"))
# if cunkun>30:
#     print("有钱人")
#     if yuer>50:
#         print("世界级")
#     elif yuer>30:
#         print("国家级")
#     else:
#         print("地区级")
#
# elif cunkun>20:
#     print("还行吧")
#     if yuer>50:
#         print("中上")
#     else:
#         print("一把那般")
# else:
#     print("马龙")
'''
print("欢迎来到慢慢批发市场")
weight=int(input("请输入你要批发的重量（千克）："))
num=str(input("请输入你要批发的地点(01：东北三省  02：云贵川  03:北上广深 04：其他地方):"))
p=0
while 1=1:


print("你要缴纳的费用为:",p,"元")
print("欢迎下次再来慢慢批发市场")
'''
# a=[235,354,21,23,10,3569,95,63]
# sum=0
# for i in range(0,len(a)-1):
#     if a[i]<=a[i+1]:
#         sum=a[i+1]
#
# print(sum)
'''
#while循环
i=0
sum=0

while i<=23:
    i = i + 1
    print("第",i,"年到了")
    j = 1
    if i==10:
        print("你没有办法了  那好给你一个缓冲的时间  来年再给")
        continue
    while j<=12:
        
        sum = sum + 15.6

        print("第",i,"年","第",j,"月","你需要交纳的费用为:",round(sum,6))
        j = j + 1

'''
name1="1001"
pw1="12345"
name2="1002"
pw2="1234"
num1=10000
num2=20000
num=0
time1=0
print("欢迎来到慢慢银行")

while True:
    name = input("请输入你的银行卡号：")
    paw = input("请输入你的密码:")
    if name==name1 and paw==pw1:
        num=num1
    elif name == name2 and paw==pw2:
         num=num2
    else:
        time1=time1+1
        if time1>=3:
            print("你的卡已经呗锁，对不起滚吧")
            break
        else:
             print("你的输入有误，请重新输入")
             continue

    while True:
        a=input("请输入你要选着的业务：1 存款  2 取款 3 退出 4 余额查询")
        if a=="1":
            b=float(input("请输入你要存的金额(万)："))
            if b<=0:
                print("你的输入错误，是不是一个男子汉")
            else:
                num=num+b
                print("你存款金额为：",b,"你存款后余额为:",num)
        elif a=="2":
             c=float(input("请输入你的取款金额："))
             if c>num:
                print("你的钱不足 看清楚了再取钱")
             else:
                num=num-c
                print("你取款金额为：",c,"你取款后余额wei:",num)
        elif a=="3":
            break

        else:
            print("你的余额为：",num)















