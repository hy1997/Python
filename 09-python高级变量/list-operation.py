# 列表常用操作 增删改查
""""
    int[] arr =new int[10];  Java里面的数组操作
"""

name_lists = ["张三", "李四", "王五"]
temp_lists = ["1", "2", "3"]

# 取值 取索引  （类似于Java中的下标）
print(name_lists[2])
# 知道数据内容，取出索引
print(name_lists.index("李四"))


# 修改
name_lists[0] = "zhangs"
# list assignment index out of range 超出范围程序会报错
name_lists[2] = "lishi"


# 增加
name_lists.insert(2, "胡壹")
name_lists.append("huyi")
# 可以把其他列表的内容完整的追加到列表的末尾
name_lists.extend(temp_lists)

# 删除
name_lists.remove("lishi")
# name_lists.remove(name_lists[1])
name_lists.pop(3)

#  del关键字本质是把一个变量从内存中删除！
del name_lists[1]


arr = ["12", "12", "12", "12", "1234"]

# name_lists.clear()

# len（length 长度） 行数可以统计列表中的元素总数
print(len(arr))

# count 方法可以统计列表中某一个数据出现的次数
print(arr.count("12"))
#  删的是第一个元素！
arr.remove("12")

print(name_lists)

for name in name_lists:
    print(name)


