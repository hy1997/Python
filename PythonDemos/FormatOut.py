# 格式化输出
"""
格式符号 转换
%c  字符
%s  通过str() 字符串转换来格式化
%i  有符号十进制整数
%d  有符号十进制整数
%u  无符号十进制整数
%o  八进制整数
%x  十六进制整数（小写字母）
%X  十六进制整数（大写字母）
%e  索引符号（小写'e'）
%E  索引符号（大写“E”）
%f  浮点实
%g  ％f和％e 的简写
%G  ％f和％E的简写
"""

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


