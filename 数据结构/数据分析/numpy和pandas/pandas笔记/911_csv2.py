import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv("./911.csv")

#获取分类
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]

cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)),columns=["cate"])
#print(cate_df)

df["cate"] = cate_df
print(df.groupby(by="cate").count()["title"])