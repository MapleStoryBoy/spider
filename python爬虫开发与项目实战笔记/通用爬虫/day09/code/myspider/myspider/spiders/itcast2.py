# -*- coding: utf-8 -*-
import scrapy


class Itcast2Spider(scrapy.Spider):
    name = 'itcast2'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass
