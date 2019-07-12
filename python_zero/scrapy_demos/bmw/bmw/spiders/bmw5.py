# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bmw.items import BmwItem

class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65-.+'), callback='parse_pic', follow=False),
    )

    def parse_pic(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").extract_first()
        srcs = response.xpath("//div[contains(@class,'uibox-con carpic-list03')]//li//img/@src").extract()
        for src in srcs:
            src = src.replace("/t_","/1024x0_1_q87_")
            image_url = "https:"+src
            yield BmwItem(category=category,image_urls=[image_url],page_url=response.url)
