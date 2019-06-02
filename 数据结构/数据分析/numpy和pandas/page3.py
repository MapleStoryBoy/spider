#数组的行列交换
import numpy as np
t = np.arange(12,24).reshape(3,4)

print(t)

t[[1,2],:] = t[[2,1],:]
print(t)










