'''
文件上传
'''
import requests


files = {'file':open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)
'''
这个网站会返回响应，里面包含 files 这个字段，而 form 字段是空 的，
这证 明文件上传部分会单独有一个 files字段来标识。
'''