## 神经网络
### 一、神经网络基础
- 感知机
	- 在n个输入数据，通过权重与各数据之间的计算和，比较激活函数结果，得出输出
	- 应用：很容易解决与、或问题
		- 与或问题：于：所有的输入为1，输出为1.或：只要有一个为1，输出就为1.异或：相同为0，不同为1.
	- 感知机解决分类问题，下图为简单的感知机模型
	- ![简单的感知机模型](/Users/mac/Desktop/spider/deeplearn/neurl_network/简单的感知机模型.jpeg)
	- 单个感知机解决不了的问题，可以增加
	- Rosenblatt在1957年，于Cornell航空实验室所发明的一种人工神经网络

	- 神经网络的发展
		- 定义：在机器学习和认知科学领域，人工神经网络（artificial neural network，缩写ANN），简称神经网络（neural network，缩写NN）或类神经网络，是一种模仿生物神经网络的结构和功能的计算模型，用于对函数进行估计或近似。
		- 神经网络的种类：
			- 基础神经网络：单层感知机，线性神经网络，BP神经网络，Hopfield网络等
			- 进阶神经网络：玻尔兹曼机，受限玻尔兹曼机，递归神经网络等
			- 深度神经网络：深度置信网络，卷积神经网络，循环神经网络，LSTM网络等  
	- 神经网络的特点
		- 输入向量的维度和输入神经元的个数相同
		- 每个连接都有个权值
		- 同一层神经元之间没有连接
		- 由输入层，隐层，输出层组成
		- 第N层与第N-1层的所有神经元连接，也叫全连接
	- 神经网络的组成
		- 结构（Architecture）例如：神经网络中权重，神经元等等
		- 激活函数（Activity Rule）
		- 学习规则（Learning Rule）学习规则指定了网络中的权重如何随着时间推进而调整。（反向传播算法）

	- 神经网络API模块
		- 在使用tensorflow时候，tf.nn,tf.layers,tf.contrib模块有很多功能是重复的。
		- 1，tf.nn：提供神经网络相关操作的支持，包括卷积操作（conv）、池化操作（pooling）、归一化、loss、分类操作、embedding、RNN、Evaluation。
		- 2，tf.layers：主要提供的高层的神经网络，主要和卷积相关的，对tf.nn的进一步封装。
		- tf.contrib：tf.contrib.layers提供能够将计算图中的网络层、正则化、摘要操作、是构建计算图的高级操作，但是tf.contrib包不稳定以及一些实验代码。

	- 浅层人工神经网络模型
		- SoftMax回归函数
		- ![SoftMax回归](/Users/mac/Desktop/spider/deeplearn/neurl_network/SoftMax回归.jpeg)
		- 交叉熵损失函数
		- ![交叉熵损失](/Users/mac/Desktop/spider/deeplearn/neurl_network/交叉熵损失.jpeg)
	
		- 1，全连接-从输入直接到输出
		- 特征加权
			- tf.matmul(a,b,name=None) + bias
				- return:全连接结果，供交叉损失运算
				- 不需要激活函数（因为是最后的输出）
		- 2，SoftMax计算、交叉熵
			- tf.nn.softmax_cross_entropy_with_logits(labels=None,logits=None,name=None)----计算logits和labels之间的交叉损失熵
			- labels:标签值（真实值）
			- logits：样本加权之后的值
			- return：返回损失值列表
		- 3，损失值列表平均值计算
			- tf.reduce_mean(input_tensor)
			- 计算张量的尺寸的元素平均值
		- 4，其它方法--损失下降API
			- tf.train.GradientDescentOptimizer(learning_rate)---梯度下降优化
			- learning_rate:学习率，一般为
			- minimize(loss):最小化损失
			- return：梯度下降op
		- 5，获取数据
			- from tensorflow.examples.tutorials.mnist import input_data
			- mnist = input_data.read_data_sets(FLAGS.data_dir,one_hot=True)
		
		- 6，准确性计算
			- equal_list = tf.equal(tf.argmax(y,1),tf.argmax(y_label,1))
			- accuracy = tf.reduce_mean(tf.cast(equal_list,tf.float32))

		- Mnist数据集神经网络实现流程
			- 1，准备数据
			- 2，全连接结果计算
			- 3，损失优化
			- 4，模型评估（计算准确性）
### 二、人工神经网络（ANN）
### 三、Mnist数据集浅层神经网络分析
### 四、卷积神经网络（CNN）
### 五、卷积网络Mnist数字图片识别
