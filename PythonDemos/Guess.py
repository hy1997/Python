# 石头（1） 剪刀（2） 布（3）
computer = 1

fist = int(input("请出拳 石头（1） 剪刀（2） 布（3）"))

if ((fist == 1 and computer == 2)
        or (fist == 2 and computer == 3)
        or (fist == 3 and computer == 1)):

    print("玩家赢了")
elif fist == computer:
    print("平局")
else:
    print("电脑赢了")
