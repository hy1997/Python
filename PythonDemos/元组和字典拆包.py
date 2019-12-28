def demo(*args, **kwargs):
    print(args)
    print(kwargs)


gl_num=(1, 2,3)

gl_dict={"name": "huyi","age": "32"}


demo(gl_num, gl_dict)
# 简化开发 元组前面加一个* 字典后面加两个**
demo(*gl_num,**gl_dict)
