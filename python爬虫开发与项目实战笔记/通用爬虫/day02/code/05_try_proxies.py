# coding=utf-8
import requests


proxies = {"http":"http://163.177.151.23:80"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.status_code)