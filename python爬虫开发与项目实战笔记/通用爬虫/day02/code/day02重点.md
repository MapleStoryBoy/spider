### 判断请求否是成功
```python
assert response.status_code==200
```

### url编码
- `https://www.baidu.com/s?wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2`

### 字符串格式化的另一种方式
```python
"传{}智播客".format(1)
```

### 使用代理ip
- 准备一堆的ip地址，组成ip池，随机选择一个ip来时用

- 如何随机选择代理ip，让使用次数较少的ip地址有更大的可能性被用到
  - {"ip":ip,"times":0}
  - [{},{},{},{},{}],对这个ip的列表进行排序，按照使用次数进行排序
  - 选择使用次数较少的10个ip，从中随机选择一个

- 检查ip的可用性
  - 可以使用requests添加超时参数，判断ip地址的质量
  - 在线代理ip质量检测的网站


### 携带cookie请求
- 携带一堆cookie进行请求，把cookie组成cookie池

### 使用requests提供的session类来请求登陆之后的网站的思路
- 实例化session
- 先使用session发送请求，登录对网站，把cookie保存在session中
- 再使用session请求登陆之后才能访问的网站，session能够自动的携带登录成功时保存在其中的cookie，进行请求

### 不发送post请求，使用cookie获取登录后的页面
- cookie过期时间很长的网站
- 在cookie过期之前能够拿到所有的数据，比较麻烦
- 配合其他程序一起使用，其他程序专门获取cookie，当前程序专门请求页面

### 字典推导式，列表推到是
```python
cookies="anonymid=j3jxk555-nrn0wh; _r01_=1; _ga=GA1.2.1274811859.1497951251; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; ln_uact=mr_mao_hacker@163.com; depovince=BJ; jebecookies=54f5d0fd-9299-4bb4-801c-eefa4fd3012b|||||; JSESSIONID=abcI6TfWH4N4t_aWJnvdw; ick_login=4be198ce-1f9c-4eab-971d-48abfda70a50; p=0cbee3304bce1ede82a56e901916d0949; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20171230/1635/main_JQzq_ae7b0000a8791986.jpg; t=79bdd322e760beae79c0b511b8c92a6b9; societyguester=79bdd322e760beae79c0b511b8c92a6b9; id=327550029; xnsid=2ac9a5d8; loginfrom=syshome; ch_id=10016; wp_fold=0"
cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
```
```python
[self.url_temp.format(i * 50) for i in range(1000)]
```

### 获取登录后的页面的三种方式
- 实例化session，使用session发送post请求，在使用他获取登陆后的页面
- headers中添加cookie键，值为cookie字符串
- 在请求方法中添加cookies参数，接收字典形式的cookie。字典形式的cookie中的键是cookie的name对应的值，值是cookie的value对应的值
