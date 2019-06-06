# 数据特征预处理

## 归一化公式
- 特点：通过对原始数据进行交换把数据映射到(默认为[0，1])之间
- 注：作用于每一列，max为一列的最大值，min为一列的最小值，那么X''为最终结果，mx，mi分别为指定区间值默认为mx为1，mi为0.
- sklearn归一化API
	- sklearn.preprocessing.MinMaxScaler
- 目的：使得某一个特征对最终结果不会造成更大的影响

- MinMaxScaler语法
	- MinMaxScaler(feature_range=(0,1)...)
		- 每个特征缩放到给定范围(默认[0,1])
		- MinMaxScaler.fit_transform(X)
			- X:numpy array格式的数据[n_samples,n_features]
			- 返回值：转换后的形状相同的array
	- 归一化实现步骤：
		- 1，实例化MinMaxScalar
		- 2，通过fit_transform转换
- 数据中异常点较多，会有什么影响？
	- 异常点对最大值最小值影响太大
	- 缺点：归一化对异常点处理不是特别好
- 总结：注意在特定场景下最大值最小值是变化的，另外，最大值与最小值非常容易受异常点影响，所以这种方法鲁棒性较差，只适合传统精确小数据场景

### 标准化
- 1，特点：通过对原始数据进行交换把数据变换到均值为0，方差为1范围内
- 公式：见标准化.jpeg
- 对比标准化和归一化
	- 对于归一化来说：如果出现异常点，影响了最大值和最小值，那么结果显然会发生改变
	- 对于标准化来说：如果出现异常点，由于具有一定数据量，少量的异常点对于平均值的影响并不大，从而方差改变较小。

- sklearn特征化API：scikit-learn.preprocessing.StandardScaler
- StandardScaler语法
	- StandardScaler(...)
		- 处理之后每列来说所有数据都聚集在均值0附近方差为1
		
		- StandardScaler.fit_transform(X)
			- X:numpy array格式的数据[n_samples,n_features]
			- 返回值：转换后的形状相同的array

		- StandardScaler.mean_
			- 原始数据中每列特征的平均值

		- StandardScaler.std_
			- 原始数据每列特征的方差

		- 标准化实现步骤
			- 实例化StandardScaler
			- 通过fit_transform转换	
	
