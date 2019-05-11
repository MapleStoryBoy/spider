'''
是 URLError的子类，专门用来处理HTTP请求错误：
    code: 返回 HTTP状态码，比如 404表示网页不存在， 500表示服务器内部错误等
    reason:同父类一样，用于返回错误 的原因
    headers: 返回请求头。
'''

from urllib import request,error

try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,)