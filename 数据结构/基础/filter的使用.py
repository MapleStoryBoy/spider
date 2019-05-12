'''
假设你想要从考试分数的一个列表中删除所有的0分。
'''
newList = []
oldList = [90,63,74,88,0,67,78,0]
'''
for number in oldList:
    if number > 0:
        newList.append(number)
print(newList)
'''
#使用filter实现
newList = list(filter(lambda number:number > 0,oldList))

print(newList)