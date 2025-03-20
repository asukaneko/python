from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re,requests
from bs4 import BeautifulSoup
import os
edge_options = Options()
edge_options.add_argument("--headless")

service = Service('edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service, options=edge_options)
purls = []
for i in range(2,1000):
    purls.append("https://wallhaven.cc/latest?page={}".format(i))

def getname(n):
    url = "https://wallhaven.cc/w/"+n
    driver.get(url)
    text = driver.page_source
    text = str(text)
    cont = text.count("png")
    cont += text.count("PNG")
    if cont >=3:
        return "png"
    else:
        return "jpg"

def save(n):
    name = getname(n)
    url = "https://w.wallhaven.cc/full/"+n[:2]+"/"+"wallhaven-"+n+"."+name
    print(url)
    res = requests.get(url)
    try:
        with open(".\photo\\"+n+"."+name,'wb') as f:
            f.write(res.content)
            print("OK")
    except:
        print("已下载")


def geturl(url):
    driver.get(url)
    time.sleep(10)
    res = driver.page_source
    bs = BeautifulSoup(res, 'html.parser')
    urls = bs.find_all('a')
    #print(urls)
    p1 = r'https://wallhaven.cc/w/\w+'
    for url in urls:
        url = str(url)
        #print(url)
        href = re.findall(p1, url)
        if len(href) == 0:
            continue
        #print(href[0])
        uurl = href[0][23:]
        #print(uurl)
        save(uurl)

for purl in purls:
    geturl(purl)
