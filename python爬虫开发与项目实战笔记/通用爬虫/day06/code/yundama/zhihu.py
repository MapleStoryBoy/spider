# coding=utf-8
import requests
from lxml import etree
from dama import indetify
import time

class ZhihuSpider:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    def login(self):
        html = self.session.get('https://www.zhihu.com/#signin', headers=self.headers).content
        html = etree.HTML(html)
        _xsrf = html.xpath("//input[@name='_xsrf']/@value")[0]
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
        captcha_response = self.session.get(captcha_url,headers=self.headers)
        with open("temp.gif","wb") as f:
            f.write(captcha_response.content)
        captcha = indetify(captcha_response.content)
        post_data = {
            "_xsrf": _xsrf,
            "email": "***",
            "password": "***",
            "remember_me": True,
            "captcha": captcha
        }
        print(post_data)
        resp = self.session.post('https://www.zhihu.com/login/email', data=post_data, headers=self.headers)
        print(resp.status_code)
        print(resp.content.decode())
        resposne = self.session.get("https://www.zhihu.com/",headers=self.headers)

        with open("login.html","w",encoding="utf-8") as f:
            f.write(resposne.content.decode())

if __name__ == '__main__':
    zhihu = ZhihuSpider()
    zhihu.login()