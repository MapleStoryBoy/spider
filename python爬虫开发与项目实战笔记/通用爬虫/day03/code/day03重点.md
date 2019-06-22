### 寻找登录的post地址
- 在form表单中寻找action对应的url地址
  - post的数据是input标签中name的值作为键，真正的用户名密码作为值的字典，post的url地址就是action对应的url地址

- 抓包，寻找登录的url地址
  - 勾选perserve log按钮，防止页面跳转找不到url
  - 寻找post数据，确定参数
    - 参数不会变，直接用，比如密码不是动态加密的时候
    - 参数会变
      - 参数在当前的响应中
      - 通过js生成



### 定位想要的js
- 选择会触发js时间的按钮，点击event listener，找到js的位置
- 通过chrome中的search all file来搜索url中关键字
- 添加断点的方式来查看js的操作，通过python来进行同样的操作


### 安装第三方模块
- pip install retrying
- 下载源码解码，进入解压后的目录，```python setup.py install```
- `***.whl` 安装方法 `pip install ***.whl`

### json使用注意点
- json中的字符串都是双引号引起来的
  - 如果不是双引号
    - eval：能实现简单的字符串和python类型的转化
    - replace：把单引号替换为双引号
- 往一个文件中写入多个json串，不再是一个json串，不能直接读取
  - 一行写一个json串，按照行来读取
