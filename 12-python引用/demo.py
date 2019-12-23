def test(num):
    print("在函数内部%d 对应的内存地址 %d" %(num,id(num)))

    b = 20
    print("返回的内存地址是 %d" % id(b))
    # 放回的是数据的引用 而不是数据本身
    return b

a = 10

print("a 变量保存数据的内存地址是 %d " %id(a))


# 调用test函数，本质上传递的是保存参数的引用，而不是保存的参数本身
c = test(a)
print("接受的返回结果是：%d" %id(c))
