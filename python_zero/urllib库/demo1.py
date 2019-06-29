#encoding: utf-8


from urllib import request
from urllib import parse

# urlretrieve函数的用法
# request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1511283869079&di=da3892a20ff8b4d535152e303f0c9ae6&imgtype=0&src=http%3A%2F%2Fi2.17173cdn.com%2F2fhnvk%2FYWxqaGBf%2Fcms3%2FESweDEbleCrnwrx.jpg','luban.jpg')

# urlencode函数的用法
# params = {'name':'张三',"age":18,'greet':'hello world'}
# result = parse.urlencode(params)
# print(result)


# url = 'http://www.baidu.com/s'
# params = {"wd":"刘德华"}
# qs = parse.urlencode(params)
# url = url + "?" + qs
# resp = request.urlopen(url)
# print(resp.read())


# parse_qs函数的用法
# params = {'name':'张三',"age":18,'greet':'hello world'}
# qs = parse.urlencode(params)
# print(qs)
# result = parse.parse_qs(qs)
# print(result)

