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
	

### 二、卷积神经网络（CNN）
- 神经网络（neural networks）的基本组成包括输入层、隐藏层、输出层。二卷积神经网络的特点在于隐藏层分为卷积层和池化层（pooling layer，又叫下采样层）
	- 卷积层：通过在原始图像上平移来提取特征
	- 池化层：通过特征后稀疏参数来减少学习的参数，降低网络的复杂度，（最大池化和平均池化）

- 卷积神经网络的结构
	- 1，卷积层过滤器
		- 个数
		- 大小（1*1，3*3，5*5）
		- 步长
		- 零填充
		- 卷积层输出深度、输出宽度
			- 深度由过滤器个数决定
			- 输出宽度
	- 2，激活函数
	- ![激活函数Relu](/Users/mac/Desktop/spider/deeplearn/neurl_network/激活函数Relu.jpeg)
	- 3，池化层
	- 4，全连接层
- 注：在大型网络当中会有一个droupout（减少过拟合）
	- 卷积层过滤器的参数
		- 输入体积大小H1*W1*D1
		- 四个超参数：
			- Filter数量K
			- Filter大小F
			- 步长S
			- 零填充大小P
		- 输出体积大小H2*W2*D2
			- H2 = （H1-F+2P）/ S + 1
			- W2 = （W1-F+2P）/ S + 1
			- D2 = K 
	- 卷积层的零填充
		- 卷积核在提取特征映射时的动作称之为padding（零填充），由于移动步长不一定能整出整张图的像素宽度。其中有两种方式，SAME和VALID
			- 1，SAME：越过边缘取样，取样的面积和输入图像的像素宽度一致。
			- 2，VALID：不越过边缘取样，取样的面积小于输入人的图像的像素宽度
	- 卷积网络API介绍
	- 卷积层：
		- tf.nn.conv2d(input,filter,strides=,padding=,name=None)
		- 计算给定4-D input和filter张量的2维卷积
			- input：给定的输入张量，具有[batch,height,width,channel],类型为float32，64
			- filter：指定过滤器的大小，[filter_height,filter_width,in_channels,out_channels]
			- strides：strides = [1,stride,stride,1],步长
			- padding："SAME","VALID",使用的填充算法的类型，使用"SAME".其中"VALID"表示滑动超出部分舍弃，"SAME"表示填充，使得变化后height，width一样大。 
	- 激活函数：
	- tf.nn.relu(features,name=None)
		- features:卷积后加上偏置的结果
		- return:结果

	- 池化层（pooling）计算
		- Pooling层主要的作用是特征提取，通过去掉Feature Map中不重要的样本，进一步减少参数数量。Pooling的方法很多，最常用的是Max 
		- Pooling。2*2，步长2
		- ![池化层计算](/Users/mac/Desktop/spider/deeplearn/neurl_network/池化层计算.jpeg)
	
	- 池化API：
	- tf.nn.max_pool(value,ksize=,strides=,padding=,name=None)---输入上执行最大池数
		- value：4-D Tensor形状[batch,height,width,channels]
		- ksize：池化窗口大小，[1,ksize,ksize,1]
		- strides：步长大小，[1,strides,strides,1]
		- padding："SAME","VALID",使用的填充算法的类型，使用"SAME"

	- Full Connected层
		- 分析：前面的卷积和池化相当于做特征工程，后面的全连接相当于做特征加权。最后的全连接层在整个卷积神经网络中起到“分类器”的作用。
	- 卷积网络分析
	- ![卷积网络实现分析](/Users/mac/Desktop/spider/deeplearn/neurl_network/卷积网络实现分析.jpeg)
		
### 三、分布式TensorFlow
- 分布式API
	- 1，创建一个tf.train.ClusterSpec,用于对集群中的所有任务进行描述，该描述内容对所有任务应该是相同的。
	- 2，创建一个tf.train.Server,用于创建一个任务(ps,worker)，并运行相应作业上的计算任务。
- 1，创建集群
	- cluster = tf.train.CluterSpec({"ps":ps_spec,"worker":worker_spec})
	- cluster = tf.train.ClusterSpec({"worker":["worker0.example.com:2222","worker1.example.com:2222","worker2.example.com:2222"],"ps":["ps0.example.com:2222","ps1.example.com:2222"]})

- 2，创建服务
	- tf.train.Server(server_or_cluster_def,job_name=None,task_index=None,protocol=None,config=None,start=True)
		- 创建服务(ps,worker)
		- server_or_cluster_def:集群描述
		- job_name:任务类型名称
		- task_index:任务数
		- attribute：target
			- 返回tf.Session连接到此服务器的目标
		- method：join()
			- 参数服务器端，直到服务器等待接受参数任务关闭
- 3，工作节点指定设备运行
	- tf.device(device_name_or_function)
	- 选择指定设备或者设备参数
	- if device_name:
		- 指定设备
		- 例如："/job:worker/task:0/cpu:0"
	- if function:
		- tf.train.replica_device_setter(worker_device=worker_device,cluster=cluster)
		- 作用：通过此函数协调不同设备上的初始化操作
		- worker_device:为指定设备，"/job:worker/task:0/cpu:0"or"/job:worker/task:0/gpu:0"
		- cluster:集群描述对象
	- 注：使用with tf.device(),使不同工作节点工作在不同的设备上

- 4，分布式会话API
	- tf.train.MonitoredTrainingSession(master="",is_chief=True,checkpoint_dir=None,hooks=None,save_checkpoint_secs=600,save_summaries_steps=USE_DEFAULT,save_summaries_secs=USE_DEFAULT,config=None)
	- 分布式会话函数
	- master：指定运行会话协议ip和端口（用于分布式）
		- "grpc://192.168.0.1:2000"
	- is_chief是否为主worker（用于分布式）
		- 如果为True，它将负责初始化和恢复基础的Tensorflow会话。如果为False，它将等待一位负责人初始化或恢复Tensorflow会话
	- checkpoint_dir：检查点文件目录，同时也是events目录
	- config：会话运行的配置项，tf.ConfigProto(log_device_placement=True)
	- hooks:可选SessionRunHook对象列表
	- should_stop():是否异常停止
	- run()：跟session一样可以运行op

- 5，常用钩子
	- tf.train_StopAtStepHook(last_step=5000)
	- 指定执行的训练轮数也就是max_step，超过了就会抛出异常
	- tf.train.NanTensorHook(loss)
	- 判断指定Tensor是否为NaN，为NaN则结束
	- 注：在使用钩子的时候需要定义一个全局步数：global_step=tf.contrib.framework.get_or_create_global_step()
	
	
