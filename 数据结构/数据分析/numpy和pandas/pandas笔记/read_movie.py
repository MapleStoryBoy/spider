import pandas as pd
import numpy as np

file_path = "./IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)


#print(df.info())

print(df.head(1))

#获取电影的平均评分
print(df["Rating"].mean())

#导演的人数
#print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

#获取演员的人数
temp_actors_list = df["Actors"].str.split(",").tolist()
actors_list = [i for j in temp_actors_list for i in j]

#actors_list = np.array(temp_actors_list).flatten().tolist()  #得到的每一个元素是一个列表
actors_num = len(set(actors_list))
print(actors_num)





