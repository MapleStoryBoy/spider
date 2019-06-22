### requests如何获取响应的url地址和请求的url地址，如何发送post请求
- response.url
- response.request.url
- requests.post(url,data={})

### 如何发送带headers的请求和params的请求
- requests.get(url,headers={})
- requests.get(url,params = {})


### 如何使用代理，正向代理和反向代理的区别
- requests.get(url,proxies={协议:协议+ip+端口})
- 正向代理：客户端知道最终服务器的地址
- 反向代理：客户端不知道最终服务器的地址

### 模拟登陆的三种方式
- session
  - 实例化session（session具有的方法和requests一样）
  - session发送请求post请求，对方服务器设置的cookie会保存在session
  - session请求登录后能够访问的页面

- cookie放在headers中
  - headers = {"Cookie":"cookie字符串"}

- cookie转化为字典放在请求方法中
  - requests.get(url,cookies={"name的值":"values的值"})
