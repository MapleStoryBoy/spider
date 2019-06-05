import pandas as pd
from matplotlib import pyplot as plt

file_path = "./PM2.5/BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

# print(df.head())
# print(df.info())

# 构造时间,把分开的时间字符串通过periodIndex方法转换为pandas的时间类型
period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
# print(period,type(period))
df["datetime"] = period
print(df.head(10))

# 把datatime设置为索引
df.set_index("datetime", inplace=True)

# 进行降采样
df = df.resample('7D').mean()

# 处理缺失数据，删除缺失数据
print(df['PM_US Post'])
data = df['PM_US Post'].dropna()
data_china = df["PM_Dongsi"].dropna()

# 画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in data_china.index]
_y = data.values
_y_china = data_china.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y, label="US_POST")
plt.plot(range(len(_x_china)), _y_china, label="CN_POST")

plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
plt.legend(loc="best")

plt.show()
