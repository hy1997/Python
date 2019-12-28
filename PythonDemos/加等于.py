def demo(num, num_list):
    num += num
    # 函数执行后外部会发生变化
    # num_list += num_list
    num_list = num_list + num_list

    print(num)
    print(num_list)
    print("函数调用完成")


gl_num = 9

gl_list = [1, 2, 3]

demo(gl_num,gl_list)

print(gl_num)
print(gl_list)
