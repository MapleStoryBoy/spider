# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SinaItem(scrapy.Item):
    main_name = scrapy.Field()
    sub_name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pub_time = scrapy.Field()
    author = scrapy.Field()
