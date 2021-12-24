from typing import List
print("hello")
list3=[1,2,3]
print(list3[1])

print("list[2,3]", list3[1:5])
a= 'python'
print(a and True)
print(a and False)

print(a or False)

# list2=['中文的','us',1,2021,'lqvz','2222']
# print(list2)
# print(list2[2])
# list2[2]='ussb'
# print(list2[2])
#
# list2.remove(2021);
# print(list2)
#
# del list2[2]
# print(list2)
# list2.pop();
# print(list2)
# list2.pop(1)
# print(list2)
# list2.append("append222")
# print(list2)

l3=[['中国','美国'],['2021','2022']]
print(l3)
print(l3[1][0])
print(l3[1])

rows =3
cols=6
ddd=5
c=5
matrix=[[0 for col in range(cols)] for row in range (rows)]

for i in range(rows):
    for j in range (cols):
        matrix[i][j] = i*3+j
        print(matrix[i][j],end = " , ")

    print('\n')

# matrix2=[[3][6]];
matrix2=[[0 for col in range(cols)]for row in range(3)]
# matrix2=[[0 for col in range(cols)] for row in range (rows)]

matrix2[0][0]=2
matrix2[1][0]=3
print(matrix2)
for i in range(2):
    for j in range (cols):
        matrix2[i][j] = i * 3 + j
        print(matrix2[i][j], end=" , ")
        # matrix2[i][j]= i*3+j
        # print(matrix2[i][j],end = " , ")

    print('\n')

ls2=list((range(0,10)))
print(ls2)