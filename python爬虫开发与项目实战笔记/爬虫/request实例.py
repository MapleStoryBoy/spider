import urllib.request


request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

'''
下面我们看一下 Request可以通过怎样的参数来构造，它的构造方法如下:
class urllib. request. Request (ur1, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None) 
第一个参数 url用于请求 URL， 这是必传参数，其他都是可选参数。
第二个参数 data 如果要传，必须传 bytes (字节流)类型的 。 如果它是字典，可以先用 urllib.parse模块里的 urlencode()编码。
第 三个参数 headers是一个字典，它就是请求头，我们可以在构造请求时通过 headers参数直 接构造，也可以通过调用请求实例的 add_header()方法添加。
添加请求头最常用的用法就是通过修改 User-Agent 来伪装浏览器，默认的 User-Agent 是 一’- Python-urllib，我们可以通过修改它来伪装浏览器 。 比如要伪装火狐浏览器，你可以把它设 E 置为 :
问ozilla/s.o (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11
第四个参数 origin_req_host指的是请求方的 host名称或者 IP地址。
第五个参数 unveri干iable表示这个请求是否是无法验证 的，默认是 False，意思就是说用户没
有足够权限来选择接收这个请求的结果。 例如，我们请求一个 HTML文档中的图片，但是我
们没有向动抓取图像的权限，这时 unverifiable 的值就是 True。
第六个参数 method是一个字符串 ，用来指示请求使用的方法，比如 GET、 POST和 PUT等。

'''