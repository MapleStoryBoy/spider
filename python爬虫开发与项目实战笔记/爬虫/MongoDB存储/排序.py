import pymongo
#建立连接
client = pymongo.MongoClient(host='localhost',port=27017)

db = client.test

collection =db['students']


#排序
results = collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])


#偏移
results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

#limit
results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])


#更新
condition = {'name':'Pjs'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition,student)
print(result)

#h或者使用$set操作符对数据进行更新： result = collection.update(condition,{'$set':student}
#update_one()方法和 update_many()方法，用法更加严格，它们的第二个参数需要使用$类型操作符作为字典的键名
'''
condition = {'name':'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition,{'$set':student})
print(result)
print(result.matched_count,result.modified_count)
'''
#删除 remove()方法指定删除条件即可
result = collection.remove({'name':'Pjs'})
print(result)



