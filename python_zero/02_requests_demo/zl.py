#encoding: utf-8
import requests

def renren():
    url = "http://www.renren.com/PLogin.do"
    data = {"email": "970138074@qq.com", 'password': "pythonspider"}
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    # 登录
    session = requests.session()
    session.post(url, data=data, headers=headers)

    # 访问大鹏个人中心
    resp = session.get('http://www.renren.com/880151247/profile')

    print(resp.text)