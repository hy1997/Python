# break 结束循环（终止）  continue 跳出当前循环（循环体下面的代码不走了 ，重新开始下一个循环）
i = 0
while i < 10:
    i += 1

    if i == 2:
        continue
    if i == 8:
        break
    print("%d" % i)
