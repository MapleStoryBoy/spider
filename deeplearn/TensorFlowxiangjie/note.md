## TensorFlow
- 前端系统：定义程序的图的结构
- 后端系统：运算图结构
- tensor：张量
- operation（op）：专门运算的操作节点，所有操作都是一个op
- 图：graph：整个程序的结构
- 会话：运算程序的图
- ![TensorFlow数据流图介绍](/Users/mac/Desktop/spider/deeplearn/TensorFlowxiangjie/TensorFlow数据流图介绍.jpeg)
### 图
- 图默认已经注册，一组表示tf.Operation计算单位的对象和tf.Tensor表示操作之间流动的数据单元的对象
- 获取调用：
	- tf.get_default_graph()
	- op、sess或者tensor的graph属性
- 图的创建
	- tf.Graph()
	- 使用新创建的图
		- g = tf.Graph()
		- with g.as_default():
			- a = tf.constant(1.0)
			
### 会话
- 会话的作用：
	- 1，运行图的结构
	- 2，分配资源计算
	- 3，掌握资源（变量生命周期，队列，线程）

- tf.Session()
	- 运行TensorFlow操作图的类，使用默认注册的图（可以指定运行图）
- 会话资源
	- 会话可能拥有很多资源，如tf.Variable,tf.QueueBase和tf.ReaderBase,会话结束后需要进行资源释放
	- 1，sess = tf.Session()  sess.run(...)  sess.close（sess.run，启动整个图）
	- 2，使用上下文管理器（对比第一种方法）
		- 	with tf.Session() as sess:
			- sess.run(...)
	- config = tf.ConfigProto(log_device_placement=True)
	- 交互式：tf.InteractiveSession()
- 会话里面的run方法
	- run(fetches,feed_dict=None,graph=None)
		- 运行ops和计算tensor
		- 嵌套列表，元组，namedtuple，dict或OrderedDict（重载的运算符也能运行）
		- feed_dict 允许调用者覆盖图中指定张量的值，提供给placeholder使用
		- 返回值异常
			- RuntimeError：如果它Session处于无效状态（例如已关闭）。
			- TypeError：如果fetches或feed_dict键是不合适的类型。
			- ValueError：如果fetches或feed_dict键无效或引用Tensor不存在。

### 张量（tensor）
- tensorflow依赖的是numpy

- 张量的阶和数据类型
	- Tensorflow基本的数据格式
	- 一个类型化的N维数组（tf.Tensor）
	- 三部分，名字，形状，数据类型
	
- 张量的属性
	- graph   张量所属的默认图
	- op      张量的操作名
	- name    张量的字符串描述
	- shape   张量的形状
	
- 张量的动态形状与静态形状
	- Tensorflow中，张量具有静态形状和动态形状
	- 静态形状：
		- 创建一个张量，初始状态的形状
			 - tf.Tensor.get_shape():获取静态形状
			 - tf.Tensor.set_shape():更新Tensor对象的静态形状，通常用于在不能直接推断的情况下。
	- 动态形状：
		- 一种描述原始张量在执行过程中的一种形状（动态变化）
		- tf.reshape:创建一个具有不同动态形状的新张量。
   - 要点：
   		- 1，转换静态形状的时候，1-D到1-D，2-D到2—D，不能跨阶数改变形状
   		- 2，对于已经固定或者设置静态形状的张量/变量，不能再次设置静态形状
   		- 3，tf.reshape()动态创建新张量时，元素个数不能不匹配

- 张量操作-生成张量
	
	- 固定值张量
	- ![张量操作-生成张量](/Users/mac/Desktop/spider/deeplearn/TensorFlowxiangjie/张量操作-生成张量.jpeg)
	
	![创建随机张量](/Users/mac/Desktop/spider/deeplearn/TensorFlowxiangjie/创建随机张量.jpeg)
	
- 正态分布

- ![正态分布](/Users/mac/Desktop/spider/deeplearn/TensorFlowxiangjie/正态分布.jpeg)


### 变量
- 变量也是一种op，是一种特殊的张量，能够进行存储持久化，它的值就是张量，默认被训练。
- 变量的创建
	- tf.Variable(initial_value=None,name=None,trainable=True)
		- 创建一个带值initial_value的新变量
		- assign(value)-----为变量分配一个新值,返回新值
		- eval(session=None)------计算并返回此变量的值
		- name属性表示变量的名字

- 变量的初始化
	- tf.global_variables_initializer()
	- 添加一个初始化所有变量的op，在会话中开启。

### 可视化学习Tensorboard
- 数据序列化-events文件
	- Tensorboard通过读取TensorFlow的事件文件来运行
- tf.summary.FileWriter("/tmp/tensorflow/summary/test/",graph=)
	- 返回filerwriter，写入事件文件到指定目录（最好用绝对路径），以提供给tensorboard使用
- 开启
	- tensorboard --logdir="/tmp/tensorflow/summary/test/"
	- 一般浏览器打开为127.0.0.1:6006
- 注：修改程序后，在保存一遍会有新的事件文件，打开默认最新

- 增加变量显示
- 目的：观察模型的参数、损失值等变量值的变化
	- 1，收集变量
		- tf.summary.sclar(name='',tensor)收集对于损失函数和准确率等单值变量，name为变量的名字，tensor为值
		- tf.summary.history(name='',tensor)收集高纬度的变量参数
		- tf.summary.image(name='',tensor)收集输入的图片张量能显示图片
	- 2，合并变量写入事件文件
		- merged = tf.summary.merge_all()
		- 运行合并：summary = sess.run(merged),每次迭代都需运行
		- 添加：FileWriter.add_summary(summary,i)i表示第几次的值。

### tensorflow实现一个简单的线性回归案例
- 1，准备好1特征和1目标值(y = x*0.7 + 0.8)
- 2，建立模型，准备一个权重w，一个偏置b（随机初始化） y_predict = xw+b（模型的参数必须用变量定义）
- 3，求损失函数，均方误差((y1-y1')^2+....+(y_100-y_100')^2)/100
- 4，梯度下降优化损失的过程，指定学习率

- Tensorflow运算API
	- 矩阵运算
		- tf.matmul(x,w)
	- 平方
		- tf.square(error)
	- 均值
		- tf.reduce_mean(error)
- 梯度下降API
	- tf.train.GrandientDescentOptimizer(learning_rate)
		- 梯度下降优化
		- learning_rate:学习率，一般为
		- method：
		- minimize(loss)
		- return:梯度下降op
- 关于梯度爆炸/梯度消失
	- 在极端情况下，权重的值变得非常大，以至于溢出，导致NaN值
	- 如何解决梯度爆炸问题（深度神经网络（如RNN）当中更容易出现）
	- 1，重新设计网络
	- 2，调整学习率
	- 3，使用梯度截断（在训练过程中检查和限制梯度的大小）
	- 4，使用激活函数

- tensorflow变量作用域
	- tf.variable_socpe(<socpe_name>)创建指定名字的变量的作用域
		- 观察变量的name改变
	- 嵌套使用变量作用域
		- 观察变量的name改变

- 模型保存和加载
	- tf.train.Saver(var_list=None,max_to_keep=5)
		- var_list:指定将要保存和还原的变量。它可以作为一个dict或一个列表传递
		- max_to_keep:指示要保留的最近检查点文件的最大数量。创建新文件时，会删除较旧的文件。如果无或0，则保留所有检查点文件，默认为5（即保留最新的5个检查点文件。）
	- 例如：saver.save(sess,"/tmp/ckpt/test/model")
		- saver.restore(sess,"/tmp/ckpt/test/model")
	- 保存文件格式：checkpoint文件

### 线程队列与IO操作
- 队列和线程
	- 队列与队列管理器
		- Tensorflow队列
			- 在训练样本的时候，希望读入的训练样本是有序的
			- tf.FIFOQueue先进先出队列，按顺序出队列
			- tf.RandomShuffleQueue随机出队列
		- tf.FIFOQueue
			- FIFOQueue(capacity,dtypes,name='fifo_queue')
			- 创建一个以先进先出的顺序对元素进行排队的队列
				- capacity：整数。可能存储在此队列中的元素数量的上限
				- dtypes：DType对象列表。长度dtypes必须等于每个队列元素中的张量数，dtype的类型形状，决定了后面进队列元素的形状
				- method
					- dequeue(name=None)
					- enqueue(vals,name=None)
					- enqueue_many(vals,name=None):vals列表或者元组
					- 返回一个进队列操作
					- size(name=None)
	- 线程和协调器






​	