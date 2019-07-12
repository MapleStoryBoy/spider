#encoding: utf-8
import requests
from urllib import request
from base64 import b64encode

def recognize_captcha(image_url):
    # 发送一个网络请求
    request.urlretrieve(image_url,'captcha.png')
    pic = None
    with open('captcha.png','rb') as fp:
        data = fp.read()
        pic = b64encode(data)
    data = {
        'pic': pic
    }
    appcode = '831a890b2cfe4ea0a8e345078434ebfc'
    headers = {
        'Authorization': 'APPCODE ' + appcode,
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
    }
    recognize_url = "http://jisuyzmsb.market.alicloudapi.com/captcha/recognize?type=e"
    print()
    response = requests.post(recognize_url, data=data, headers=headers)
    print(response.json())


recognize_captcha('https://www.douban.com/misc/captcha?id=l3BBALs9oTgc6H8ZQ2DRGo9w:en&size=s')