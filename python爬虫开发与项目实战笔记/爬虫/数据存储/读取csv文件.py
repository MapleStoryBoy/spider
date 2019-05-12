import csv

with open('data.csv','r',encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)



#使用pandas读取

import pandas as pd

df = pd.read_csv('data2.csv')
print(df)