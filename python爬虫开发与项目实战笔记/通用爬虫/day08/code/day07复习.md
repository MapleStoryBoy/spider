### mongodb的增删改查如何操作
- 增
  - db.collection.insert() #`_id`相同会报错
  - db.collection.save() #`_id`相同会更新其余的字段
- 删
  - db.collection.remove({},{justOne:ture})
- 更新
  - `db.collection.update({},{$set:{name:"a"}},{multi:true})`
- 查询
  - db.collection.find({})
  - db.collection.find({}).pretty()

### mongodb统计数量，mongodb的投影操作
- db.collection.count({})
- db.collection.find({}).count
- 投影：设置返回的字段
- db.collection.find({},{_id:0,name:1})



### mongodb的比较运算符(大于，小于等于等)，范围运算符（in，not in），逻辑运算符（and ，or）
- 大于，大于等于 `$gt,$get`
- `$lt,$lte 小于，小于等于`
- $ne 不等于

- 在 `$in`
  - `db.collection.find({name:{$in:["a","b","c"]}})`
- 不在 `$nin`
  - `db.collection.find({name:{$nin:["a","b","c"]}})`

- 和
  - `db.collection.find({name:"a",age:20})`
- or
  - `bd.collection.find({$or:[{name:"a"},{age:20}]})`



### mongodb的排序和消除重复
- 排序
  - db.collection.find({}).sort({age:1})

- distinct
  - db.collection.distinct("gender",{age:{$gt:18}})
  - 返回数组


### 聚合操作的分组和计数如何使用，如何修改输出数据的样式，
- 分组
  - `db.collection.aggregate({$group:{_id:"$age",count:{$sum:1}}})`
- `$project`
  - `db.collection.aggregate(
    {$group:{_id:"$age",count:{$sum:1}}},
    {$project:{_id:0,age:"$_id",count:1}}
    )`


### 聚合操作如何匹配内容
- `$match`
  - `db.collection.aggregate(
    {$match:{gender:true},
    {$group:{_id:"$age",count:{$sum:1}}},
    {$project:{_id:0,age:"$_id",count:1}}
    )`
