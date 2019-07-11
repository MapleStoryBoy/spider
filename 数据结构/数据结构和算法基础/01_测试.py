# 如果a+b+c=1000，且a^2+b^2=c^2(a，b，c为自然数)，如何求出所有a,b,c可能的组合？

import time

start_time = time.time()
'''
for a in range(0,1001):
    for b in range(0,1001):
        for c in range(0,1001):
            if a+b+c == 1000 and a**2+b**2 == c**2:
                print('a,b,c:%d,%d,%d' % (a,b,c))
'''
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a - b
        #for c in range(0,1001):
        if a+b+c == 1000 and a**2+b**2 == c**2:
            print('a,b,c:%d,%d,%d' % (a,b,c))


end_time = time.time()
print('times:%d' % (end_time-start_time))














