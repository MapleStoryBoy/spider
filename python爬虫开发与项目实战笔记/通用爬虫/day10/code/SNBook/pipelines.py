# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class SnbookPipeline(object):
    def process_item(self, item, spider):
        item['son_type'] = [re.sub(r'\r\n|\s', '', i) for i in item['son_type']]
        item['son_type'] = [i for i in item['son_type'] if len(i)>0]

        item['book_descrip'] = [re.sub(r'\u3000', '', i) for i in item['book_descrip']]
        item['book_descrip'] = [i for i in item['book_descrip'] if len(i) > 0]
        print(item)