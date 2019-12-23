# 如果在函数内部用方法修改   可变参数 内容 ， 是会影响到外部的数据
def demo( num_list):
    print("函数内部")
    # 赋值语句
    num_list.append(9)
    print(num_list)
    print("调用函数代码完成")


gl_num_list = [4, 5, 6]
demo(gl_num_list)
print(gl_num_list)
