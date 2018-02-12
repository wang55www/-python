# coding:utf-8
# 类的创建
class Fruit:
    price=0
    def __init__(self,name,color):           # __init__为类的构造函数，后面会详细介绍
        self.name = name
        self.color = color
    def grow(self):             # 定义grow函数，类中的函数称为方法
        print "Fruit grow ..."

if __name__ == "__main__":
    fruit = Fruit('name','red')               # 实例化
    fruit.grow()                # 调用grow()方法
    print fruit.price
    apple = Fruit("apple","red")
    apple.grow()
    apple.price=9

    print apple.price
    print Fruit.price
