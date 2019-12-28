class Cat:
    def __init__(self,new_name):
        print("初始化方法")
        # self.name="Tom"
        self.name=new_name

    def __del__(self):
        print("%s 走了" %self.name)

    def __str__(self):
        # 必须要return  类似于Java里面的田toString方法
        return  "我是小猫"


cat=Cat("Tom")

print(cat)
