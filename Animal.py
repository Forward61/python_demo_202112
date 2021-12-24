class animal:
    def run(self):
        print('animal is runnig')
class Cat(animal):
    def run(self):
        print('cat is running')
class Dog(animal):
    def run(self):
        print('dog is run')

c=Dog()
c.run()


a=list()
b=animal()

print(isinstance(a,list))
print(isinstance(b,list))
print(isinstance(b,animal))
print(isinstance(c,Dog))
print(isinstance(c,animal))