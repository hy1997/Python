class Dog:
    count = 0

    @classmethod
    def run(cls):
        # 这里是类属性
        cls.count

        print(" cls (类对象的引用) 这是一个类方法")

    @staticmethod
    def demo():
        print("这是一个静态方法")

    def test(self):
        # 实例属性
        self.count
        print("self（实例对象的引用） 只能通过Dog的实例对象来掉用方法  ")

# 类似于Java里面的静态方法
Dog.run()
Dog.demo()
Dog().test()
