#encoding: utf-8

from urllib import request

# 没有使用代理的
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())

# 使用代理的
url = 'http://httpbin.org/ip'
# 1. 使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({"http":"223.241.78.43:8010"})
# 2. 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3. 使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())