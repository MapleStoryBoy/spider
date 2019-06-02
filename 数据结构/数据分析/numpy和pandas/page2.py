import numpy as np


us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"


#t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")

print(t2)


#numpy的索引和切片
#取行
print('*'*100)
#print(t2[2])

#取连续的多行
print(t2[2:])
print('*'*100)
#取不连续的多行
print(t2[[2,8,10]])
print('*'*100)
#取列
print(t2[1,:])
print(t2[2:,:])
print('*'*100)
print(t2[[2,10,3],:])

#取连续的多列
print('*'*100)
print(t2[:,2:])

#取不连续的多列
print('*'*100)
print(t2[:,[0,2]])

#取多行和多列，取第三行，第四列的值
print('*'*100)
a = t2[2,3]
print(a)
print(type(a))

#取第三行到第五行，第二列到第四列的结果
#取的是行和列交叉点的位置
print('*'*100)
b = t2[2:5,1:4]
print(b)

#取多个不相邻的点
#选出来的结果是（0，0）（2，1）（2，3）对应的值
print('*'*100)
c = t2[[0,2,2],[0,1,3]]
print(c)




