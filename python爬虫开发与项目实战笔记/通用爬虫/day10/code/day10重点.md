### crawlspider的使用
- 常见爬虫 scrapy genspider -t crawl 爬虫名 allow_domain
- 指定start_url，对应的响应会进过rules提取url地址
- 完善rules，添加Rule ` Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),`

- 注意点:
  - url地址不完整，crawlspider会自动补充完整之后在请求
  - parse函数不能定义，他有特殊的功能需要实现
  - callback：连接提取器提取出来的url地址对应的响应交给他处理
  - follow：连接提取器提取出来的url地址对应的响应是否继续被rules来过滤
