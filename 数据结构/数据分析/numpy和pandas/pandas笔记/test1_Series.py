import pandas as pd
import numpy as np

t = pd.Series([1,2,31,12,3,4])

print(t)  #带索引
print(type(t))

print("*"*100)
import string
#指定索引 index
t1 = pd.Series(np.arange(10),index=list(string.ascii_uppercase[:10]))
print(t1)

#通过字典创建
a = {string.ascii_uppercase[i]:i for i in range(10)}#字典推倒式
t2 = pd.Series(a)
print(t2)
print(type(t2))
print(t2[t2>4])
print(t2.index)#可以使用for遍历
print(t2.values)
print(type(t2.values))



