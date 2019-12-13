#-*- coding:utf-8 -*-
import urllib
from urllib import request
from lxml import etree

class tebasp(object):
    def __init__(self):
        self.name="python"
        self.begin=1
        self.end=2
        self.url="http://tieba.baidu.com/f?"
        self.headers={"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
        self.filename=1
    def teba1(self):
        for page in range(self.begin,self.end+1):
            pn=(page-1)*50
            wd={'pn':pn,'wb':self.name}
            word=urllib.parse.urlencode(wd)
            myurl=self.url+word
            self.teba2(myurl)

    def teba2(self,myurl):
        req=request.Request(myurl,headers=self.headers)
        response=request.urlopen(req).read()
        #print(response.decode())
        html=etree.HTML(response)
        data=html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for datas in data:
             datas="http://tieba.baidu.com"+datas
             self.teba3(datas)

    def teba3(self,datas):
        req1=request.Request(datas,headers=self.headers)
        response1=request.urlopen(req1).read()
        html=etree.HTML(response1)
        data1=html.xpath('//img[@class="BDE_Image"]/@src')
        for img in data1:
             self.reba4(img)

    def teba4(self,img):
        print("正在保存第"+self.filename+"图片")
        imge=request.urlopen(img).read()
        file=open(r"C:\Users\黎曼\Desktop\贴吧图片\\" + str(self.fileName) + ".jpg", "wb")
        file.write(imge)
        file.close()
        self.filename=self.filename+1

if __name__=='__main__':
    spteba=tebasp()
    spteba.teba1()