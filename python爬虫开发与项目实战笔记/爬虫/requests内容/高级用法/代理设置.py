'''
设置代理解决大规 模且频繁的请求，网站可能会弹出验证码，或者跳转到登录认证页面，
 更甚者可能会直接封禁客户端 的 IP，导致一定时间段内无法访问 的问题。
 proxies参数
'''
import requests

proxies = {
    'http':'http://120.210.219.105:80',
    'https':'https://120.210.219.104:80'
}

requests.get('https://www.taobao.com',proxies=proxies)
'''
若代理需要使用 HTTP Basic Auth，可以使用类似 
http://user:password@host:port这样的语法来设 置代理，
除了基本的 HTTP代理外， requests还支持 SOCKS协议的代理。
首先，需要安装 socks这个库 : pip3 install 'requests[socks ]'
'''
'''

import requests
proxies = {
    'http': ' sockss://user:password@host:port',
    'https':'sockss://user:password@host:port'
}
requests.get('https://www.taobao.com',proxies=proxies)


'''
#超市设置，只需要在get里面设置一个timeout参数