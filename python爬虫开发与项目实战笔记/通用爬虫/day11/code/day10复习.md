### crawlspider如何使用
- 创建爬虫 scarpy genspider -t crawl spider_name allow_domain
- 完善spider
  - 1.start_url
  - 2.完善rules
    - 元组
    - Rule(LinkExtractor,callback，follow)
      - LinkExtractor 连接提取器，提取url
      - callback url的响应会交给该callback处理
      - follow= True url的响应会继续被Rule提取地址
  - 3.完善callback


### 下载中间件如何使用
- 定义类
- process_request 处理请求，不需要return
- process_response  处理响应，需要return request response
- settings中开启

### scrapy如何模拟登陆
- 携带cookie登录
  - 准备cookie字典
  - scrapy.Request(url,callback,cookies=cookies_dict)

- scrapy.FormRequest(post_url,formdata={},callback)
- scrapy.FormRequest.from_response(response,formdata,callback)
