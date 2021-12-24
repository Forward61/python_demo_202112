
# print(1)
# list=[]
# for x in range(1,10):
#     list.append(x*x)
#     print(list)
#
# print(list[2])
#
# l=[x*x for x in range(1,11) if x%2==0]
# print(l)
#
# L=['Hello','World','IBM','Apple']
# print(L)
#
# l2=[s.lower() for s in L]
# print(l2)
# d={'x':'A','y':'B','z':'C'}
# for k, v in d.items():
#     print(k,'键=',v, end=";")
# # l3=[k+'=']
#
# print('\n')
# tup1=('c','v',1,5)
# print(tup1)
# tup2=(50,)
# print(tup2)
# print(tup1[2])
#


dict = {'name':'wang','age':'15','class':'一班'}
print(dict['name'])
# print(dict['aaa'])报错
dict['age']=18
print(dict)
del dict['age']
print(dict)

# dict.clear()
# print(dict)
# del dict
# print(dict)

print('age' in dict)
print('name' in dict)
print(dict.values())
for key,value in dict.items():
    stu = {'tom', 'jim', 'jerry'}
    print(stu)

    print(key,value)


stu= {'tom','jim','jerry'}
print(stu)
nullset =set()
print(nullset)
if('Rose' in stu):
    print("in")
else:
    print("not in ")
if('tom' in stu):
    print('in')

a=set('abcd')
b=set('edfd')
print(a)

print(a|b)
print(a&b)
print(a-b)
print(a^b)