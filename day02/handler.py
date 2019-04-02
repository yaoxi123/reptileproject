import urllib.request

#创建处理器对象
http=urllib.request.HTTPHandler()    #支持http
# https = urllib.request.HTTPHandler()

#使用调用方法使用对象 创建打开器对象
opener=urllib.request.build_opener(http)

#打开URL
response = opener.open("http://www.baidu.com")
print(response.read().decode())

#创建全局打开器
urllib.request.install_opener(opener)   #使用全局打开器
