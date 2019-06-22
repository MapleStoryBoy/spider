# -*- coding: utf-8 -*-
import scrapy
from SNBook.items import SnbookItem
import re


class SnBookSpider(scrapy.Spider):
    name = 'sn_book'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='ulwrap']/li")
        for li in li_list:
            item = SnbookItem()
            item['parent_type'] = li.xpath(".//a/text()").extract_first()
            item['parent_href'] = li.xpath(".//a/@href").extract_first()
            item['parent_href'] = 'http://snbook.suning.com' + item['parent_href']
            item['son_type'] = li.xpath(".//div[@class='three-sort']//text()").extract()
            item['son_href'] = li.xpath(".//div[@class='three-sort']//@href").extract()
            item['son_href'] = ['http://snbook.suning.com' + i for i in item['son_href']]

            yield scrapy.Request(item['son_href'],
                                 callback=self.parse_son_type,
                                 meta={'item': item})

    def parse_son_type(self, response):
        item = response.meta['item']
        li_list = response.xpath("//ul[@class='clearfix']/li")
        pattern = re.compile(r'pagecount=(\d+);')
        pagecount = pattern.findall(response.body.decode())[0]  # 子类图书总页数
        item['pagecount'] = pagecount
        for li in li_list:
            item['belong_son_tyoe'] = li.xpath(".//a[@class='ci']/text()").extract_first()  # 所属子类没取到
            item['book_href'] = li.xpath("./div[1]/a/@href").extract_first()
            item['book_img'] = li.xpath("./div[1]/a/img/@src").extract_first()  # 图片没取到
            item['book_name'] = li.xpath("./div[1]/a/img/@alt").extract_first()
            item['book_author'] = li.xpath("./div[2]//div[@class='book-author']/a/text()").extract_first()
            item['book_descrip'] = li.xpath("./div[2]//div[@class='book-descrip c6']/text()").extract()
            # print(item)
            #TODO 价格
            yield item
        # next_url = 'javascript:turnpage(下一页的页码);'  # ???不用selenium怎么到下一页
        #TODO 翻页
















