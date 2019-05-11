'''
首先 ，我们必须声明一个 CookieJar对象。 接下来，就需要利用 HTTPCookieProcessor来构建一个
Handler，最后利用 build_opener()方法构建出 Opener，执行 open()函数即可 。
'''
import http.cookiejar,urllib.request


cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')

for item in cookie:
    print(item.name + '=' + item.value)