#获取cookies的过程
import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)

for key,value in r.cookies.items():
    print(key + '=' + value)




