import pandas as pd

#read_csv读取csv中的文件
df = pd.read_csv("./dogNames2.csv")

print(df[(800 < df["Count_AnimalName"])&(df["Count_AnimalName"] < 1000)])