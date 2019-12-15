# 传递参数

# 形参


def sum_2_num(num1, num2):
    """求和计算"""
    result = num1 + num2
    print("%d + % d = %d" % (num1, num2, result))


num1 = int(input("请输入:"))
num2 = int(input("请输入:"))

# 实参
sum_2_num(num1, num2)
