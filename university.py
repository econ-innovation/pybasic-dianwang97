
# 准备好985大学的名单 985university.txt 文件

# 开始使用高德地图的key按学校名称进行搜索坐标点
import json
import requests # 无法pip安装就去解析器里面手动安装一下

def get_geo(University):
    key = '75f3c8650855fe5372f3fe79761265df'
    url = f"https://restapi.amap.com/v3/geocode/geo?address={University}&output=json&key={key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['geocodes'][0]['location']

with open("./985university.txt","r") as f:
    for l in f.readlines():
        university = l.strip() # 去除可能的空格和换行符
        location = get_geo(university)
        with open('./985location.txt', 'a') as fs:
            fs.write("{1}{0}{2}\n".format("|",university, location))


