### xpath的包含
- `//div[contains(@class,'i')]`

### 实现爬虫的套路
- 准备url
  - 准备start_url
    - url地址规律不明显，总数不确定
    - 通过代码提取下一页的url
      - xpath
      - 寻找url地址，部分参数在当前的响应中（比如，当前页码数和总的页码数在当前的响应中）
  - 准备url_list
    - 页码总数明确
    - url地址规律明显

- 发送请求，获取响应
  - 添加随机的User-Agent,反反爬虫
  - 添加随机的代理ip，反反爬虫
  - 在对方判断出我们是爬虫之后，应该添加更多的headers字段，包括cookie
  - cookie的处理可以使用session来解决
  - 准备一堆能用的cookie，组成cookie池
    - 如果不登录
      - 准备刚开始能够成功请求对方网站的cookie，即接收对方网站设置在response的cookie
      - 下一次请求的时候，使用之前的列表中的cookie来请求
    - 如果登录
      - 准备多个账号
      - 使用程序获取每个账号的cookie
      - 之后请求登录之后才能访问的网站随机的选择cookie

- 提取数据
  - 确定数据的位置
    - 如果数据在当前的url地址中
      - 提取的是列表页的数据
        - 直接请求列表页的url地址，不用进入详情页
      - 提取的是详情页的数据
        - 1. 确定url
        - 2. 发送请求
        - 3. 提取数据
        - 4. 返回

    - 如果数据不在当前的url地址中
      - 在其他的响应中，寻找数据的位置
        - 1. 从network中从上往下找
        - 2. 使用chrome中的过滤条件，选择出了js,css,img之外的按钮
        - 3. 使用chrome的search all file，搜索数字和英文
  - 数据的提取
    - xpath,从html中提取整块的数据，先分组，之后每一组再提取
    - re，提取max_time,price,html中的json字符串
    - json



- 保存
  - 保存在本地，text,json,csv
  - 保存在数据库
