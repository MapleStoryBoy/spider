### domz的案例给我们展示了一个什么样的爬虫，如何实现的
- 增量式爬虫（爬取过的生成指纹），断点续爬（带爬取的request存在redis中）
- settings中设置
  - 指定的去重的类
  - 指定调度器的类
  - redis_url
  - redisPipeline


### request对象什么时候入队
- dont_filter=True
- 全新的url
- url在start_urls中的
  - start_request


### scrapy_redis去重方法
- 使用sha1得到requests的指纹
- 指纹存在redis的集合中
- 下一次request，生成指纹，判断是否存在redis的集合中


### 生成指纹
- fp = hashlib.sha1()
- fp.update(request.method)
- fp.update(request.body or b"")
- fp.update(url)
- fp.hexdigest()


### 判断数据是否存在redis的集合中，不存在插入
- added = server.sadd(key,fp)
- return added == 0 #Ture 插入失败，已经存在
