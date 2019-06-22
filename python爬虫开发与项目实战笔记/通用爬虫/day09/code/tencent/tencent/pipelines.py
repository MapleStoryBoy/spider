# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from tencent.items import TencentItem

client = MongoClient()
collection = client["tencent"]["hr"]

class TencentPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,TencentItem):
            print(item)
            collection.insert(dict(item))
        return item
