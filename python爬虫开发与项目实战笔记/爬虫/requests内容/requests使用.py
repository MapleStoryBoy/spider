'''
调用 get()方法实现与 urlopen()相同的操作，得到一个 Response 对象，
然后分别输出 了 Response 的类型、状态码、响应体的类型、内容 以及 Cookies。
'''

import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)




