'''
urllib库里还提供了parse模块，它定义了处理URL的标准接口，例如实现URL各部 分的抽取、合并以及链接转换 。
 它支持如下协议的 URL 处理:file、ftp、 gopher、 hdl、 http、 https、 imap、 m a i l to 、 mms 、
  news 、 nntp 、 prospero 、 rsync 、 rtsp 、 rtspu 、 sftp 、 sip 、 sips 、 snews 、 svn 、
   svn+ssh 、 telnet 和 wais
'''
# urlparse()实现 URL 的识别和分段,对立方法urlunparse

from urllib.parse import urlparse,urlunparse,urlsplit,urlunsplit

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
# urlunparse()
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))

#urlsplit
result1 = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result1)
#urlunsplit
data2 = ['http','www.baidu.com','index.html','user','a=6']
print(urlunsplit(data2))

#urljoin()方法
