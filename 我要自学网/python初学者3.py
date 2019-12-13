#-*- coding:utf-8 -*-
# class Dog(object):
#     neme="狗狗"#类变量
#     def __init__(self,a,b,c):#初始化
#         self.age=b
#         self.sex=c
#         self.name=a#实例变量
#
#     def run(self,speed):#普通化
#         print(self.name,"狗狗在跑,速度为：",speed)
# dog=Dog("小狗","23","公的",)
# print(dog.name)
#
# dog.run("十米每秒")
'''
class Card(object):
    def __init__(self,a,b,c):
        self.nu=a
        self.na=b
        self.__nm=c
    def lm(self):
        self.na
    def getnm(self,nuu,naa):
        if nuu==self.nu and naa==self.na:
           return self.__nm
        else:
            return "输入错误"
card1=Card("232","123545","45")
print(card1.getnm("232","123545"))
#print(card1._Card__nm)#就算封装也能拿到
'''
# class Animai(object):
#     def __init__(self,color):
#         self.color=color
#     def eat(self):
#         print("动物")
# class Cat(Animai):
#     pass
   # def __init__(self,m):
   #     self.m=m
   # def eat(self):
   #      print("小猫")
# class Dog(Animai):
#     def __init__(self,sex,color):
#       super(Dog, self).__init__(color)
#       self.sex = sex
#     def eat(self):
#         print("小狗")
# cat=Cat("蓝白色")
# # print(cat.color)
#cat=Cat("民族")
#print(cat.m)
# dog=Dog("男","白色")
# print(dog.color)

# def feed(bj):#类的多态
#     bj.eat()
# an=Animai("白色")
# ca=Cat("汉的")
# do=Dog("女的","蓝色")
#
# feed(an)
