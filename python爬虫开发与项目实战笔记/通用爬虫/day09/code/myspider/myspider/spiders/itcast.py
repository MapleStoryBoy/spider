# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item = {}
            item["come_from"] =  "itcast"
            logger.warning(item)
            yield item
