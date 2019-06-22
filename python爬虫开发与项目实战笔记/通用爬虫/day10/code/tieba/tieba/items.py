# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tz_herf = scrapy.Field()
    tz_title = scrapy.Field()
    tz_content = scrapy.Field()
    tz_visitor_response = scrapy.Field()
    tz_talk = scrapy.Field()
    tz_img = scrapy.Field()

