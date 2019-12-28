# def sum_numbers(num):
#     print(num)
#     # 递归自己掉自己
#     sum_numbers(num)
#
#
# sum_numbers(1)


def sum_numbers1(num):
    if num == 1:
        return 1
    temp = sum_numbers1(num - 1)
    return num + temp


print(sum_numbers1(100))
