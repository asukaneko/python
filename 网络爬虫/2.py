import bs4,requests
from bs4 import BeautifulSoup
import os

url = "http://192.168.43.130:8888"
res = requests.get(url)
bs1 = BeautifulSoup(res.content)
links = bs1.find_all('a')
 
for link in links:
    #print(link)
    link = str(link)
    a = link.find('href=')
    b = link.find('>')
    link = link[a:b].replace('href=','').replace('"','')
    #print(link)
    link = 'http://192.168.43.130:8888/'+link
    os.system('wget -P /home/pi/shiyan {}'.format(link))
print("已完成")
