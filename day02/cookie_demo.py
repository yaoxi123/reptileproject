import urllib.request
from http import cookiejar

#创建cookiejar对象用来管理cookie
cookies=cookiejar.CookieJar()

#创建cookie处理器
cookie_handler=urllib.request.HTTPCookieProcessor(cookies)

#创建opener打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}

url = "http://www.baidu.com"
req=urllib.request.Request(url,headers=headers)
response = opener.open(req)
#print(response.read().decode())
#print(cookies)   #百度cookie

for cookie in cookies:
    print(cookie.name)
    #print(cookie.value)