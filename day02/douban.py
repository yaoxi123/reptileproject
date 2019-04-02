# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"
import urllib.request
from http import cookiejar

cookies = cookiejar.CookieJar()
# 创建cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
# 创建opener打开器
opener = urllib.request.build_opener(cookie_handler)

def getData(url):
    headers = {
        "User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = opener.open(req)
    print(response.read().decode())



if __name__ == "__main__":

    for i in range(1, 3):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i * 20) + "&limit=20"
        getData(url)
