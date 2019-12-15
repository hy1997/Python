

def print_line(char, times):
    """"打印分隔符
    :param char:
    :param times:
    """
    print(char*times)


def print_lines(char, times):
    """打印多行分割线

    :param char:  分割线的字符
    :param times:  分割线的重复次数
    """
    i = 0
    while i < 5:
        print_line(char, times)
        i += 1


name = "胡怡"
