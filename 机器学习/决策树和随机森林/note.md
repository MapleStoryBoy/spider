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