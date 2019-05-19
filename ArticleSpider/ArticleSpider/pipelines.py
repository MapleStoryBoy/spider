# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs,json
import MySQLdb
import MySQLdb.cursors
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义导出json文件
    def __init__(self):
        # json文件保存和格式
        self.file = codecs.open('article.json','w',encoding='utf-8')
    def process_item(self,item,spider):
        #调用json.dumps方法以字典形式保存数据
        lines = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(lines)
        return item
    def spider_close(self,spider):
        self.file.close()


class JsonExporterPipeline(object):
    #调用scrapy提供的json_export导出json文件
    def __init__(self):
        self.file = open('articleexporter.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    '''
    采用同步的机制插入数据库
    '''
    def __init__(self):
        self.conn = MySQLdb.connect('localhost','root','maple','test2',charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        insert_sql = """
            insert into jobbole_article(title,url,create_date,fav_nums,url_object_id,
            front_image_url,front_image_path,comment,praise_nums,tags,content)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
       """
        self.cursor.execute(insert_sql,(item['title'],item['url'],item['create_date'],item['fav_nums'],
                                        item['url_object_id'],item['front_image_url'],item['front_image_path'],
                                        item['comment'],item['praise_nums'],item['tags'],item['content']))
        self.conn.commit()



class MysqlTwistedPipeline(object):
    '''
    twisted 异步api写入数据到数据库
    '''
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        #从settings文件中引入mysql基础配置
        dbparms = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            passwd = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)

    def process_item(self,item,spider):
        # 使用twisted将mysql插入变成异步插入
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error)

    def handle_error(self,failure):
        # 处理异步插入的异常
        print(failure)


    def do_insert(self,cursor,item):
        # 执行具体插入
        insert_sql = """
                   insert into jobbole_article(title,url,create_date,fav_nums,url_object_id,
                   front_image_url,comment,praise_nums,tags,content)
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
              """
        cursor.execute(insert_sql, (item['title'], item['url'], item['create_date'], item['fav_nums'],
                                         item['url_object_id'], item['front_image_url'],
                                         item['comment'], item['praise_nums'], item['tags'], item['content']))



class ArticleImagePipeline(ImagesPipeline):
    '''
    处理图片，保存在自己设置的path
    '''
    def item_completed(self, results, item, info):
        for ok,value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item