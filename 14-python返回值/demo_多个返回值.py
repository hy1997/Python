def demo():
    print("开始计算温度。。。")
    temp = 13
    print("结束计算温度。。。")
    print("开始计算湿度。。。")
    wetness = 50
    print("结束计算湿度。。。")
    # 返回一个元组
    return temp, wetness


result= demo()
print(result)
print("需要单独处理时、、、")
print(result[0])
print(result[1])

# 可以直接用全局变量直接接受  全局变量必须和返回的元素个数一样
gl_temp, gl_wetness = demo()
print(gl_temp)
print(gl_wetness)
