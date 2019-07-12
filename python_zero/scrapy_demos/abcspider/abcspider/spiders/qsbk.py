# -*- coding: utf-8 -*-
import scrapy
from abcspider.items import QsbkItem

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    base_domain = 'https://www.qiushibaike.com'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        outerbox = response.xpath("//div[@id='content-left']/div")
        for box in outerbox:
            author = box.xpath(".//div[contains(@class,'author')]//h2/text()").extract_first().strip()
            content = box.xpath(".//div[@class='content']/span/text()").extract_first().strip()
            item = QsbkItem()
            item["author"] = author
            item["content"] = content
            yield item
        # 遍历下一页的请求
            next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").extract_first()
            # print(self.base_domain+next_url)
            if next_url:
                yield scrapy.Request(self.base_domain+next_url)
