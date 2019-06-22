### 爬虫的概念
- 爬虫是模拟浏览器发送请求，获取响应

### 爬虫的流程
- url--->发送请求，获取响应--->提取数据---》保存
- 发送请求，获取响应--->提取url

#### 爬虫要根据当前url地址对应的响应为准 ，当前url地址的elements的内容和url的响应不一样

### 页面上的数据在哪里
- 当前url地址对应的响应中
- 其他的url地址对应的响应中
  - 比如ajax请求中
- js生成的
  - 部分数据在响应中
  - 全部通过js生成

### requests中解决编解码的方法
- response.content.decode()
- response.content.decode("gbk")
- response.text
