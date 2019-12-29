class Animal:
    def eat(self):
        print("吃饭！！")

    def sleep(self):
        print("睡觉！！")


# 继承
class  Person(Animal):

    def eat(self):
        print("人吃饭")



print(Person().__dir__())
