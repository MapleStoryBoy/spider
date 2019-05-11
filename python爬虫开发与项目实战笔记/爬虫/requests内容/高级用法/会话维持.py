'''
利用Session对象
利用 Session，可以做到模拟同一个会话而不用担心 Cookies的问题。 它通常用于模拟登录
成功之后再进行下一步的操作 。可以用于模拟在同一个浏览器中打开同一个网站的不同页面
'''
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
