#encoding: utf-8

import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTimes = 0

class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            print('%s当前存入%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            time.sleep(0.5)
            gLock.release()

class Consumer(threading.Thread):
    def run(self):
        global gMoney
        global gLock
        global gTimes
        while True:
            money = random.randint(100, 500)
            gLock.acquire()
            if gMoney > money:
                gMoney -= money
                print('%s当前取出%s元钱，剩余%s元钱' % (threading.current_thread(), money, gMoney))
                time.sleep(0.5)
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s当前想取%s元钱，剩余%s元钱，不足！" % (threading.current_thread(),money,gMoney))
            gLock.release()

def main():
    for x in range(5):
        Consumer(name='消费者线程%d'%x).start()

    for x in range(5):
        Producer(name='生产者线程%d'%x).start()

if __name__ == '__main__':
    main()

