import tensorflow as tf
import os


def csvread(filelist):
    '''
    读取CSV文件
    :return: None
    '''
    # 1,构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    # 2,构造阅读器读取队列，默认以行读取
    reader = tf.TextLineReader()
    key, value = reader.read(file_queue)
    # print(value)

    # 3,对每行内容解码
    # record_defaults：指定每一个样本每一列的类型，指定默认值
    records = [['None'], ['None']]
    example, label = tf.decode_csv(value, record_defaults=records)

    # 想要读取多个数据，使用批处理
    # 批处理大小，跟队列，数据的数量没有影响，只决定这批次取多少数据，受batch_size影响，我们可以在会话中使用for循环
    # 来操作batch_size
    example_batch, label_batch = tf.train.batch([example, label], batch_size=9, num_threads=1, capacity=9)

    print(example_batch, label_batch)

    return example_batch, label_batch


if __name__ == '__main__':
    # 找到文件,放入列表    路径+名字   --- 》列表
    file_name = os.listdir("./data/csvdata/")
    filelist = [os.path.join("./data/csvdata/", file) for file in file_name]
    # print(file_name)

    example_batch, label_batch = csvread(filelist)

    # 开启会话运行结果
    with tf.Session() as sess:
        # 定义一个线程协调器
        coord = tf.train.Coordinator()

        # 开启读取文件的线程
        threads = tf.train.start_queue_runners(sess, coord=coord)

        # 打印读取的内容
        print(sess.run([example_batch, label_batch]))

        # 回收子线程
        coord.request_stop()
        coord.join(threads)
