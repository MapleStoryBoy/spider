'''
递归函数：调用自身的函数，为了防止函数无限次地重复调用自己，它至少包含一条选择语句。
'''
'''
迭代算法转换成一个递归函数

def displayRange(lower,upper):
    while lower <= upper:
        print(lower)
        lower += 1
'''
'''
def displayRange(lower,upper):
    if lower <= upper:
        print(lower)
        displayRange(lower+1,upper)
'''
'''
def ourSum(lower,upper):
    if lower > upper:
        return 0
    else:
        return lower + ourSum(lower + 1,upper)

'''
def ourSum(lower,upper,margin=0):
    blanks = " " * margin
    print(blanks,lower,upper)

    if lower > upper:
        print(blanks,0)
        return 0
    else:
        result = lower + ourSum(lower+1,upper,margin + 4)
        print(blanks,result)
        return result
ourSum(2,5)
