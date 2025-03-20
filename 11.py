import os,requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import datetime

headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1',
}

def get_img_url(url):
    imgurls = []
    res = requests.get(url,headers=headers)
    if res.ok:
        bs = BeautifulSoup(res.content,'html.parser')
        hrefs = bs.find_all('a')
        #print(hrefs)
        for href in hrefs:
            href = str(href)
            a = href.find('href="/tupian')
            b = href.find('title')
            href = 'http://pic.netbian.com'+href[a:b][6:-18]
            #print(href)
            if href != 'http://pic.netbian.com':
                imgurls.append(href)
        print(imgurls)
        return imgurls
    else:
        print('爬取失败')

def get_url(url):
    res = requests.get(url,headers=headers)
    if res.ok:
        bs = BeautifulSoup(res.content,'html.parser')
        img = bs.find('img')
        img = str(img)
        d = img.find('src=')
        e = img.find('title=')
        img = "http://pic.netbian.com" + img[d:e].replace('src=','').replace('"','')[:-1]
        return img
    else:
        print("爬取失败")

def sava(url):
    try:
        filename = url.lstrip('http://').replace('/','')
    except Exception:
        return;
    resp = requests.get(url,headers=headers)
    if resp.ok:
        img = resp.content
        if not os.path.exists('tupian/clear/'+filename):
            with open('tupian/clear/'+filename,'xb') as f:
                f.write(img)
                print("保存成功",filename)
                with open('a.txt','a+') as f:
                    f.wirte('保存成功'+'\n')
        else:
            print("该文件已下载")
    else:
        print("爬取图片内容失败")

def worker():
    start = datetime.datetime.now()
    raw_urls = ['http://pic.netbian.com']
    n = 1
    for i in range(32):
        n += 1
        raw_urls.append("http://pic.netbian.com/index_{}".format(n))
    for raw_url in raw_urls:
        imgurls = get_img_url(raw_url)
        for imgurl in imgurls:
            url = get_url(imgurl)
            sava(url)
    end = datetime.datetime.now()
    print("ok")
    print("Time\t:",end - start)

if __name__ == '__main__':
    worker()
