#-*- coding:utf-8 -*-
import requests
import json
import re

class xima():
    def __init__(self):
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"}
        self.url="https://www.ximalaya.com/revision/play/album?albumId=21577427&pageNum=1&sort=-1&pageSize=30"
    def xima1(self):
        response=requests.get(self.url,headers=self.headers).content.decode()
        data=json.loads(response)
        data_list=data['data']['tracksAudioPlay']#截取data下面的tracksAudioPlay的内容
        list2=[]
        for i in data_list:
            list1={}#字典
            list1['name']=i['trackName']#字典name属性来代替trackName
            list1['yp']=i['src']
            list2.append(list1)#将字典转换为列表里面
        return list2
    def xima2(self,list2):
        for i in list2:
            i['name']=re.sub('"|\|', '',i['name'])#替换“和|产生的误差 替换成''

            with open(r"F:\喜马拉雅\\"+i['name']+".m4a","ab") as f:
                print("正在保存第",i,"挑数据")
                r=requests.get(i['yp'],headers=self.headers).content
                f.write(r)

    def run(self):
        list2=self.xima1()
        self.xima2(list2)

if __name__ == '__main__':
    ximala=xima()
    ximala.run()
