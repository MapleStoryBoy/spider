import tensorflow as tf


def main(argv):

    # 指定集群描述对象
    tf.train.ClusterSpec({"ps":[],"worker":["192.168.8.141:2222"]})









if __name__ == '__main__':

    tf.app.run()