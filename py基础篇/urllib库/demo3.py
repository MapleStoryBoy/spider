#encoding: utf-8

from urllib import request,parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# resp = request.urlopen(url)
# print(resp.read())


url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

req = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))