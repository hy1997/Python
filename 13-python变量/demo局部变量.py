# 全局变量
num = 20


def demo():
    # 局部变量  生命周期就是这个函数的内部 执行玩这个函数后变量就被系统回收了
    # 不同函数之间相同的的局部变量（名称相同） 是没有影响的！
    # Java里面也有局部变量 也是在方法的内部才会有效（和python的函数一样）
    """
    Java 代码
        public class Demo{
            // 全局变量
            private static  String num = 20

            public  void   demo(){
                // 局部变量
                private  String  name  =10;
            }
        }
    """
    a = 10
    print("%d" % a)
    print("%d" % num)


def demo1():
    print("%d" % num)

demo()

print()
