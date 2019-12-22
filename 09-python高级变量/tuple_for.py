info_tuple = ("zhangsan", 18, 1.75)
num_lists=[1,10,3,23,1997,9,27]
for info in info_tuple:
    print(info)

# 元组格式化字符串
print("%s 年龄是 %d  身高 %.2f" % info_tuple)
info_str = "%s 年龄是 %d  身高 %.2f" % info_tuple
print(info_str)

# 装换函数 tuple()  list()

# 数组转元组
num_tuple=tuple(num_lists)
print(type(num_tuple))
# 元组转数组
info_lists=list(info_str)
print(type(info_lists))
