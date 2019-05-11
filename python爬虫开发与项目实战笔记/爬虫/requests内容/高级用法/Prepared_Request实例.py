'''
我们可以将请求表示为数据结构，其中各个参数都可以通过一个 Request 对 象来表示 。
 这在 requests里同样可以做到，这个数据结构就叫 Prepared Request。

'''
from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'jsp'
}

headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)'
}

s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r =s.send(prepped)
print(r.text)

'''
有了Request这个对象，就可以将请求当作独立的对像来看待。
'''
