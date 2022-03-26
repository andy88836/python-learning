# 最常使用的场景就是在重写父类方法时，调用在父类中封装的方法实现

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

class XiaoTianQuan(Dog):
    def fly(self):

        print("我会飞")



    def bark(self):
        # 1,针对子类特有的需求，编写代码
        print("叫的跟神一样")
        # 2，使用super（），调用原本在父类中封装的方法
        super().bark()
        # 3，增加其他子类的代码
        print("%^%%%^^^^&&&")

wangcai = Dog()
wangcai.eat()
xtq = XiaoTianQuan()
xtq.bark()
