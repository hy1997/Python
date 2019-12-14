# 格式化输出
name = "小明"
print("我的名字叫%s" % name)


student_no = 1
# 我的学号是：001
print("我的学号是：%03d" % student_no)

price = 805
weight = 12
money = price * weight
print("单价为 %.2f 购买 %.3f  价格为！%.4f" % (price, weight, money))


# 输出 0.00%
scale = 0.8
print("数据比例为%.2f%%" % (scale * 100))


