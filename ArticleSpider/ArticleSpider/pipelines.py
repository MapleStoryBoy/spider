# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagePipeline(ImagesPipeline):
    '''
    处理图片，保存在自己设置的path
    '''
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item