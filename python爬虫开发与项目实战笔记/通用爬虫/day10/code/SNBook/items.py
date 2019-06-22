# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SnbookItem(scrapy.Item):
    # define the fields for your item here like:
    parent_type = scrapy.Field()
    parent_href = scrapy.Field()
    pagecount = scrapy.Field()
    son_type = scrapy.Field()
    son_href = scrapy.Field()
    belong_son_tyoe = scrapy.Field()
    book_href = scrapy.Field()
    book_name = scrapy.Field()
    book_img = scrapy.Field()
    book_author = scrapy.Field()
    book_descrip = scrapy.Field()

