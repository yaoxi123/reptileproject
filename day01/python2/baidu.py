# -*- coding:utf-8 -*-
import urllib
import urllib2
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}

url = "http://www.baidu.com/"
res = urllib2.Request(url,headers=headers)
#获取完整的url
print res.get_full_url()    #http://www.baidu.com/
#获取请求方法
print res.get_method()   #GET
#获取浏览器名称
print res.get_header("User-agent")   #User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36
#host名称
print res.get_host()   #www.baidu.com
#协议名称
print res.get_type()   #http

#header 头中添加请求信息
res.add_header("Connection","keep-alive")
print res.get_header("Connection")   #keep-alive