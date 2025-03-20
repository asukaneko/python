#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 00:22:48 2021

@author: pi
"""

import requests,os
from bs4 import BeautifulSoup
import datetime,time,random

headers={
       'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

ha = datetime.date.today()
t = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
n = 1
q = "http://127.0.0.1:8000/pic.netbian/dongman"
h = requests.get(q,headers=headers)
bs = BeautifulSoup(h.content,'lxml')
lys = bs.find_all("a")

    
"""这个部分是爬取url
"""
urls = []
for ly in lys:
    #print(img)
    ly = str(ly)
    f = ly.find('href=')
    g = ly.find('>')
    ly = 'http://127.0.0.1:8000/pic.netbian/dongman/'+ly[f:g].replace('href=','').replace('"','')[:-1]
    #print(ly)
    urls.append(ly)        
#print(urls)

    
    
"""这个部分是保存文件
"""

for url in urls:
    h = requests.get("{}".format(url),headers=headers)
    bs1 = BeautifulSoup(h.content,'lxml')
    imgs = bs1.find_all("a")
    for img in imgs:
        #print(img)
        img = str(img)
        d = img.find('href=')
        e = img.find('>')
        img = "{}/".format(url)+img[d:e].replace('href=','').replace('"','')
        #print(img)
        #time.sleep(random.choice(t))
        os.system("wget -P /home/pi/Documents/数据库/爬虫数据/shiyan/{} {} ".format(ha,img))
print("Ok!")
print("爬取主路径：{}".format(q))
print("所有路径：{}".format(urls))

