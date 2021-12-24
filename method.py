import math

a=0.5
def printHello():
    print('hello')

def printNum():
    for i in range(0,10):
        print(i)

    return

def add(a,b):
    return a+b


print(printHello())

print(printNum())
print(add(1,6))


# def sum(a,n):
#     result,t=0,0
#     for i in range(n):
#         t=t*10+a
#         result+=t
#     return result
# a=int(input("输入a:"))
# n=int(input("输入n:"))
# print(sum(a,n))


def func_lib():
    def add(x,y):
        return x+y
    return add
fadd =func_lib()
print(fadd(1,6))


def f(x):
    if x==1:
        return 1
    else:
        return f(x-1)+x*x
print(f(5))


print(math.sqrt(50))
print(math.sqrt(49))