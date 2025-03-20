import os,requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import datetime

headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}
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
                print('保存成功')
                with open('a.txt','a+') as f:
                    f.wirte('保存成功'+'\n')
        else:
            print("该文件已下载") 
            with open('a.txt','a+') as f:
                f.wirte('该文件已下载'+'\n')
    else:
        print("爬取图片内容失败")

def worker():
    start = datetime.datetime.now()
    raw_urls = []
    n = 5579
    for i in range(22700):
        n += 1
        raw_urls.append("http://pic.netbian.com/tupian/{}.html".format(n))
    for raw_url in raw_urls:
        url = get_url(raw_url)
        sava(url)
        print('下载路由:',raw_url)
        print('-'*60)
    end = datetime.datetime.now()
    print("ok")
    print("Time\t:",end - start)

if __name__ == '__main__':
    worker()
