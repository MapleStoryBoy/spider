
# 借助HTTPBasucAuthHandler

from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError


username = 'username'
password = 'password'
url = 'http://localhost:5000/'

p = HTTPPasswordMgrWithDefaultRealm()
#利用 add_password()添加进去用户名和密码，这样就建立了一个处理验证的 Handler
p.add_password(None,url,username,password)
#实例化 HTTPBasicAuthHandler对象
auth_handler = HTTPBasicAuthHandler(p)
#构建opener
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)






