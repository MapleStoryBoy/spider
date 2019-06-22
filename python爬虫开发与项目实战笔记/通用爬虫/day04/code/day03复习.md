### requests如何进行url解码，如何添加超时参数
- requests.utils.unquot(url)
- requests.utils.quot(url)
- requests.get(url,timeout=3)


### retrying模块如何使用
```python
@retry(stop_max_attempt_number=3)
def fun1():
  pass
```

### 爬虫中遇到js生成的数据，怎么办
- 定位js
  - search all file搜索关键字
  - event listener
- 分析js，添加断点的方式

### 寻找登录页面post的地址
- form表单的action的url地址
  - input标签中用户名密码的name的值作为键，真正的用户名密码作为值的一个字典
- network 中抓包，找到post数据
  - form data中
    - 参数的来源
      - 响应中（当前的响应或者是其他的url地址的响应）
      - js生成

### json模块如何使用，在一个文档中连续写入多个json，能够整体的读出来么
- 字符串和python类型
  - json.loads(json_str)
  - json.dumps(python类型,ensure_ascii=False,indent=2)
- 类文件对象中的数据和python类型的转化
  - json.load(fp)[fp是类文件对象]
  - json.dump(obj,fp,ensure_ascii=False,indent=2)
