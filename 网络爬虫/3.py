import time
import requests
import re
import os
headers={
       'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
response=requests.get('http://127.0.0.1/2.html',headers=headers)

# print(response.request.headers)
# print(response.text)
html=response.text

# 解析网页
# 目录名字
dir_name=re.findall('<img alt="(.*?)" width=".*?" height=".*?" >',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls=re.findall('<img alt=".*?" width=".*?" height=".*?">',html)
print(urls);

# 保存图片
for url in urls:
    # 加个延时,避免给服务器造成压力
    
    # 图片的名字
    file_name=url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(dir_name+'/'+file_name,'wb') as f:
        f.write(response.content)
