#encoding: utf-8

import time
import threading

# 传统的方式
# def coding():
#     for x in range(3):
#         print('正在写代码%s'%x)
#         time.sleep(1)
#
# def drawing():
#     for x in range(3):
#         print('正在画图%s' % x)
#         time.sleep(1)
#
#
# def main():
#     coding()
#     drawing()
#
# if __name__ == '__main__':
#     main()

# 采用多线程的方式：

def coding():
    for x in range(3):
        print('正在写代码%s'%threading.current_thread())
        time.sleep(1)

def drawing():
    for x in range(3):
        print('正在画图%s' % threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    print(threading.enumerate())

if __name__ == '__main__':
    main()