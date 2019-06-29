#encoding: utf-8


import requests

proxy = {
    'http': '123.54.194.96:38661'
}

response = requests.get("http://httpbin.org/ip",proxies=proxy)
print(response.text)