# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from tieba.settings import MONGO_HOST
from pymongo import MongoClient

from tieba.items import TiebaItem

client = MongoClient()
collection = client['tieba']['tbdetail']

class TiebaPipeline(object):
    # def open_spider(self, spider):
    #     client = MongoClient()
    #     self.collection = client["tieba"]["yuantienglish"]

    def process_item(self, item, spider):
        # self.collection.insert(dict(item))
        if isinstance(item, TiebaItem):
            print(item)
            collection.insert(dict(item))
        return item
