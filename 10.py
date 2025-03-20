import requests,os
from bs4 import BeautifulSoup
import datetime,time,random

headers={
       'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}

ha = datetime.date.today()
t = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
n = 20000
h = requests.get("http://pic.netbian.com/tupian/{}.html".format(n),headers=headers)
bs1 = BeautifulSoup(h.content,'html.parser')
imgs = bs1.find_all("img")
while True:
    
    for img in imgs:
        #print(img)
        
        img = str(img)
        d = img.find('src=')
        e = img.find('title=')
        img = "http://pic.netbian.com" + img[d:e].replace('src=','').replace('"','')[:-1]
        print(img)
        # time.sleep(random.choice(t))
        os.system("wget -P /home/pi/Documents/tupian/{} {} ".format(ha,img))
    
    print("这是第{}页".format(n))
    n += 1   
    h = requests.get("http://pic.netbian.com/tupian/{}.html".format(n))
    bs1 = BeautifulSoup(h.content,'html.parser')
    imgs = bs1.find_all("img")
    
    
    
print("Ok!")
