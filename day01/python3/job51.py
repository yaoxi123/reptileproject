import re
import urllib.request
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}
url="https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

#抓取数据  创建请求对象
req = urllib.request.Request(url,headers=headers)

#获取服务器响应数据
response = urllib.request.urlopen(req)

#print(response)  #<http.client.HTTPResponse object at 0x0000000002DB9978>

#解码
html = response.read().decode("gbk")
# print(html)  #整个页面

#处理数据 拿到标签中间所有你内容
# (.*?)所有内容包括空格
jobnum_re = '<div class="rt">(.*?)</div>'
# re.S  #匹配任意非空白字符
coms = re.compile(jobnum_re,re.S)
strs = coms.findall(html)[0]
#print(strs)  # 共36685条职位

#取出存数字
num_re = ".*?(\d+).*"
num = re.findall(num_re,strs)
#print(num)    #['36685']
#print(int(num[0]))    #36685

#获取第一个岗位信息
jobname_re = '<div class="el">(.*?)</div>'
joblist = re.findall(jobname_re,html,re.S)
#print(joblist[0])
#print(joblist)

for job in joblist:
    jobnameone_re = 'onmousedown="">(.*?)</a>'
    jobnameone_list = re.findall(jobnameone_re,job,re.S)
    print(jobnameone_list)