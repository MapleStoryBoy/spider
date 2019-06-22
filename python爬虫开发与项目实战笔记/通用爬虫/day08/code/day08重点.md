### mongodb mysql redis的区别和使用场景
- mysql是关系型数据库，支持事物
- mongodb，redis非关系型数据库，不支持事物
- mysql，mongodb，redis的使用根据如何方便进行选择
  - 希望速度快的时候，选择mongodb或者是redis
  - 数据量过大的时候，选择频繁使用的数据存入redis，其他的存入mongodb
  - mongodb不用提前建表建数据库，使用方便，字段数量不确定的时候使用mongodb
  - 后续需要用到数据之间的关系，此时考虑mysql

### 爬虫数据去重，实现增量式爬虫
- 使用数据库建立关键字段（一个或者多个）建立索引进行去重

- 根据url地址进行去重
  - 使用场景：
    - url地址对应的数据不会变的情况，url地址能够唯一判别一个条数据的情况
  - 思路
    - url存在redis中
    - 拿到url地址，判断url在redis的url的集合中是够存在
    - 存在：说明url已经被请求过，不再请求
    - 不存在：url地址没有被请求过，请求，把该url存入redis的集合中
  - 布隆过滤器
    - 使用多个加密算法加密url地址，得到多个值
    - 往对应值的位置把结果设置为1
    - 新来一个url地址，一样通过加密算法生成多个值
    - 如果对应位置的值全为1，说明这个url地址已经抓过
    - 否则没有抓过，就把对应位置的值设置为1

- 根据数据本省进行去重
  - 选择特定的字段，使用加密算法（md5，sha1）讲字段进行假面，生成字符串，存入redis的集合中
  - 后续新来一条数据，同样的方法进行加密，如果得到的字符串在redis中存在，说明数据存在，对数据进行更新，否则说明数据不存在，直接插入

### page50练习
```
db.tv1.aggregate(
  {$project:{title:1,_id:0,count:"$rating.count",rate:"$rating.value",country:"$tv_category"}},
  {$match:{rate:{$gt:8}}},
  {$group:{_id:"$country",count:{$sum:1}}},
  {$project:{_id:0,country:"$_id",count:1}}
  )
```
