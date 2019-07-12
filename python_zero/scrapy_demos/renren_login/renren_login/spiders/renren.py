# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        formdata = {
            'email': '970138074@qq.com',
            'password': 'pythonspider'
        }
        request = scrapy.FormRequest(url,formdata=formdata,callback=self.parse_page)
        yield request

    def parse_page(self,response):
        yield scrapy.Request("http://www.renren.com/880151247/profile",callback=self.parse_dp)

    def parse_dp(self,response):
        with open('dp.html','w',encoding='utf-8') as fp:
            fp.write(response.text)