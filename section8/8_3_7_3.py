#coding:utf-8
class FruitShop(object):
    "水果商店"
    def __init__(self,fruits=[]):
        self.fruits=fruits

    def __getitem__(self,item):
        return self.fruits[item]

    def __str__(self):
        return self.__doc__

    def __call__(self):    #对象可以看成一个函数来调用
        print("FruitShop call")


if __name__ == "__main__":
    shop = FruitShop(["apple","banana","pear"])
    shop()
    print(shop)

    for item in shop:
        print(item)