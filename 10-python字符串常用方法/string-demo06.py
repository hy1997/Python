# len()    方法返回对象（字符、列表、元组等）长度或项目个数。

a = [1,23,3,5,2,"a"]

print(len(a))
# max()    方法返回给定参数的最大值，参数可以为序列
lists = [1,2,3,4,5,6]

print(max(lists))

print(min(lists))


print([1,2]*5)
print((1,2)*5)

print([1,2]+[3,4])
print((1,2)+(3,4))

t_list = [1,2]
t_list.extend([3,4])
print(t_list)
t_list.append([3,4])
print(t_list)


print(3 in t_list)

print(3 not in t_list)
