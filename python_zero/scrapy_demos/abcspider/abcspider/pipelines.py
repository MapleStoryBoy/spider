# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class AbcspiderPipeline(object):
    def __init__(self):

        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        print("="*40)
        return item

    def close_spider(self,spider):
        with open('qsbk.json','w',encoding='utf-8') as fp:
            json.dump(self.items,fp,ensure_ascii=False)