#-*- coding:utf-8 -*-
import requests
import re




headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"
}

def sqider():
    url="http://book.zongheng.com/showchapter/795746.html"
    response = requests.get(url,headers=headers).text
    print(response)
    data=re.findall(r'<li class="vip col-4">(.*?)</li>',response)
    print(data)


if __name__ == '__main__':
    sqider()























