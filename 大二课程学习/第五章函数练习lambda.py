# Athour:Mr Xie
# 开发时间:2021/10/30 13:57
'''
格式： lambda 参数: 执行语句
'''
f = lambda x, y, z: x+y+z
print(f(1, 2, 3))

g = lambda x, y=2, z=3: x+y+z
print(g(2))
print(g(1, 2, 3))

l = [(lambda x: x**2), (lambda x: x**3), (lambda x: x**4)]
for i in range(3):
    print(l[i](2), end=' ')
print()
print(l[0](2), l[1](2), l[2](2))

d = {'f1': (lambda: 2+3), 'f2': (lambda: 2*3), 'f3': (lambda: 2**3)}
for i in d:
    print(d[i](), end=' ')
print()
print('------------')
import random
q = [random.randint(1,10) for i in range(10)]
print(q)
o = list(map(lambda x: x+10, q))
print(o)

def demo3(n):
    return n*n
print(demo3(10))
#lambda 表达式中调用定义函数
a_list = [random.randint(1,5) for i in range(5)]
print(a_list)
b_list = list(map(lambda x: demo3(x), a_list))
print(b_list)
print('--------------')

data = list(range(20))
random.shuffle(data)
print(data)
print('--------------')
data.sort(key = lambda x:x)   #用列表的每个元素作为参数
print(data)
print('--------------')
data.sort(key = lambda x: len(str(x)))
print(data)                   #用列表的每个元素的字符长度作为排序标准
print('--------------')
data.sort(key = lambda x: len(str(x)), reverse = True)
print(data)
print('--------------')

r = []
#for x in range(10):      由于变量的作用域，此处x 无法被lambda内的x接受，返回的是
 #   r.append(lambda X: x**2)
#for i in r:
 #   print(i)
#修改后可以
for i in range(10):
    r.append(lambda n=i: n**2)
for q in r:    #存储进去的是[lambda n=0: n**2, lambda n=1: n**2, lambda n=2: n**2..........]
    print(q, end=' ')   #所以没有赋值打印出来的是列表里lambda表达式的地址
print()
print(r[0]())  #没有赋值()，返回默认值平方， 赋值(9)，计算所赋值的平方,  没有使用()相当于没有调用lambda函数
print(r[0](1))
print(r[0](9))
print(r[1]())
print(r[1])


