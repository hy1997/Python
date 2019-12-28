class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shot(self):
        if self.bullet_count <= 0:
            print("枪没有子弹了！！！")
            return
        self.bullet_count = self.bullet_count -1
        print("fire ....")
        print(self.bullet_count)


class Person:

    def __init__(self, name):
        self.name = name
        self.gun = None


gun = Gun("1")

gun.add_bullet(5)

person = Person("张三")

person.gun = gun

person.gun.shot()
