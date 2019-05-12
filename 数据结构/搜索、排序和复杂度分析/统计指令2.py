'''
记录一个递归的Fibonacci函数针对几个不同问题规模的调用次数
'''

from counter import Counter

def fib(n,counter):
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n-1,counter) + fib(n-2,counter)

problemSize = 2
print("%12s%15s" % ("Problem Size","Calls"))

for count in range(5):
    counter = Counter()
    fib(problemSize,counter)

    print("%12d%15s" % (problemSize,counter))
    problemSize *= 2


'''
Problem Size          Calls
           2              1
           4              5
           8             41
          16           1973
          32        4356617
'''





