# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"
        data = {"email": "970138074@qq.com", 'password': "pythonspider"}
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)
        yield request


    def parse_page(self,response):
        request = scrapy.Request(url='http://www.renren.com/880151247/profile',callback=self.parse_profile)
        yield request

    def parse_profile(self,response):
        with open('dp.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
