import time
problemSize = 10000000

print("%12s%16s" % ("Problem Size","Seconds"))

for count in range(5):
    start = time.time()
    work = 1
    for x in range(problemSize):
        work += 1
        work -= 1

    elapsed = time.time() - start

    print("%12s%16s" % (problemSize,elapsed))
    problemSize *= 2
'''
Problem Size         Seconds
    100000001.3758049011230469
    200000002.52891206741333
    400000005.090194940567017
    8000000010.147652864456177
   16000000020.27204918861389

'''

