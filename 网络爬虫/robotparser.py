import urllib.robotparser as urobot
import requests

url = "http://{}".format(input("url:"))
rp = urobot.RobotFileParser()
rp.set_url(url + "/robots.txt")
rp.read()
user_agent = '{}'.format(input("user agent:"))
if rp.can_fetch(user_agent,url):
    site = requests.get(url)
    print("seems good")
else:
    print("cannot")
