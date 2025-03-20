import os,requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import time,random

headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

def get_turl(url):
    res = requests.get(url,headers=headers)
    if res.ok:
        bs=BeautifulSoup(res.content,'html.parser')
        urls=bs.find_all('a','item')
        li = []
        for turl in urls:
            turl = str(turl)
            a = turl.find('href=')
            b = turl.find('target=')
            urll = turl[a:b][6:-2]
            li.append(urll)
        return li



def get_url(url):
    res = requests.get(url,headers=headers)
    if res.ok:
        bs = BeautifulSoup(res.content,'html.parser')
        img = bs.find('img')
        img = str(img)
        #print(img)
        e = img.find('src=')
        g = img.find('title=')
        urll = img[e:g][5:-2]
        
        name=img[g+7:-3]
        
        return urll,name
    else:
        print("爬取失败")

def save(url,filename):
    resp = requests.get(url,headers=headers)
    if resp.ok:
        img = resp.content
        if not os.path.exists('tupian/'+filename):
            with open('tupian/'+filename,'wb') as f:
                f.write(img)
                print("保存成功")
                time.sleep(random.randrange(1,3))
        else:
            print("该文件已下载",filename)
    else:
        print("爬取图片内容失败")

def worker():
    raw_urls = []
    n = 1
    for i in range(90):
        n += 1
        raw_urls.append("https://www.4kdesk.com/4Kdongman/index_{}.html".format(n))
    for raw_url in raw_urls:
        turls = get_turl(raw_url)
        for turl in turls:
            url,name = get_url(turl)
            print(url,name)
            save(url,name)
        
    print("ok")
if __name__ == '__main__':
    worker()
    #get_turl('https://www.4kdesk.com/4Kdongman/index_2.html')
    

