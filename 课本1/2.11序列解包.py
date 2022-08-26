# Athour:Mr Xie
# 开发时间:2021/10/18 20:20
'''
序列封包：多个值赋给一个变量或序列
序列解包：把一个序列或变量赋给一个值
'''
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
v_tuple = (False, 3.5, 'exp')
(x, y, z) = v_tuple
print(x)
print(y)
print(z)
print('------')
x, y, z = range(3)
print(x)
print(y)
print(z)
print('------')
x, y, z = map(str, range(3))
print(x)
print(y)
print(z)
print('------')
# 交换两个两个变量的值
a, b = 10, 20
print(a,b)
a, b = b, a
print(a, b)
print('------')
a = {'a': 1, 'b': 2, 'c': 3}
x, y, z = a
print(x)    #字典默认读key,而且无序
print(y)
print(z)
print('------')
x, y, z = a.items()
print(x)
print(y)
print(z)
print('------')
a, b, c = 'ABC'
print(a, b, c)
print('------')
x = ['a', 'b', 'c']
for i, v in enumerate(x):
    print('The value on position {0} is {1}'.format(i, v))
print('------')
s = {'a': 1, 'b': 2, 'c': 3}
for k, v in s.items():
    print((k, v), end=' ')
print()
print('------')
for item in s.items():
    print(item[0])   #设置的参数可以用切边
print('------')
for item in s.items():
    print(item[1])

