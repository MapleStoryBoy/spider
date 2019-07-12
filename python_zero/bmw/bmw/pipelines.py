# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

class BmwPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__),"images")
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        partname = item['partname']
        urls = item['urls']
        partpath = os.path.join(self.path,partname)
        if not os.path.exists(partpath):
            os.mkdir(partpath)
        for url in urls:
            imagename = url.split('__')[-1]
            request.urlretrieve(url,os.path.join(self.path,imagename))
        return item
