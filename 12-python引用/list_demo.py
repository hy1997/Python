# 不会改变内存地址


a = [1,2,3]

print(id(a))

a.append(4)

print(id(a))

a.clear()

print(id(a))


a =[]

print(id(a))

d = {'name':'xiaoming'}

d["age"] =18

print(id(d))


d.clear()

print(id(d))


