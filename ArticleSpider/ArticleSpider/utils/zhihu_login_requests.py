import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

def get_xsrf():
    response = requests.get("https://www.zhihu.com")
    print(response.text)
    return " "

def zhihu_login(account,password):
    #知乎登录
    if re.match("r1\d{10]",account):
        print("手机号码登录")
        post_url = "https://www.zhihu.com/signin"
        post_data = {
            "_xsrf":get_xsrf,
            "phone_num":account,
            "password":password
        }