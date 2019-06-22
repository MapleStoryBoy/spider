# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  logging

logger = logging.getLogger(__name__)

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "itcast":
        # if item["come_from"]=="itcast":
            logger.warning("-"*10)

        return item

class MyspiderPipeline2(object):
    def process_item(self, item, spider):
        if item["come_from"]=="jd":
            pass

        return item

