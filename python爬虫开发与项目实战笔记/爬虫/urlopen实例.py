import urllib.request
import urllib.parse
response= urllib.request.urlopen('https://www.python.org') 
#print(response. read(). decode (' utf-8'))
print(type(response))
#它是一个 HTTPResposne类型的对象，主要包含 read()、 readinto()、 getheader(name)、
#getheaders()、 fileno()等方法，以及 msg、 version、 status、 reason、 debuglevel、 ιlosed等属性。
print(response . status)
print(response .getheaders())
print(response . getheader ('Server'))

#data参数
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())




