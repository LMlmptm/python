#-*- coding:utf-8 -*-
import requests
from pyquery import PyQuery as pq

def get_request(url_img):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400"
    }
    response=requests.get(url_img,headers=headers).content.decode("utf-8")
    doc=pq(response)
    items = doc('.span3').items()
    for item in items:
        url_img = item.find('img').attr('src')
        name = item.find('img').attr('title')
        response1 = requests.get(url_img, headers=headers).content
        print("下载的图片：", url_img, "下载的名称为：", name)

        with open(r"F:\图片爬虫\\" + name + ".jpg", "wb") as f:
            f.write(response1)
        print("下载完毕")


if __name__ == '__main__':
    url = "https://www.dbmeinv.com/?pager%20offset=1&pager_offset="
    page=int(input("请输入你要爬取的页数:"))
    for i in range(1,page+1):
        url_img = url + str(i)
        get_request(url_img)






