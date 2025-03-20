#删除文件中多余的内容
import os
from bs4 import BeautifulSoup
from html import unescape

for filename in os.listdir('.'):
    if not filename.endswith('.txt'):
        continue
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        content = str(content)
        #content = content[170:-98]
        soup = BeautifulSoup(unescape(content), 'lxml')
        content = soup.text
        content.replace('>','')
    with open(filename, 'w', encoding='utf-8', errors='ignore') as f:
        f.write(content)
    print(filename+"已处理")


