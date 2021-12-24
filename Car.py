class Car:
    price=10000
    def __init__(self,c,w):
        self.color =c
        self.__w2=w

car1=Car("red",10.5)
car2= Car("blue",11.9)
print(car1.color)
print(car1._Car__w2)
# print(car1.__w2)
