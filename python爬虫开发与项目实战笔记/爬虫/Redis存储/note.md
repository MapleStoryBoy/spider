# redis存储
- redis和StrictRedis
    - redis-py库提供两个类 Redis 和 StrictRedis 来实现 Redis 的命令操作 。
    
    - 启动redis：brew service redis start
        - redis-server
    

- 连接Redis
   
   
        from redis import StrictRedis
        redis = StrictRedis(host='localhost',port=6379,db=0,password='maple')  
- ConnectionPool连接
    
    
    from redis inport StrictRedis,ConnectionPool
    pool = ConnectionPool(host='localhost',port=6739,db=0,password='')
    redis = StrictRedis(connection_pool=pool)  
    
- RedisDump
     - 提供了强大的 Redis数据的导人和导出功能
  
