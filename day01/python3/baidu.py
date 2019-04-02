from urllib import request
import urllib.parse
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}
kw = input("请输入关键字:")
params = {
    'wd':kw
}

#将字段解析成参数字符串
params=urllib.parse.urlencode(params)
print(params)

#创建url
url = "http://www.baidu.com/s?"+params

#创建请求对象
requests=urllib.request.Request(url,headers=headers)
responses=urllib.request.urlopen(requests)

#print(responses.read().decode('utf-8'))
#print(responses.status)   #200
print(responses.__dict__)   #
