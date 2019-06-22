# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
data = {
    "from":"en",
    "to":"zh",
    "query":"hola",
    "transtype":"translang",
    "simple_means_flag":"3",
    "sign":"372549.85108",
    "token":"e89a8f037aac1b51a86cbc82356949d"
}
post_url = "http://fanyi.baidu.com/v2transapi"

r = requests.post(post_url,data=data,headers=headers)
print(r.content.decode())
