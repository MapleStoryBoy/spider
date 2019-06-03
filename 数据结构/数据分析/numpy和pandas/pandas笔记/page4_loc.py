import pandas as pd
import numpy as np



t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))

print(t)

t1 = t.loc["a","z"]
t2 = t.loc["a",:]
print(t1)
print(t2)

t3 = t.loc[:,"y"]
print(t3)

