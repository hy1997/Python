# 全局变量
num = 20


def demo():

  # 如果想要修改全局变量  -需要用到global关键字
    global  num

    num = 99

    print("%d" % num)


def demo1():
    print("%d" % num)


demo()
demo1()
