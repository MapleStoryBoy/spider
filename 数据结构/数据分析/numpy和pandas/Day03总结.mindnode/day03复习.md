#### numpy的索引和切片
  - t[10,20]
  - `t[[2,5],[4,8]]`

  - t[3:]
  - t[[2,5,6]]

  - t[:,:4]
  - t[:,[2,5,6]]

  - t[2:3,5:7]


#### numpy中的bool索引,where,clip的使用
  - t[t<30] = 2
  - np.where(t<10,20,5)
  - t.clip(10,20)


#### 转置和读取本地文件
  - t.T
  - t.transpose()
  - t.sawpaxes()

  - np.loadtxt(file_path,delimiter,dtype)


#### nan和inf是什么
  - nan not a number
  - np.nan != np.nan
  - 任何值和nan进行计算都是nan

  - inf 无穷

#### 常用统计函数
  - t.sum()
  - t.mean()
  - np.meadian()
  - t.max()
  - t.min()
  - np.ptp()
  - t.std()
