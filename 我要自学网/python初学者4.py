#-*- coding:utf-8 -*-
# list=[1,2,6,91,0,"a",61,39]
# for i in list:
#     print("------",i)
#     try:
#        print(2/i)
#     except Exception as e:
#         print("出错误的地方为：",e)
#     else:
#         print("正常执行，没有错误")
#     finally:
#         print("结束")
pwd="23124683548"
if len(pwd)<8:
    ex=Exception("密码不能低于八位")
    raise ex
else:
    print("zc")



