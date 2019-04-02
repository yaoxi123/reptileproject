import urllib.request

#第一个参数是要下载的URL   第二个参数  文件存放的路径
#request.urlretrieve("http://www.so.com",r"baidu.html")

urllib.request.urlretrieve("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554129177484&di=b8034e7f903bb3e95e545017ac28e863&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F16%2F14%2F80%2F91J58PICzdA_1024.jpg",r"图片.jpg")

# strings = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&srcqid=2982980266031548955&tn=50000021_hao_pg&wd=%E9%A3%8E%E6%99%AF%E8%83%8C%E6%99%AF%E5%9B%BE&oq=%25E8%2583%258C%25E6%2599%25AF%25E5%259B%25BE&rsv_pq=94cfab9f0003e850&rsv_t=60a1kitlu4FpaaYRDABWoZgFyIaQI0T1FeTKR8dchvU2LRwKaxvuEOLyGbciU25oZRXRySb1&rqlang=cn&rsv_enter=1&rsv_sug3=8&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&inputT=3757&rsv_sug4=8792"
# print(urllib.parse.quote(strings))

strings="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&srcqid=2982980266031548955&tn=50000021_hao_pg&wd=%E9%A3%8E%E6%99%AF%E8%83%8C%E6%99%AF%E5%9B%BE&oq=%25E8%2583%258C%25E6%2599%25AF%25E5%259B%25BE&rsv_pq=94cfab9f0003e850&rsv_t=60a1kitlu4FpaaYRDABWoZgFyIaQI0T1FeTKR8dchvU2LRwKaxvuEOLyGbciU25oZRXRySb1&rqlang=cn&rsv_enter=1&rsv_sug3=8&rsv_sug1=3&rsv_sug7=100&rsv_sug2=0&inputT=3757&rsv_sug4=8792"
print(urllib.parse.quote(strings))