'''
创建一个匿名函数传递给map或者filter，从而避免定义像isPositive这样的一次性的辅助函数。
语法： lambda：<argument list> : <expression>

'''
'''
另一个高阶函数functools.reduce，通过应用带有两个参数的函数来将一个可迭代
对象的项转换为单个值，而该函数的两个参数是下一项和前一次应用该函数的结果。
'''
#示例
import functools
product = functools.reduce(lambda x,y:x * y,range(1,11))
print(product)