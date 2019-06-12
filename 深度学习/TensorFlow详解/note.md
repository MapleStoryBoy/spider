## TensorFlow
- 前端系统：定义程序的图的结构
- 后端系统：运算图结构
- tebsor：张量
- operation（op）：专门运算的操作节点，所有操作都是一个op
- 图：graph：整个程序的结构
- 会话：运算程序的图
- ![TensorFlow数据流图介绍](/Users/mac/Desktop/spider/深度学习/TensorFlow详解/TensorFlow数据流图介绍.jpeg)

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
	- 3，掌握资源（变量生命周期）

- tf.Session()
	- 运行TensorFlow操作图的类，使用默认注册的图（可以指定运行图）
- 会话资源
	- 会话可能拥有很多资源，如tf.Variable,tf.QueueBase和tf.ReaderBase,会话结束后需要进行资源释放
	- 1，sess = tf.Session()  sess.run(...)  sess.close
	- 2，使用上下文管理器
		- 	with tf.Session() as sess:
			- sess.run(...)
	- config = tf.ConfigProto(log_device_placement=True)
	- 交互式：tf.InteractiveSession()
	
