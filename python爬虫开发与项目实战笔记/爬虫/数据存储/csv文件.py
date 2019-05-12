
#写入
import csv


with open('data.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    #writerow()方法传入每行的数据
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','Mike',20])
    writer.writerow(['10002','Jsp',21])
    writer.writerow(['10003','Bob',22])
#初始化写入对象时传入delimiter 为空格，此时输出结果的 每一列就是以空格分隔了

'''
多行同时写入
writer.writerow([['10001','Mike',20],['10002','Jsp',21],['10003','Bob',22]])



'''






