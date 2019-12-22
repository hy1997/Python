# 元祖  定义后不能修改
info_tuple = ("zhangsan", 18, 1.75)
print(type(info_tuple))  # <class 'tuple'>


single_tuple=(5)
print(type(single_tuple))  # <class 'int'>

# 定义一个只包含一个元素的元组
single_tuple=(5,)
print(type(single_tuple))  # <class 'tuple'>

# 常用方法

# 统计
print(info_tuple.count("zhangsan"))

# 取取索引
print(info_tuple.index("zhangsan"))

print(len(info_tuple))
