class Person:
    num =1
    def __init__(self,str,n):
        self.name=str
        self.age=n
    def sayHello(self):
        print("hello")
    def printName(self):
        print("姓名：",self.name)
    def printNum(self):
        print(Person.num)
p1=Person("夏天",42)
p2=Person("冬天",35)
p1.printName()
p2.printName()

Person.num=2
p1.printNum()
p2.printNum()