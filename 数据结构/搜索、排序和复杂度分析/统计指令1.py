
problemSize = 1000
print("%12s%15s" % ("Problem Size","Iterations"))

for count in range(5):
    number = 0

    work = 1
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1

    print("%12s%15d" % (problemSize,number))
    problemSize *= 2

'''
Problem Size     Iterations
        1000        1000000
        2000        4000000
        4000       16000000
        8000       64000000
       16000      256000000
'''












