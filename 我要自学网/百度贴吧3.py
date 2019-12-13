#-*- coding:utf-8 -*-
import urllib
from urllib import request
from lxml import etree

class teba(object):
    def __init__(self):
        self.name="python"
        self.begin=1
        self.end=3
        self.url="http://tieba.baidu.com/f?"
        self.headers={"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.fileName=1

    def teba1(self):
        for page in range(self.begin,self.end):
            pn=(page-1)*50
            wo={'pn':pn,'kw':self.name}
            word=urllib.parse.urlencode(wo)
            myurl=self.url+word
            self.teba2(myurl)

    def teba2(self,myurl):
        req=request.Request(myurl,headers=self.headers)
        response=request.urlopen(req).read()
        html=etree.HTML(response)
        data=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for da in data:
            da="http://tieba.baidu.com"+da
            self.teba3(da)
    def teba3(self,da):
        req=request.Request(da,headers=self.headers)
        response=request.urlopen(req).read()
        html=etree.HTML(response)
        data=html.xpath('//img[@class="BDE_Image"]/@src')
        for dat in data:
            self.teba4(dat)

    def teba4(self,dat):
        print("曼哥非诚勿扰：正在保存 图片第：",self.fileName,"....张")
        response = request.urlopen(dat).read()
        file=open(r"C:\Users\黎曼\Desktop\贴吧图片\\"+str(self.fileName)+".jpg","wb")
        file.write(response)
        file.close()
        self.fileName=self.fileName+1




if __name__=='__main__':
    myteba=teba()
    myteba.teba1()

