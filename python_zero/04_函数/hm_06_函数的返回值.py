def sum_2_num(num1, num2):
    """对两个数字的求和"""

    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果
    return result
    # 注意：return 就表示返回，下方的代码不会被执行到！
    # num = 1000

# 可以使用变量，来接收函数执行的返回结果
sum_result = sum_2_num(10, 20)

print("计算结果：%d" % sum_result)
