#encoding: utf-8

from urllib import request
from base64 import b64encode
import requests

captcha_url = 'https://www.douban.com/misc/captcha?id=bfOLE7WNLcqoCTFKRop1PTiT:en&size=s'
request.urlretrieve(captcha_url,'captcha.png')

recognize_url = 'http://jisuyzmsb.market.alicloudapi.com/captcha/recognize?type=e'

formdata = {}
with open('captcha.png','rb') as fp:
    data = fp.read()
    formdata['pic'] = b64encode(data)
appcode = '831a890b2cfe4ea0a8e345078434ebfc'
headers = {
    'Authorization': 'APPCODE ' + appcode,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

response = requests.post(recognize_url,data=formdata,headers=headers)
result = response.json()
captcha = result['result']['code']
print(captcha)



