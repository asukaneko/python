from bs4 import BeautifulSoup
import requests
headers = {
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1'
}
def get_urls(url):
    urls=[]
    res=requests.get(url)
    if res.ok:
        bs=BeautifulSoup(res.content,"html.parser")
        herfs=bs.find_all('a')
        for herf in herfs:
            print(herf)
            print("-------")
            
def worker():
    get_urls("https://www.pixiv.net/ranking.php")


if __name__=='__main__':
    worker()
