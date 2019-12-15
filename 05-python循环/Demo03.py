# 循环嵌套
row = 1
num = 1
while row <= 10:
    print("*"*row)
    row += 1


# end="" 不换行！
# while num <= 10:
#     print("*"*num, end="-")
#     num += 1

# end="" 不换行！
while num <= 10:
    for i in num:
        print("*")
    num += 1


# while row == 1:
#     print("*"*1)
#     row += 1
#     while row == 2:
#         print("*"*row)
#         row += 1
#         while row == 3:
#             print("*"*row)
#             row += 1
#             while row == 4:
#                 print("*"*row)
#                 row += 1
#                 while row == 4:
#                     print("*"*row)
#                     row += 1
#                     while row == 5:
#                         print("*"*row)
#                         row += 1



