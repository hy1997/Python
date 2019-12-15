def multiple_table():

    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # print("*", end="")
            print("%d * %d = % d " % (col, row, col * row), end="  ")
            col += 1
        print("循环 %d" % row)
        row += 1


