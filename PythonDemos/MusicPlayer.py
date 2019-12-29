class MusicPlayer(object):
    instance = None
    init_flg =True
    # 必须方法对象的引用
    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")

        # 判断类属性是否是空对象！
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 通过表示判断是决定初始几次
        if self.init_flg:
            print("初始化")
            self.init_flg = False
        return



print(MusicPlayer())

print(MusicPlayer())
