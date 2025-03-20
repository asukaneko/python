import os,requests
from bs4 import BeautifulSoup
import time,random

headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

def get_turl(url):
    res = requests.get(url,headers=headers)
    if res.ok:
        bs=BeautifulSoup(res.content,'html.parser')
        urls=bs.find_all('img','lazy')
        li = []
        names = []
        for turl in urls:
            turl = str(turl)
            #print(turl)       
            a = turl.find('data-original=')
            b = turl.find('data-resolution=')
            c = turl.find('alt=')
            d = turl.find('class=')
            urll = "https://www.toopic.cn" + turl[a:b][15:-2]
            name = turl[c:d][5:-2]
            #print(urll)
            #print(name)
            
            li.append(urll)
            names.append(name)
            
        return li,names


def save(url,filename):
    resp = requests.get(url,headers=headers)
    if resp.ok:
        img = resp.content
        filename = filename.replace('/','')
        if not os.path.exists('tupian/'+filename+'.jpg'):
            with open('tupian/'+filename+'.jpg','wb') as f:
                f.write(img)
                print("保存成功",filename)
                #time.sleep(random.randrange(1,3))
        else:
            print("该文件已下载",filename)
    else:
        print("爬取图片内容失败")

def worker():
    raw_urls = []
    n = 285
    for i in range(287):
        n += 1
        raw_urls.append("https://www.toopic.cn/dnbz/?page={}".format(n))
    page = 0
    for raw_url in raw_urls:
        turls,names = get_turl(raw_url)
        page += 1
        print(page)
        for turl,name in zip(turls,names):
            #print(turl)
            save(turl,name)
        
    print("ok")
if __name__ == '__main__':
    worker()
    #get_turl('https://www.toopic.cn/4kbz/?page=1')
    

