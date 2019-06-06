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
- 标准化总结：在已有样本足够多的情况下比较稳定，适合现代嘈杂大数据场景。

### 如何处理缺失值：
- 1，删除(不建议)：如果每列或者行数据缺失值达到一定的比例，建议放弃整行或者整列
- 2，插补：可以通过缺失值每行或者每列的平均值、中位数来填充
- 3，sklearn缺失值API：sklearn.preprocessing.Imputer
- 4,Imputer语法
	- Imputer(missing,values='NaN',strategy='mean',axis=0)
		- 完成缺失值插补
		- Imputer.fit_transform(X)
			- X:numpy array格式的数据[n_samples,n_features]
			- 返回值：转换后的形状相同的array
		- Imputer流程
			- 1，初始化Imputer，指定‘缺失值’，指定填补策略，指定行或列
			- 注意：缺失值也可以是别的指定要替换的值
			- 2，调用fit_transform

### 特征预处理
- 通过特定的统计方法（数学方法）将数据转换成算法要求的数据
- sklearn特征处理API：所有的预处理方法都在sklearn.preprocessing中。
			
	
	
