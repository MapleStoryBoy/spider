#### 验证码的识别
- url不变，验证码不变
  - 请求验证码的地址，获得相应，识别

- url不变，验证码会变
  - 思路：对方服务器返回验证码的时候，会和每个用户的信息和验证码进行一个对应，之后，在用户发送post请求的时候，会对比post请求中法的验证码和当前用户真正的存储在服务器端的验证码是否相同

  - 1.实例化session
  - 2.使用seesion请求登录页面，获取验证码的地址
  - 3.使用session请求验证码，识别
  - 4.使用session发送post请求’

- 使用selenium登录，遇到验证码
  - url不变，验证码不变，同上
  - url不变，验证码会变
    - 1.selenium请求登录页面，同时拿到验证码的地址
    - 2.获取登录页面中driver中的cookie，交给requests模块发送验证码的请求，识别
    - 3.输入验证码，点击登录

### selenium使用的注意点
- 获取文本和获取属性
  - 先定位到元素，然后调用`.text`或者`get_attribute`方法来去
- selenium获取的页面数据是浏览器中elements的内容
- find_element和find_elements的区别
  - find_element返回一个element，如果没有会报错
  - find_elements返回一个列表，没有就是空列表
  - 在判断是否有下一页的时候，使用find_elements来根据结果的列表长度来判断
- 如果页面中含有iframe、frame，需要先调用driver.switch_to.frame的方法切换到frame中才能定位元素

- selenium请求第一页的时候回等待页面加载完了之后在获取数据，但是在点击翻页之后，hi直接获取数据，此时可能会报错，因为数据还没有加载出来，需要time.sleep(3)
- selenium中find_element_by_class_name智能接收一个class对应的一个值，不能传入多个



```
db.stu.aggregate({$group:{_id:"$name",counter:{$sum:2}}})

db.stu.aggregate({$group:{_id:null,counter:{$sum:1}}})
db.stu.aggregate({$group:{_id:"$gender",name:{$push:"$name"}}})
db.stu.aggregate({$group:{_id:"$gender",name:{$push:"$$ROOT"}}})
db.tv3.aggregate(
  {$group:{_id:{"country":"$country",province:"$province",userid:"$userid"}}},
  {$group:{_id:{country:"$_id.country",province:"$_id.province"},count:{$sum:1}}},
  {$project:{country:"$_id.country",province:"$_id.province",count:"$count",_id:0}}
  )
db.stu.aggregate(

  {$match:{age:{$gt:20}}},
  {$group:{_id:"$gender",count:{$sum:1}}}
  )
db.t2.aggregate(
  {$unwind:"$size"}
  )
db.t3.aggregate(
  {$unwind:"$tags"},
  {$group:{_id:null,count:{$sum:1}}}
  )
db.t3.aggregate(
  {$unwind:{path:"$size",preserveNullAndEmptyArrays:true}}
  )
```
