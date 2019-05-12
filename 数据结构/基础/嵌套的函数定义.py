'''
可以在一个函数的语句序列中，嵌套其它函数的定义
'''

#
'''
def factorial(n):
    def recurse(n,product):
        if n == 1: return product
        else: return recurse(n-1,n*product)
    recurse(n,1)
'''

def factorial(n,product=1):
    if n == 1:
        return product
    else:
        return factorial(n - 1, n * product)

#看看两个函数的区别