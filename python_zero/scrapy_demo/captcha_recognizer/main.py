#encoding: utf-8

from urllib import request
from base64 import b64encode
import requests

captcha_url = 'https://www.douban.com/misc/captcha?id=yxlOex0dffk3sgHjncMOvFNY:en&size=s'
request.urlretrieve(captcha_url,'captcha.png')

recognize_url = 'http://jisuyzmsb.market.alicloudapi.com/captcha/recognize?type=e'

formdata = {}
with open('captcha.png','rb') as fp:
    data = fp.read()
    pic = b64encode(data)
    formdata['pic'] = pic

appcode = '831a890b2cfe4ea0a8e345078434ebfc'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}

response = requests.post(recognize_url,data=formdata,headers=headers)
result = response.json()
code = result['result']['code']
print(code)
