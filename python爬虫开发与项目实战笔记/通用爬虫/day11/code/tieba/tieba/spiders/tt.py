# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'),follow=True),
    )

    def parse_item(self, response):
        item = {}
        item["title"] = response.xpath("//td[@id='sharetitle']/text()").extract_first()
        item["aquire"] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        # return i
        print(item)