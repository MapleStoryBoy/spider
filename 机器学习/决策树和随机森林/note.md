## 决策树
- 决策树思想的来源非常朴素，程序设计的条件分支结构就是if-then结构，最早的决策树就是利用这类结构分割数据的一种分类学习方法
- 信息熵
- ![信息熵](/Users/mac/Desktop/spider/机器学习/决策树和随机森林/信息熵.jpeg)
- 信息和消除不确定性是相联系的
### 决策树的划分依据之一 - 信息增益
- 特征A对训练集D的信息增益g(D,A)，定义为集合D的信息熵H(D)与特征A给定条件下D的信息条件熵H(D|A)之差，即公式为
- ![信息增益](/Users/mac/Desktop/spider/机器学习/决策树和随机森林/信息增益.jpeg)
- 
- 注意：信息增益表示得知特征X的信息而使得类Y的信息的不确定性减少的程度
- ![信息熵增益计算](/Users/mac/Desktop/spider/机器学习/决策树和随机森林/信息熵增益计算.jpeg)
- 决策树的分类依据之一：信息增益。
- 常见决策树使用的算法：
	- ID3
		- 信息增益 最大的准则
	- C4.5
		- 信息增益比 最大的准则
	- CART
		- 回归树：平方误差 最小
		- 分类树：基尼系数 最小的准则 在sklearn中可以选择划分的默认原则

### sklearn决策树API
- class sklearn.tree.DecisionTreeClassifter(criterion='gini',max_depth=None,random_state=None)
	- 决策树分类器
	- criterion：默认是‘gini’系数，也可以选择信息增益的熵‘entropy’
	- max_depth:树的深度大小
	- random_state：随机种子
	- method：
	- decision_path:返回决策树的路径

### 示列：泰坦尼克号乘客生存分类模型
- 1，pd读取数据
- 2，选择有影响的特征，处理缺失值
- 3，进行特征工程，pd转换字典，特征抽取x_train.to_dict(orient="records")
- 4，决策树估计器流程

### 决策树的结构、本地保存
- 1，sklearn.tree.export_graphviz()该函数能够导出DOT格式
	- tree.export_graphviz(estimator,out_file='tree.dot',feature_names=[","])
- 2，工具：（能够将dot文件转换为pdf、png）
	- 安装graphviz
	- mac：brew install graphviz
- 3，运行命令
	- dot -Tpng tree.dot -o tree.png

### 决策树的优缺点以及改进
- 优点：
	- 简单的理解和解释，树木可视化
	- 需要很少的数据准备，其它技术通常需要数据归一化

- 缺点：
	- 决策树学习者可以创建不能很好地推广数据过于复杂的树，这被称为过拟合

- 改进：
	- 减枝cart算法（决策树API当中已经实现，随机森林参数调优有相关介绍）
	- 随机森林
	- 注意：企业重要决策，由于决策树很好的分析能力，在决策过程应用较多。

## 集成学习方法-随机森林
### 集成学习方法
- 集成学习通过建立几个模型组合来解决单一预测问题，它的工作原理是生成多个分类器/模型，各自独立地学习和作出预测，这些预测最后结合成单预测，因此优于任何一个单分类的做出预测。

- 什么是随机森林
- 定义：在机器学习中，随机森林是一个包含多个决策树的分类器，并且其输出的类别是由个别树输出的类别的众数而定
- 随机森林建立多个决策树的过程：(N个样本，M个特征)
	- 单个树建立过程：
		- 1，随机在N个样本当中选择一个样本，重复N次，样本可能重复
		- 2，随机在M个特征当中选出m个特征  m取值
	- 建立10颗决策树，样本，特征大多不一样（随机又放回的抽样）

### 随机森林API
- class sklearn.ensemble.RandomForestClassifier(n_estimators=10,criterion='gini',max_depth=None,bootstrap=True,random_state=None)
	- 随机森林分类器
	- n_estimators:integer  optional(default=10)森林里的树木数量120，200，300，500，800，1200
	- criteria：string 可选(default='gini')分割特征的测量方法
	- max_depth:integer或None 可选（默认=无）树的最大深度，5，8，15，25，30
	- max_features="auto",每个决策树的最大特征数量
		- if 'auto',then 'max_features=sqrt(n_features)'.
		- if 'sqrt',then 'max_features=sqrt(n_features)'(same as 'auto').
		- if 'log2',then 'max_features=log2(n_features)'.
		- if None,then 'max_features=n_features'.
	
	- bootstrap:boolean,optional(default=True)是否在构建树时使用放回抽样。
