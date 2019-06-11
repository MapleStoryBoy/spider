## 逻辑回归
- 逻辑回归是解决二分类问题的利器
- ![逻辑回归](/Users/mac/Desktop/spider/机器学习/逻辑回归/逻辑回归.jpeg)
- sigmoid函数
- ![sigmoid函数](/Users/mac/Desktop/spider/机器学习/逻辑回归/sigmoid函数.jpeg)
- sigmoid函数输出值[0,1]之间。
- 逻辑回归公式
- ![逻辑回归公式](/Users/mac/Desktop/spider/机器学习/逻辑回归/逻辑回归公式.jpeg)
- Z = 回归的结果
- 逻辑回归损失函数
- ![逻辑回归损失函数](/Users/mac/Desktop/spider/机器学习/逻辑回归/逻辑回归损失函数.jpeg)
- ![目标值为1](/Users/mac/Desktop/spider/机器学习/逻辑回归/目标值为1.jpeg)
- ![目标值是0类](/Users/mac/Desktop/spider/机器学习/逻辑回归/目标值是0类.jpeg)
- 损失函数：
	- 均方误差（不存在多个局部最低点）只有一个最小值
	- 对数似然损失：多个局部最小值
	- 多个局部最小值解决方案：（尽量改善）
		- 1，多次随机初始化，多次比较最小值
		- 2，求解过程中，调整学习率

### 逻辑回归API
- sklearn.linear_model.LogisticRegression(penalty='l2',C=1.0)
	- Logistic回归分类器
	- coef_:回归系数
- 逻辑回归案例：
	- 癌症预测。
	- https://archive.ics.uci.edu/ml/machine-learning-databases/
	- 1，网上获取数据（pandas）
	- 2，数据缺失值处理，标准化
	- 3，LogisticRegression估计器流程

### LogisticRegression总结
- 应用：广告点击率预测、是否患病、金融诈骗、是否为虚假账号
- 优点：适合需要得到一个分类概率的场景，简单，速度快
- 缺点：不好处理多分类问题。

## 非监督学习
- 没有目标值，只有特征值
- k-means聚类分析
	- 1，随机在数据当中抽取k个样本，当作k个类别的中心点
	- 2，计算其余的点分别到这个中心点的距离，每一个样本有k个距离，从中选出距离最近的一个点作为自己的标记，形成k个族群
	- 3，分别计算着k个族群的平均值，把k个平均值与之前的k个旧中心点进行比较。如果相同：结束聚类；如果不相同：把k个平均值当作新的中心点，重复第二步。

- k-means的API
- sklearn.cluster.KMeans(n_clusters=8,init='k-means++')
	- k-means聚类
	- n_clusters:开始的聚类中心数量
	- init：初始化方法，默认为‘k-means++’
	- labels_:默认标记类型，可以和真实值比较（不是值比较）
- kmeans性能评估指标
	- ![kmeans性能评估指标](/Users/mac/Desktop/spider/机器学习/逻辑回归/kmeans性能评估指标.jpeg)