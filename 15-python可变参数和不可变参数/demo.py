def demo(num, num_list):
    print("函数内部")
    # 赋值语句
    num = 200
    num_list = [1, 2, 3]
    print(num)
    print(num_list)
    print("调用函数代码完成")


# 在函数内部修改参数不会修改调用时传入的实参变量
gl_num = 10
gl_num_list = [4, 5, 6]
demo(gl_num,gl_num_list)
print(gl_num)
print(gl_num_list)
