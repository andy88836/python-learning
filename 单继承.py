# 继承的语法： class 类名（父类名）
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")


class Dog(Animal):
    # 子类拥有父类所有的属性和方法
    # 继承具有传递性
    def bark(self):
        print("汪汪")

wangcai = Dog()
wangcai.eat()