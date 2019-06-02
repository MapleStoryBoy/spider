import requests
import json


headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

post_data = {
    "query":"人生苦短，我用python",
    "from":"zh",
    "to" : "en"
}
post_url = "https://fanyi.baidu.com"

r = requests.post(post_url,data=post_data,headers=headers)
print(r.content.decode())

