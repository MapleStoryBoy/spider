# 911数据中不同月份不同类型的电话的次数的变化情况
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./911.csv")
# 把时间字符串转为时间类型设置为索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

# 添加列，表示分类
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))

#指定index为timeStamp
df.set_index("timeStamp", inplace=True)

plt.figure(figsize=(20, 8), dpi=80)
# 分组
for group_name, group_data in df.groupby(by="cate"):
    # 对不同的分类进行绘图
    count_by_month = group_data.resample('M').count()['title']
    # print(count_by_month)

    # 画图
    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
