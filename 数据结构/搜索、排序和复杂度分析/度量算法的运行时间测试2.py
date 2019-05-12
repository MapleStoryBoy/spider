
import time
problemSize = 1000
print("%12s%16s" % ("Problem Size","Seconds"))
for count in range(5):
    start = time.time()
    work = 1

    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1

    elapsed = time.time() - start

    print("%12s%16s" % (problemSize, elapsed))
    problemSize *= 2













