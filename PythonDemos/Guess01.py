# 导入函数 （类似与Java的导Jar包）
import random
# 随机生成数字
computer = random.randint(1, 3)
# 用户输入数字
fist = int(input("请出拳 石头（1） 剪刀（2） 布（3）"))

if ((fist == 1 and computer == 2)
        or (fist == 2 and computer == 3)
        or (fist == 3 and computer == 1)):

    print("玩家赢了")
elif fist == computer:
    print("平局")
else:
    print("电脑赢了")


if computer == 1:
    computer = "石头"
elif computer == 2:
    computer = "剪刀"
elif computer == 3:
    computer = "布"

if fist == 1:
    fist = "石头"
elif fist == 2:
    fist = "剪刀"
elif fist == 3:
    fist = "布"

print("电脑随机生成的数据：%s,玩家输入：%s " % (computer, fist))




# def alter(computer ):
#     if computer == 1:
#         computer = "石头"
#     elif computer == 2:
#         computer = "剪刀"
#     elif computer == 3:
#         computer = "布"
#     pass

