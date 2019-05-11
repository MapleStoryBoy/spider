

import requests

data = {
    'name':'jsp',
    'age':23
}

r = requests.get('http://httpbin.org/get',params=data)
print(r.text)
'''
网页的返回类型实际上是 str类型，但是它很特殊，是 JSON格式的。
可以利用json（）直接解析返回结果
'''
print(r.json())
print(type(r.json()))









