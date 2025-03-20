import requests
import os
import time,datetime
import multiprocessing as mp

raw_url = 'https://www.bilibili.com/index/recommend.json'
headers = {
    'Host':'www.bilibili.com',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
ha = datetime.date.today()

def get_json():
    try:
        res = requests.get(raw_url,headers=headers)
        if res.ok:
            return res.json()
        else:
            print("访问失败")
            return False
    except Exception as e:
        print('错误如下:\n',e)

def json_parser(json):
    if json is not None:
        news_list = json.get('list')
        if not news_list:
            return False
        for news_item in news_list:
            #print(news_item)
            pic_url = news_item.get('pic')
            yield pic_url
    
def save_image(url):
    filename = url.lstrip('http://').replace('.','').replace('/','').rstrip('jpg')+'.jpg'
    '''
    try:
        res = requests.get(url,headers=headers)
        if res.ok:
            img = res.content
            if not os.path.exists(filename):
                with open(filename,'wb') as f:
                    f.write(img)
                    print('爬取成功')
    except Exception as e:
        print("保存失败")
        print(e)
    '''
    os.system("wget -P {} {} ".format('tupian/',url))

def worker():
    raw_json = get_json()
    #print(raw_json)
    urls = json_parser(raw_json)
    '''
    for url in urls:
        save_image(url)
    '''
    p = mp.Pool()
    p.map_async(save_image,urls)
    p.close()
    p.join()

if __name__ == '__main__':
    worker()
