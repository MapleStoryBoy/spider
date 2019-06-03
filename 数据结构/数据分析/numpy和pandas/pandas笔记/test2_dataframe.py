
import numpy as np
import pandas as pd

t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print(t)
'''
Dataframe对象既有行索引，又有列索引
行索引，表明不同行，横向索引，叫index，0轴，axis=0
列索引，表明不同列，纵向索引，叫columns，1轴，axis=1

'''

d1 = {"name":["xiaoming","xiaogang"],"age":[22,24],"tel":[10086,10010]}
t1 = pd.DataFrame(d1)
print(t1)






