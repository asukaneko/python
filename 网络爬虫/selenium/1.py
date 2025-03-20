from selenium import webdriver
import time

browser = webdriver.Chrome("/usr/bin/chromium")
browser.get("http:www.bilibili.com")
print(browser.title)
time.sleep(10)
browser.quit()