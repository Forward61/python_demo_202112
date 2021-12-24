class Person:
    num =1
    def sayHello(self):
        print("hello!")

p = Person()
p.sayHello()

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
    def __del__(self):
        print("complex不存在了")
x=Complex(3.0,-4.5)
print(x.r,x.i)
print(x)
del x