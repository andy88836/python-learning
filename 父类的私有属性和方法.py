
"""
子类对象可以通过父类的公有方法间接访问到私有属性或私有方法
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的共有方法%d" % self.__num2)
        self.__test()

class B(A):
    def demo(self):

        #1在子类对象方法中，不能访问父类的私有属性

        #2,在子类对象方法中，不能调用父类私有方法
        #3.访问父类的公有属性
        print("子类方法 %d"% self.num1)
        #4.调用父类的公有方法
        self.test()



b = B()
print(b)
b.demo()
print(b.num1)
b.test()

# print(b.__num2)
# b.__test
