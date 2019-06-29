#encoding: utf-8

from urllib import parse

url = 'http://www.baidu.com/s?wd=python&username=abc#1'

result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)

print(result1)
print(result2)
# print('scheme:',result.scheme)
# print('netloc:',result.netloc)
# print('path:',result.path)
# # print('params:',result.params)
# print('query:',result.query)
# print('fragment:',result.fragment)