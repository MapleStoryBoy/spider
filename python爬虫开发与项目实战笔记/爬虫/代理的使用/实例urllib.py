from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

proxy = '123.169.37.151'
proxy_handler = ProxyHandler({
    'http':'http://' + proxy,
    'https':'https://' + proxy
})

opener = build_opener(proxy_handler)

try:
    response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)