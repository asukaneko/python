import requests

url = "https://www.wenku8.net/modules/article/articlelist.php"

cookies = "__51vcke__1xtyjOqSZ75DRXC0=f5fdf784-0b3e-5c91-8a2a-3714a39f2b22; __51vuft__1xtyjOqSZ75DRXC0=1727188190223; Hm_lvt_acfbfe93830e0272a88e1cc73d4d6d0f=1727187940,1728707458; __51uvsct__1xtyjOqSZ75DRXC0=3; Hm_lvt_d72896ddbf8d27c750e3b365ea2fc902=1728707439,1730868814,1731066009; HMACCOUNT=DF779BEB7EF70AC0; _clck=wliofh%7C2%7Cfqp%7C0%7C1728; PHPSESSID=e0cca5ab3b4c7dbd914598f4b4b16e2a; jieqiUserInfo=jieqiUserId%3D1107578%2CjieqiUserName%3Daska11%2CjieqiUserGroup%3D3%2CjieqiUserVip%3D0%2CjieqiUserName_un%3Daska11%2CjieqiUserHonor_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserGroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%3D1731066372%2CjieqiUserPassword%3Db00ac9a36735ea614cbe339e6a338195; jieqiVisitInfo=jieqiUserLogin%3D1731066372%2CjieqiUserId%3D1107578; Hm_lpvt_d72896ddbf8d27c750e3b365ea2fc902=1731067286; _clsk=6v606l%7C1731067287318%7C7%7C1%7Cn.clarity.ms%2Fcollect"
headers = {
    'authority':'www.wenku8.net',
    'method':'GET',
    'path':'/modules/article/articlelist.php',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'max-age=0',
    'Host':'https://www.wenku8.net/',
    'Referer':'https://www.wenku8.net/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.split('=',1)
    cookies_jar.set(key, value)

res = requests.get(url, headers=headers, cookies=cookies_jar)
print(res)
