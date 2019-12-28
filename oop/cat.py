class Cat:

    def eat(self):
        # 那个对象调用的方法  方法内部的self就是那个对象的引用
        # 可以通过self。访问对象的属性
        # 也可以通过self调用其他的对象的方法
        
        print("小猫爱吃鱼")


    def drink(self):
        print("小猫爱和水")




tom =Cat()
tom.drink()
tom.eat()

print(tom)

a =id(tom)

print(a)




lazy_cat = Cat()
tom =Cat()
tom.drink()
print(lazy_cat)
