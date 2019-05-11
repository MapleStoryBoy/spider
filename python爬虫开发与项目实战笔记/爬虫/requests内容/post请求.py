

import requests

data = {'name':'jsp','age':'23'}
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)



