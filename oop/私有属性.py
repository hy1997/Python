"""
私有属性 和私有方法  前面加两个下划线就可以了（__）,想要调用 可以加类名  women.Women__secret()
java 是在 属性 或者 方法 前面加 private 关键字
class{
    private  String age ：

    private secret(){

    }
}

"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 23

    def __secret(self):
        print("%s 的年龄是 %s" % (self.name, self.__age ))


women = Women("huyi")

# women.secret()

women.__Women.secret()
