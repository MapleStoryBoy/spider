import pandas as pd
import numpy as np



t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))


print(t)
print("*"*100)
t1 = t.iloc[1,:]
print(t1)

print("*"*100)
t2 = t.iloc[:,2]
print(t2)

print("*"*100)
t3 = t.iloc[:,[2,1]]
print(t3)

print("*"*100)
t4 = t.iloc[[0,2],[2,1]]
print(t4)

print("*"*100)
t5 = t.iloc[1:,:2]
print(t5)