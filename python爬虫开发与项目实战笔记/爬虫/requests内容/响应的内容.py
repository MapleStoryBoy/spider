import requests
r = requests.get('http://www.jianshu.com')
print(type(r.status_code), r.status_code)
print(type(r. headers), r. headers)
print (type(r. cookies), r. cookies)
print(type(r. url), r. url)
print(type(r.history), r.history)
'''
我们使用 text 和 content 获取了 响应的内 容。 此外，还有
很多属性和方法可以用来获取其他信息，比如状态码、响应头、 Cookies等
状态码常用来判断请求是否成功，而 requests还提供了一个内置的状态码查询对象 requests.codes,
'''
#r = requests.get('http://www.jianshu.com')
#exit() if not r.status_code == requests.codes.ok else print('Request Success于ully')