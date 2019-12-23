# 全局变量 定义在函数的开头
gl_num = 20

name = "张三"


def demo():

  # 如果想要修改全局变量  -需要用到global关键字
    global \
        num

    num = 99

    print("%d" % num)
    print("%d" % name)
    # print("%d" % title)





demo()
# 错误 找不到
# title ="python Hello"
