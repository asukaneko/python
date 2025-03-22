from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re,os
from bs4 import BeautifulSoup

edge_options = Options()
#edge_options.add_argument("--headless")
download_dir = "E:\\document"
dir = r"C:\Users\ycssb\Downloads"
edge_options.add_argument("--download.default_directory=" + download_dir)

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

service = Service('edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service, options=edge_options)
driver.get("https://www.wenku8.net/modules/article/articlelist.php")

purls = []
for i in range(2,191):
    purls.append("https://www.wenku8.net/modules/article/articlelist.php?page={}".format(i))
# 等待页面加载
wait = WebDriverWait(driver, 5)
email_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

# 输入文本
email_field.send_keys("ycssbc@126.com")
password_field.send_keys('yc123456')

# 点击登录按钮
login_button = driver.find_element(By.NAME, 'submit')
login_button.click()

time.sleep(8)

names = []
urls = []

rest_names = []
rest_urls = []

def save(res,name):
    url=f"https://dl.wenku8.com/down.php?type=txt&node=1&id={res}"
    driver.get(url)
    names.append(name)
    urls.append(res)
    time.sleep(5)

def rename(res,name):
    try:
        os.rename(f"{dir}\\{res}.txt",f"{dir}\\{name}.txt")
        print(f'{res}.txt ---> {name}.txt')
    except FileExistsError:
        print(f'文件 {name} 已存在，跳过')
    except PermissionError:
        print(f'文件 {name} 被占用，无法重命名')
    except FileNotFoundError:
        print(f'文件 {name} 不存在，无法重命名')
        rest_names.append(name)
        rest_urls.append(res)
    except Exception as e:
        print(f'处理 {name} 时发生意外错误：{str(e)}')


def geturl():
    res = driver.page_source
    bs = BeautifulSoup(res, 'html.parser')
    hrefs = bs.find_all('a')
    #print(hrefs)
    pattern = r'/book/\d+\.htm'
    pa2 = r'tiptitle="[^"]+"'
    urls = []
    names = []
    for href in hrefs:
        href = str(href)
        url = re.findall(pattern,href)
        name = re.findall(pa2,href)
        # 检查是否找到匹配项
        if not url or not name:
            continue
        # 确保匹配项不为空
        if len(url[0]) == 0 or len(name[0]) == 0:
            continue
        names.append(name[0][10:-1])
        urls.append(url[0][6:-4])
    urls = list(dict.fromkeys(urls))
    names = list(dict.fromkeys(names))
    for url,name in zip(urls,names):
        save(url,name)

geturl()
for purl in purls:
    driver.get(purl)
    geturl()

for url,name in zip(urls,names):
    rename(url,name)

for url,name in zip(rest_urls,rest_names):
    save(url,name)
for url,name in zip(rest_urls,rest_names):
    rename(url,name)
#这个代码用于下载轻小说文库的轻小说
#第二版，轻小说文库更新了下载规则，原版已不再有效