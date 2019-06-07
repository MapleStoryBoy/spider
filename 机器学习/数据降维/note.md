# 数据降维
- 降维：维度：特征的数量

## 特征选择
- 特征选择就是单纯地从提取到的所有特征中选择部分特征作为训练集特征，特征在选择前和选择后可以改变值、也不改变值，但是选择后的特征维数肯定比选择前小，毕竟我们只选择了其中的一部分特征。
- 特征选择的原因
	- 冗余：部分特征的相关度高，容易消耗计算性能
	- 噪声：部分特征对预测结果有影响

- 主要方法(三大武器)：Filter(过滤式):VarianceThreshold;Embedded(嵌入式):正则化、决策树；Wrapper(包裹式)
	- 1,Filter
		- sklearn特征选择API：sklearn.feature_selection.VarianceThreshold
	- VarianceThreshold语法
		- VarianceThreshold(threshold=0.0)
			- 删除所有低方差特征
			- Variance.fit_transform(X)
				- X:numpy array格式的数据[n_samples,n_features]
				- 返回值：训练集差异低于threshold的特征将被删除。
				- 默认值是保留所有非零方差特征，即删除所有样本中具有相同值的特征。
			- VarianceThreshold流程
				- 1，初始化VarianceThreshold，指定阀值方差
				- 2，调用fit_transform
	- 2,主成分分析
		- sklearn主成分分析API：sklearn.decomposition
		- PCA是什么？
			- 本质：PCA是一种分析、简化数据集的技术
			- 目的：是数据维数压缩，尽可能降低原数据的维数（复杂度），损失少量信息。
			- 作用：可以削减回归分析或者聚类分析中特征的数量（数据也会改变，特征数量也会减少）
			- 应用场景：特征数量达到上百的时候，考虑数据的简化问题
			- PCA语法
				- PCA(n_components=None)
					- 将数据分解为较低维度空间
					- PCA.fit_transform(X)
						- X:numpy array格式的数据[n_samples,n_features]
						- 返回值：转换后指定维度的array
					- n_components的形式：
						- 1，小数 0～1 90%～95%
						- 2，整数 