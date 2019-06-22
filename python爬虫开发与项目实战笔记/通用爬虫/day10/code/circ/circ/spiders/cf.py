# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://www.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    #定义提取url地址规则
    rules = (
        #LinkExtractor 连接提取器，提取url地址
        #callback 提取出来的url地址的response会交给callback处理
        #follow 当前url地址的响应是够重新进过rules来提取url地址，
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'),follow=True),
    )

    #parse函数有特殊功能，不能定义
    def parse_item(self, response):
        item = {}
        item["title"] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->",response.body.decode())[0]
        item["publish_date"] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})",response.body.decode())[0]
        print(item)
    #     yield scrapy.Request(
    #         url,
    #         callback=self.parse_detail,
    #         meta = {"item":item}
    #     )
    #
    # def parse_detail(self,response):
    #     item = response.meta["item"]
    #     item["price"] =  "///"
    #     yield item
