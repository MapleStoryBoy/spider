# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sina.items import SinaItem


class SinaSpiderSpider(CrawlSpider):
    name = 'sina_spider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        categories = response.xpath("//div[@id='tab01']/div")
        # 最后一个是城市的，不爬取了
        categories.pop()
        for category in categories:
            main_name = category.xpath(".//a/text()").extract_first()
            sublis = category.xpath(".//ul/li")
            for li in sublis:
                sub_name = li.xpath(".//a/@href").extract_first()
                sub_url = li.xpath(".//a/text()").extract_first()
                item = SinaItem(main_name=main_name,sub_name=sub_name)
                yield scrapy.Request(url=sub_url,meta={"item":item},callback=self.parse_sub_page)

    def parse_sub_page(self,response):
        meta_item = response.meta.get("item")
        a_list = response.xpath("//a/@href")
        for a in a_list:
            if a.endswith(".shtml"):
                yield scrapy.Request(a,meta={"item":meta_item},callback=self.parse_detail_page)


    def parse_detail_page(self,response):
        pass



