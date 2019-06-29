#encoding: utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies')
for cookie in cookiejar:
    print(cookie)

# cookiejar.save(ignore_discard=True)