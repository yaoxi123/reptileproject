# -*- coding:utf-8 -*-
import urllib
from urllib import request
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}

url='http://www.baidu.com/'

#创建请求对象
req = urllib.request.Request(url,headers=headers)

#发送请求获取响应
responses = urllib.request.urlopen(req)
print(responses)
print(responses.read().decode('utf-8'))  #解码

