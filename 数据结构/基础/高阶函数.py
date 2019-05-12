'''
高阶函数：它接收另一个函数作为参数，并且以某种方式应用函数。
比如map和filter，他们对于处理可迭代的对象很有用
'''
newList = []
oldList = [1,2,3,4,5,6]
'''
for number in oldList:
    newList.append(str(number))

print(newList)
'''

newList = list(map(str,oldList))
print(newList)