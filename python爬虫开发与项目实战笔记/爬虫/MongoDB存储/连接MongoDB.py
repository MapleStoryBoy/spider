import pymongo
#建立连接
client = pymongo.MongoClient(host='localhost',port=27017)

db = client.test

collection =db['students']

student1 = {
    'id':'20190101',
    'name':'Jsp',
    'age':20,
    'gender':'male'
}
student2 = {
    'id':'20190102',
    'name':'Pjs',
    'age':23,
    'gender':'male'
}

#result = collection.insert_one(student1)
#print(result)

#result2 = collection.insert_many([student1,student2])
#print(result2)
#print(result2.inserted_ids)


result2 = collection.find_one({'name':'Jsp'})
print(type(result2))
print(result2)


from bson.objectid import ObjectId
result2 = collection.find_one({'_id':ObjectId('5cd81ddf86e68604295039b4')})
print(result2)


# find()

results = collection.find({'age':20})
print(results)
for result in results:
    print(result)

# 查询年龄大于20的数据
result3 = collection.find({'age':{'$gt':19}})
print(result3)
for i in result3:
    print(i)

count = collection.find().count()
print(count)

count1 = collection.find({'age':20}).count()
print(count1)



#排序
results = collection.find().sort('name',pymongo.ASCENDING)
print([result['name'] for result in results])