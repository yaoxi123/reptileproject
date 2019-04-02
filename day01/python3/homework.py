import json
import re
import urllib.request
headers = {
"User-Agent":"User-Agent,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"
}
for i in range(10):
    url="https://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize={}&t=0.38387847202622005".format(i)
    #print(url)
    requests = urllib.request.Request(url,headers=headers)
    responses = urllib.request.urlopen(requests)
    content = responses.read().decode()
    #print(content)
    data=json.loads(content)
    #print(datas)
    datas = data.get('returnValue')
    joblists = datas.get('datas')
    #print(joblists)
    #print(datas)
    for job in joblists:
        #print(job)

        degree = job['degree']
        # degree = job.get('degree')
        # print(degree)
        # break
        workexperience = job['workExperience']
        requirement = job['requirement']
        departmentname = job['departmentName']
        with open('ali.txt', 'a', encoding='utf8') as f:
            f.write("第{}条招聘信息:\n学历:{}\n部门:{}\n工作经验:{}\n岗位要求:{}".format(i+1,degree,departmentname,workexperience,requirement) + "\n")   #"\n"换行
            break
    print("第{}条数据抓取成功".format(i+1))
print("全部数据抓取完成")
