import urllib.request
from http import cookiejar

#创建文件   保存cookie
filename = "baidu.txt"

#创建cookiejar 对象跟文件交互一般用LWPCookieJar
cookie=cookiejar.LWPCookieJar(filename=filename)

#创建cookie 处理器
handler = urllib.request.build_opener()