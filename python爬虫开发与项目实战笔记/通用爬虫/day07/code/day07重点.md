### mongodb插入数据
- db.collecion.insert({}) 插入数据，`_id`存在就报错  
- db.collection.save({}) 插入数据，`_id`存在会更新


### mongodb的更新操作
- `db.test1000.update({name:"xiaowang"},{name:"xiaozhao"})`
- 把name为xiaowang的数据替换为`{name:"xiaozhao"}`
- `db.test1000.update({name:"xiaohong"},{$set:{name:"xiaozhang"}})`
- 把name为xiaowang的数据name的值更新为xiaozhang
- `db.test1000.update({name:"xiaozhang"},{$set:{name:"xiaohong"}},{multi:true})`
- `{multi:true}`达到更新多条的目的


### mongodb删除
- `db.test1000.remove({name:"xiaohong"},{justOne:true})`
- 默认情况会删除所有满足条件的数据，`{justOne:true}`能达到只删除一条的效果

### mongodb的count方法
- `db.collection.find({条件}).count()`
- `db.collection.count({})`

### mongodb的投影
- 投影:选择返回结果的字段
- `db.collection.find({条件},{name:1,_id:0})`
  - 1.`_id`默认会显示，置为0不显示
  - 2.出了`_id`之外的其他字段，如果不显示，不写，不能写为0
### $group的注意点
- `$group`对应的字典中有几个键，结果中就有几个键
- 分组依据需要放到`_id`后面
- 取不同的字段的值需要使用$,`$gender`,`$age`
- 取字典嵌套的字典中的值的时候`$_id.country`
- 能够同时按照多个键进行分组`{$group:{_id:{country:"$country",province:"$province"}}}`
  - 结果是：`{_id:{country:"",province:""}`

### 编辑器写mongodb语句
```
db.stu.find(
  {$or:[{age:{$gte:20}},{hometown:{$in:["桃花岛","华⼭"]}}]}
  )

#按照gender进行分组，获取不同组数据的个数和平均年龄
db.stu.aggregate(
  {$group:{_id:"$gender",count:{$sum:1},avg_age:{$avg:"$age"}}},
  {$project:{gender:"$_id",count:1,avg_age:"$avg_age",_id:0}}
  )
# 按照hometown进行分组，获取不同组的平均年龄
db.stu.aggregate(
  {$group:{_id:"$hometown",mean_age:{$avg:"$age"}}}
  )
#使用$group统计整个文档
db.stu.aggregate(
  {$group:{_id:null,count:{$sum:1},mean_age:{$avg:"$age"}}}
  )
#选择年龄大于20的学生，观察男性和女性有多少人
db.stu.aggregate(
  {$match:{$or:[{age:{$gt:20}},{hometown:{$in:["蒙古","⼤理"]}}]}},
  {$group:{_id:"$gender",count:{$sum:1}}},
  {$project:{_id:0,gender:"$_id",count:1}}
  )

#page37页练习
db.tv3.aggregate(
  {$group:{_id:{country:"$country",province:"$province",userid:"$userid"}}},
  {$group:{_id:{country:"$_id.country",province:"$_id.province"},count:{$sum:1}}},
  {$project:{country:"$_id.country",province:"$_id.province",count:1,_id:0}}
  )
```
