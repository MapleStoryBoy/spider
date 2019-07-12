# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BmwItem(scrapy.Item):
    # 必须为一个列表
    image_urls = scrapy.Field()
    # 下载完成后存储用的
    images = scrapy.Field()
    category = scrapy.Field()
    page_url = scrapy.Field()
