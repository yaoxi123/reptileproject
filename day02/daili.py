import random
import urllib.request
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}

proxy = {
    'http':"http://123.207.215.186:8118"
}
# ip_list = [
#     {},
#     {},
#     {},
# ]

#设置代理服务器
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)

#创建打开服务器
opener = urllib.request.build_opener(proxy_handler)

url = "http://www.ifeng.com/"

req = urllib.request.Request(url=url,headers=headers)
response = opener.open(req)
print(response.read().decode())