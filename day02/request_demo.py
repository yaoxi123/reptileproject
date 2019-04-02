import requests

#get 请求
responses=requests.get('http://www.qfedu.com/')
print(responses)   #<Response [200]>
print(responses.status_code)  #200
print(responses.url)    #http://www.qfedu.com/
print(responses.encoding)  #ISO-8859-1
print(responses.cookies)   #<RequestsCookieJar[]>
#print(responses.text)    #字符串
print(type(responses.text))  #<class 'str'>
#print(responses.content)   #响应数据二进制
print(responses.content.decode())