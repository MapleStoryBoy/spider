'''
requests 提供了 一个更简单的写法 ，可以直接传一个元组，
它会默认使用 HTTPBasicAuth 这个类来认证 。
requests还提供了其他认证方式，如 OAuth认证，不过此时需要安装 oauth包
pip3 install requests_oauthlib
'''
import requests
from requests.auth import HTTPBasicAuth
r = requests.get('http://localhost:5000',auth=('username','password'))
#r = requests.get('http://localhost:5000',auth=HTTPBasicAuth('username','password'))
print(r.status_code)


