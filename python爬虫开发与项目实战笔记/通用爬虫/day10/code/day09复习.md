### scrapy数据流程
- 调度器---》request---》引擎---》下载中间件---》下载器
- 下载器发送请求，获取resposne，---》response--->下载中间件---》引擎---》爬虫中间件---》spider
- spider 提取数据---》引擎---》pipeline
- spider 提取url地址--》构造request---》爬虫中间件---》引擎---》调度器

### scrapy如何发送请求，能够携带什么参数
- scrapy.Request(url,callback,meta,dont_filter)
- dont_filter=True 表示请求过的url地址还会继续被请求


### scrapy如何把数据从一个解析函数传递到另一个，为什么需要这样做
- meta是个字典类型，meta = {"item":item}
- response.meta["item"]


### scrapy中Item是什么，如何使用
- Item 类，继承自scarpy.Item,name=scrapy.Field()
- Item 定义那些字段我们需要抓取
- 使用和字典一样
- 在mongodb中插入数据的时候 dict(item)

### pipeline中open_spider和close_spider是什么
- open_spdier 爬虫开启执行一次，只有一次
- close_spider 爬虫关闭的时候执行一次，只有一次
