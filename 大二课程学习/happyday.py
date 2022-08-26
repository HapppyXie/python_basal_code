# Athour:Mr Xie
# 开发时间:2021/10/1 12:09
for i in range(1, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', j*i, end='  ,  ')
    print()
    print('--------------------------------------------')


s = 0
for w in range(1, 101):
    s += w
print(s)


s2 = 0
for count in range(1, 51):
    s2 += 2*count-1

print(s2)

import random
def add(x,y):
    return x+y
x = list(map(add, range(10), range(10)))
print(x)

y = add(15, 39)
print(y)
print(add(0, 20))

print(list(zip('abcd', [1, 2, 3, 4])))

a = 15
d = a if a > 20 else 60 #三元运算
print(d)



