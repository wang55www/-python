#coding:utf-8

class Fruit:

    pass


def add(self):
    print("grow...")

def update(self):
    print("update...")

if __name__ == "__main__":
    Fruit.grow=add
    fruit=Fruit()
    fruit.grow()
    Fruit.grow=update
    fruit.grow()