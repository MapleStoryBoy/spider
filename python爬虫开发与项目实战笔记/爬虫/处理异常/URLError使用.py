'''
URLError类来自 urllib库的 error模块，它继承自 OSError类，是 error异常模块的基类，
由 request 模块生的异常都可以通过捕获这个类来处理 。
'''

from urllib import request,error

try:
    response = request.urlopen('https://cuiqingcai.com/index.html')
except error.URLError as e:
    print(e.reason)