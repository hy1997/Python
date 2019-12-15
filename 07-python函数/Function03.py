# 只有在函数中 主动调用函数时才会执行函数中的代码！ 并且只能在函数后面定义！

""""
小明
hello 1
hello 1
hello 1
hello 1
小明
"""

name = "小明"


def say_hello():
    print("hello 1")
    print("hello 1")
    print("hello 1")
    print("hello 1")


print(name)

say_hello()

print(name)
