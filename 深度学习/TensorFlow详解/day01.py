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


















