import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一张图包含了一组op和tensor,上下文环境
# op：只要使用TensorFlow的API定义的函数都是op
# tensor：就指代的是数据

g = tf.Graph()
print(g)
with g.as_default():
    n = tf.constant(11.0)
    print(n.graph)




# 实现一个加法运算
a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a,b)

# 默认的这张图，相当于是给程序分配一段内存
graph = tf.get_default_graph()
print(graph)

# 只能运行一个图，可以在会话当中指定图去运行。
with tf.Session(config = tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run(sum1))
    print(a.graph)
    print(sum1.graph)
    print(sess.graph)

# 静态形状和动态形状
# 对于静态形状来说，一旦张量形态固定了，不能再次设置静态形状
# 动态形状可以创建一个新的张量
plt = tf.placeholder(tf.float32,[None,2])
print(plt)

plt.set_shape([3,2])
print(plt)

plt_reshape = tf.reshape(plt,[2,3])
print(plt_reshape)

with tf.Session() as sess:
    pass












