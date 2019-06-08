## 机器学习开发流程
- 原始数据
- 明确问题做什么，建立模型的过程（根据数据类型划分应用种类）
- 数据的基本处理（pandas，处理缺失值，表合并。。。） 
- 特征工程（特征进行处理）
- 找到合适的算法进行预测
- 模型的评估（模型：算法+数据），判定效果
- 上线使用----以API形式提供  

## 机器学习算法分类
- 算法是核心，数据和计算是基础
- 算法判别依据
- 数据类型
	- 离散型数据：由记录不同类别个体的数目所得到的数据，又称计数数据，所以有这些数据全部都是整数，而且不能再细分，也不能进一步提高它的精确度。
	- 连续型数据：变量可以在某个范围内取任一数，即变量的取值可以是连续的。如，长度、时间、质量值等，这类整数通常是非整数，含有小数部分。
	- 注意：只要记住一点，离散型是区间内不可分，连续型是区间内可分。
	
- 算法分类
	- 监督学习（预测）
		- 特征值+目标值
		- 分类：目标值离散型
		- 概念：分类是监督学习的一个核心问题，在监督学习中，当输出变量取有限个离散值时，预测问题变成为分类问题，最基础的便是二分类问题，即判断是非，从两个类别中选择一个作为预测结果
			- K-近邻算法
			- 贝叶斯分类
			- 决策树
			- 随机森林
			- 逻辑回归
			- 神经网络
		- 回归：目标值连续型
		- 概念：回归时监督学习的另一个重要问题。回归用于预测输入变量和输出变量之间的关系，输出是连续型的值。
			- 线性回归
			- 岭回归
		- 注：隐马尔可夫模型
	- 无监督学习
		- 特征值
		- 聚类
			- K-means
			
### sklearn数据集
- scikit-learn数据集API介绍
	- sklearn.datasets
		- 加载获取流行数据集
		- datasets.load_*()
			- 获取小规模数据集，数据包含在datasets里
		- datasets.fetch_*(data_home=None)
			- 获取大规模数据集，需要从网络上下载，函数的第一个参数是data_home，表示数据集下载的目录，默认是～/scikit_learn_data/
	- 获取数据集返回的类型
	- load*和fetch*返回的数据类型datasets.base.Bunch(字典格式)
		- data：特征数据数组，是[n_samples*n_features]的二维numpy.ndarray数组
		- target：标签数组，是n_samples的一维numpy.ndarray数组
		- DESCR：数据描述
		- feature_names:特征名。新闻数据，手写数字、回归数据集没有feature_names
		- target_names:标签名
	
	- fit_transform(X):输入数据直接转换
	- fit():输入数据，但不做事情
	- transform():进行数据的转换
	- fit_transform() = fit() + transform()


​	
- 1，数据集划分
	- 训练集：建立模型
	- 测试集：评估模型是否有效
	- sklearn数据集划分API
		- sklearn.model_selection.train_test_split
		- 数据集进行分割
		
	- sklearn分类数据集
		- sklearn.datasets.load_iris()
			- 加载并返回鸢尾花数据集
		- sklearn.datasets.load_digits()
			- 加载并返回数字数据集
		
	- sklearn回归数据集
		- sklearn.datasets.load_boston()
			- 加载并返回波士顿房价数据集
		- sklearn.datasets.load_diabetes()
			- 加载和返回糖尿病数据集
	
	- sklearn.model_selection.train_test_split(*arrays,**options)
		- x  数据集的特征值
		- y  数据集的标签值
		- test_size  测试集的大小，一般为float
		- random_state  随机数种子，不同的种子会造成不同的随机采样结果。相同的种子采样结果相同。
		- return  训练集特征值，测试集特征值，训练标签，测试标签（默认随机取）
	
	- 用于分类的大数据集
		- sklearn.datasets.fetch_20newsgroups(data_home=None,subset='train')
			- subset:'train'或者'test','all',可选，选择要加载的数据集，训练集的‘训练’，测试集的‘测试’，两者的‘全部’。
		- datasets.clear_data_home(data_home=None)
			- 清楚目录下的数据
	
- 2，sklearn数据集接口
- 3，sklearn分类数据集
- 4，sklearn回归数据集	

### sklearn机器学习算法实现-估计器
- 在sklearn中，估计器（estimastor）是一个重要的角色，是一类实现了算法的API
- 1，用于分类的估计器
	- sklearn.neighbors   K-近邻算法
	- sklearn.naive_bayes   贝叶斯
	- sklearn.linear_model.LogisticRegression   逻辑回归
	- sklearn.tree      决策树与随机森林

- 2，用于回归的估计器
	- sklearn.linear_model.LinearRegression   线性回归
	- sklearn.linear_model.Ridge              岭回归

- 估计器使用流程	
	- 1,调用fit()，参数是训练集数据:fit(x_train,y_train)
	- 2,输入与测试集数据（x_test,y_test）
- 1,y_predict = predict(X_test)
- 2,预测的准确率：socre(X_test,y_test)	

### 分类算法-K近邻算法(KNN)
- 定义：如果一个样本在特征空间中的k个最相似（即特征空间中最邻近）的样本中的大多数属于某一个类别，则该样本也属于这个类别
- 来源：KNN算法最早是由Cover和Hart提出的一种分类算法
	
- 计算距离公式
	- 两个样本的距离可以通过如下公式计算，又叫欧式距离。比如说，a(a1,a2,a3),b(b1,b2,b3)
	- ![1](/Users/mac/Desktop/spider/机器学习/机器学习概述/1.jpeg)
	- 相似的样本，特征之间的值应该都是相近的
	- K-近邻算法：需要做标准化处理
	- sklearn K-近邻算法API
	  - sklearn.neighbors.KNeighborsClassifier(n_neighbors=5,algorithm='auto')
	    - n_neighbors:int,可选（默认=5），k_neighbors查询默认使用的邻居数
	    
	    - algorithm:{'auto','ball_tree','kd_tree','brute'},可选用于计算最近领居的算法：'ball_tree'将会使用BallTree，'kd_tree'将使用KDTree。'auto'将尝试根据传递给fit方法的值来决定最合适的算法。（不同实现方式影响效率）。
	    
	    - 在KNN算法实现实例中需要注意
	    
	      - 数据处理
	    
	        - 1，缩小数据集范围：DataFrame.query()
	    
	        - 2,怎么处理日期数据：pd.to_datetime，pd.DatetimeIndex
	    
	        - 3,增加分割的日期数据
	    
	        - 4，删除没用的日期数据：DataFrame.drop
	    
	        - 5,将签到位置少于n个用户的删除
	    
	          - place_count = data.groupby('place_id').count() 以place_id分组并统计次数
	    
	          - tf = place_count[place_count.row_id > 3].reset_index()
	    
	          - data = data[data['place_id'].isin(tf.place_id)]
	    
	    - K-近邻算法优缺点
	    	- 优点：简单，易于理解，易于实现，无需估计参数，无需训练
	    	- 缺点：
	    		- 1，懒惰算法，对测试样本分类时的计算量大，内存开销大
	    		- 2，必须指定K值，K值选择不当则分类精确度不能保证
	    	- 使用场景：小数据场景，几千～几万样本，具体场景具体业务去测试
	    
	            
	    
	            ​							