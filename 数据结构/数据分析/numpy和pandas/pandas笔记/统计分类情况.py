import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.head(1))

print(df["Genre"].head(3))

# 统计分类列表
temp_list = df["Genre"].str.split(",").tolist()

# 展开temp_list中的所有列表，获取到genre_list
genre_list = list(set([i for j in temp_list for i in j]))

# 构造全为0的数组
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)

# print(zeros_df)
# 给每个电影出现分类的位置赋值为1
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1
# print(zeros_df.head(3))


# 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)
print(genre_count)

# 排序
genre_count = genre_count.sort_values()

# 画图
_x = genre_count.index
_y = genre_count.values
plt.figure(figsize=(20, 8), dpi=80)
plt.bar(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x)
plt.show()
