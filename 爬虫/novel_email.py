from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re
from bs4 import BeautifulSoup
import sendEmail
edge_options = Options()
#edge_options.add_argument("--headless")

service = Service('edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service, options=edge_options)
driver.get("https://www.wenku8.net/modules/article/articlelist.php")

purls = []
for i in range(2,187):
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

def save(res,name):
    urls = []
    for i in range(1,4):
        urls.append("https://dl1.wenku8.com/down/txtgbk/{}/{}.txt".format(i,int(res)))
    for url in urls:
        driver.get(url)
        text = driver.page_source
        if "404 Not Found" in text:
            continue
        text=str(text)
        sendEmail.sendEmail("2645229359@qq.com",text,name)
        print(name+","+"OK")


def geturl():
    res = driver.page_source
    bs = BeautifulSoup(res, 'html.parser')
    hrefs = bs.find_all('a')
    #print(hrefs)
    pattern = r'/book/\d{4}\.htm'
    pa2 = r'tiptitle="[\u4e00-\u9fff]+"'
    urls = []
    names = []
    for href in hrefs:
        href = str(href)
        #print(href)
        url = re.findall(pattern,href)
        name = re.findall(pa2,href)
        if len(url) == 0:
            continue
        if len(name) == 0:
            continue
        #print(name[0][10:-1])
        names.append(name[0][10:-1])
        urls.append(url[0][6:-4])
    urls = list(set(urls))
    names = list(set(names))
    #print(urls)
    for url,name in zip(urls,names):
        save(url,name)

    #print(urls)

geturl()
for purl in purls:
    driver.get(purl)
    geturl()

#这个代码用于下载轻小说文库的轻小说并将其发送到指定邮箱