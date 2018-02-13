#coding:utf-8
class Fruit:
    price = 0  # 类变量

    def __init__(self):
        self.__color = "red"  # 定义私有变量

    def getColor(self):
        print(self.__color)  # 打印私有变量

    @classmethod
    def getPrice(cls):
        print(cls.price)

    def __getPrice(cls):  # 定义私有函数
        cls.price = cls.price + 10
        print(cls.price)

    count = classmethod(__getPrice)  # 使用staticmethod方法定义静态方法


if __name__ == "__main__":
    apple = Fruit()  # 实例化apple
    apple.getColor()  # 使用实例调用静态方法
    apple.count()
    apple.getPrice()
    Fruit.count()  # 使用类名调用静态方法
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
