### mongodb的索引如何使用
- `db.collection.ensureIndex({name:1})`
- `db.colelction.getIndexes()`
- `db.collection.dropIdex({name:1})`
- 创建唯一索引 `db.collection.ensureIndex({},{unique:ture})`
- 创建复合索引 `db.collection.ensureIndex({name：1，age:1},{unique:ture})`

### pymongo如何使用
- from pymongo import MongoClient
- client = MongoClient(host,port)  #建立连接
- colelction = client["db"]["collection"]
- 增
  - collection.insert({})
  - collection.insert_many([{},{}])
- 删除
  - collection.delete_one({条件})
  - collection.delete_many()
- 更新
  - colelction.update_one
  - collection.update_many
- 查询
  - collection.find({})
    - 返回cursor，能够迭代，只能迭代一些
  - collection.find_one()

### scrapy的数据流程
- 调取器---》request对象---》引擎---》下载中间件---》下载器
- 下载器发送请求，获取响应---》response---》下载中间件---》引擎---》爬虫中间件---》spider
- spider提取数据--- 》引擎---》pipeline
- spider提取的url地址---》构造request对象---》爬虫中渐渐---》引擎---》调度器


### scrapy的使用流程
- 创建项目 scrapy startproject 项目名
- 创建爬虫 scrapy genspider spider_name allow_domain
- 完善爬虫
  - start_url,response --> parse
  - 数据yield 通过传递给管道
  - 能够yield 的数据类型，dict，request，Item，None
- 管道
  - 开启管道
    - 开启管道，键:位置，值：距离引擎的远近，越小越近，说句越先经过
