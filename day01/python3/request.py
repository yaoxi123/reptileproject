import urllib
from urllib import request
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}

url ="http://www.baidu.com"

#创建请求对象
req = urllib.request.Request(url,headers=headers)
#发送请求获取响应
responses = urllib.request.urlopen(req)
#print(responses)   #二进制数据<http.client.HTTPResponse object at 0x0000000002DBAE48>

print(responses.read().decode('utf-8'))    #解码

#字符串》》 字节   encode
#字节 》》 字符串  decode
