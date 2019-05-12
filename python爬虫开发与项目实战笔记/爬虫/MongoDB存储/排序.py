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


