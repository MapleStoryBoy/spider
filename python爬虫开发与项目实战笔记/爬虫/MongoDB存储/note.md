# 连接MongoDB
     连接MongoDB时，我们需要使用PyMongo库里面的MongoClient。一般来说，传人 MongoDB 的IP及端口即可，
    其中第一个参数为地址 host，第二个参数为端口 port (如果不给它传递参数，默 认是 27017)
     建立连接：client = pymongo.MongoClient(host='localhost',port=27017)
     指定数据库：db =client.test
     指定集合：1、collection = db.students 2、collection =db['students']
     插入数据：
         result = collection.insert(student)
         官方推荐insert_one()和 insert_many()方法来分别插入单条记录和多条记录
     查询:
         find_one():)查询得到的是单 个结果，
         find():返回一个生成器对象
         也可以根据 Objectid来查询， 此时需要使用 bson库里面的 objectid
         
      计数：统计查询结果有多少条数据，可以调用 count()方法
         count =collection.find().count()
      统计符合某个条件的数据:count= collection.find({'age' : 20}) .count()
      
      排序：直接调用 sort()方法，并在其中传入排序的字段及升降序标志即可，pymongo.ASCENDING指定升序。
       如果要降序排列，可以传人 pymongo.DESCENDING。 
         results = collection.find().sort('name',pymongo.ASCENDING)
            
      偏移:可以利用 skip()方法偏移几个位置 ，比如偏移 2，就忽略前两个元素，得到第 三个及以后的元素
         results = collection.find().sort('name',pymongo.ASCENDING).skip(2) 
      还可以用 limit()方法指定要取的结果个数：
         results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
      值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查 询数据，
      因为这样很可能导致内存溢出
      
      更新：可以使用 update()方法，指定更新的条件和更新后的数据 即可 
         
         
         
         
      
         
     启动MongoDB服务：brew services start mongodb
         接下来进入MongoDB：终端输入mongo
        