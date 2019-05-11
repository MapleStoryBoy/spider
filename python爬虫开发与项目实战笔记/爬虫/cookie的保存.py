

import http.cookiejar,urllib.request

filename = 'cookies.txt'
#MozillaCookieJar格式
#cookie = http.cookiejar.MozillaCookieJar(filename)
# lwp格式
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)



