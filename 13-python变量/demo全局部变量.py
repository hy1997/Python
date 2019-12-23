# 全局变量
num = 20


def demo():
    # 修改全局变量的值
    # 在python中，是不允许直接修改全局变量的值
    # 这里定义的 num 是一个局部变量 不是全局变量（不是修改的全局变量的引用）
    #  但是在Java里面是可以修改的！！！
    num = 99

    print("%d" % num)


def demo1():
    print("%d" % num)


demo()
demo1()
