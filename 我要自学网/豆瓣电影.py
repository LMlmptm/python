#-*- coding:utf-8 -*-
import json
import requests

url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
with open(r'F:\自己写的\\man.csv',"a") as f:
    f.write('电影名,评分,覆盖,地址\n')
    response = requests.get(url).content.decode()

    result = json.loads(response)
    res = result['subjects']
    for i in res:
        title = i['title']
        rate = i['rate']
        cover = i['cover_x']
        url1 = i['url']

        f.write('{},{},{},{}\n'.format(title, rate, cover, url1))





