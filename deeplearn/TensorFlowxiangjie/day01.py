import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 创建一张图包含了一组op和tensor,上下文环境
# op：只要使用TensorFlow的API定义的函数都是op
# tensor：就指代的是数据

# g = tf.Graph()
# print(g)
# with g.as_default():
# n = tf.constant(11.0)
# print(n.graph)


# 实现一个加法运算
# a = tf.constant(5.0)
# b = tf.constant(6.0)

# sum1 = tf.add(a,b)

# 默认的这张图，相当于是给程序分配一段内存
# graph = tf.get_default_graph()
# print(graph)

# 只能运行一个图，可以在会话当中指定图去运行。
# with tf.Session(config = tf.ConfigProto(log_device_placement=True)) as sess:
# rint(sess.run(sum1))
# print(a.graph)
# print(sum1.graph)
# print(sess.graph)

# 静态形状和动态形状
# 对于静态形状来说，一旦张量形态固定了，不能再次设置静态形状,不能跨维度修改
# 动态形状可以创建一个新的张量
# plt = tf.placeholder(tf.float32,[None,2])
# print(plt)

# plt.set_shape([3,2])
# print(plt)

# lt_reshape = tf.reshape(plt,[2,3])
# print(plt_reshape)

# with tf.Session() as sess:
# pass


# 变量
# 1、变量能够持久化保存，普通张量op是不行的
# 2、当定义一个变量op的时候，一定要在会话当中去运行初始化
# 3、name参数：在tensorboard使用的时候显示名字，可以让相同op名字的进行区分。
# a = tf.constant([1,2,3,4,5])

# var = tf.Variable(tf.random_normal([2,3],mean=0.0,stddev=1.0),name='variable')

# print(a,var)

# 必须做一步显示的初始化
# init_op = tf.global_variables_initializer()

# with tf.Session() as sess:
#  必须运行初始化op
# sess.run(init_op)

# 把程序的图结构写入事件文件
# filewriter = tf.summary.FileWriter("./temp/summary/test/",graph=sess.graph)

# print(sess.run([a,var]))

# 训练参数问题：trainable
# 学习率和步数问题


def myregression():
    '''
    自己实现一个线性回归预测
    :return:None
    '''
    with tf.variable_scope("data"):
        # 1，准备数据，x特征值[100,1]    y 目标值[100]
        x = tf.random_normal([100, 1], mean=1.75, stddev=0.5, name="x_data")

        # 矩阵相乘必须是二维的
        y_true = tf.matmul(x, [[0.7]]) + 0.8

    with tf.variable_scope("model"):
        # 2,建立线性回归模型  1个特征，1个权重，一个偏置  y = x*w + b
        # 随机给一个权重和偏置的值，让它去计算损失，然后在当前状态下优化
        # trainable参数：指定这个变量能跟着梯度下降仪器优化
        weight = tf.Variable(tf.random_normal([1, 1], mean=0.0, stddev=1.0), name="w")
        bias = tf.Variable(0.0, name="b")

        y_predict = tf.matmul(x, weight) + bias

    with tf.variable_scope("loss"):
        # 3，建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):
        # 4,梯度下降优化损失   learning_rate:0~1,2,3,5,7,10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


    # 5，定义一个初始化变量的op
    init_op = tf.global_variables_initializer()

    # 6,通过会话运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        # 打印随机最先初始化的权重和偏置
        print("随机初始化的参数权重为： %f, 偏置为：%f " % (weight.eval(), bias.eval()))

        # 建立事件文件
        folewriter = tf.summary.FileWriter("./temp/summary/test/", graph=sess.graph)

        # 循环训练 运行优化
        for i in range(1300):
            sess.run(train_op)

            print("第%d次优化参数权重为： %f, 偏置为：%f " % (i, weight.eval(), bias.eval()))

    return None


if __name__ == '__main__':
    myregression()
