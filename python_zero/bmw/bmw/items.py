# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BmwItem(scrapy.Item):
    urls = scrapy.Field()
    partname = scrapy.Field()
