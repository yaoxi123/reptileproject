import re
import urllib.request
import time

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示：
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

def getData(url):
    headers = {
        "User-Agent": "User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    #print(html)
    regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
    regs = regCom.findall(html)
    #print(regs)
    for reg in regs:
        #print(reg)
        nameCom = re.compile('<h2>(.*?)</h2>', re.S)
        name=nameCom.findall(reg)[0]
        #print(name)
        contentCom = re.compile('<span>(.*?)</span>', re.S)
        content = contentCom.findall(reg)[0]
        #print(content)
        print("{}说:{}".format(name.strip(),content.strip()))



if __name__ == "__main__":

    # 所有数据
    #allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # 遍历每一页的数据
    for i in range(1, 2):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        #allData.extend(list1)

        time.sleep(0.5)
    # 遍历allData 把数据显示
    #for dict1 in allData:
        #print("%s 说： %s" % (dict1["name1"], dict1["content"]))




