# Athour:Mr Xie
# 开发时间:2021/10/29 15:15
def myMap(iterable, op, value):
     if op not in '+-*/':
         return 'Error operator'
     def nested(item):
         return eval(repr(item)+op+repr(value))
     return map(nested, iterable)
print(list(myMap(range(5), '+', 5)))
print(list(myMap(range(5), '-', 5)))
print(list(myMap(range(5), '*', 5)))
print(list(myMap(range(5), '/', 5)))


'''
参数：位置参数

'''
def demo(a, b, c):
    print(a, b, c)
demo(8, 9, 10)

'''
默认值参数 
'''
def say(message, times=1):
    print((message+' ')*times)
say('啊哈哈哈哈哈')
say('啊哈哈哈哈哈', 9)
#print(say.__default__)


def demo2(newitem, old_list=None):
    if old_list is None:
        old_list = []
    old_list.append(newitem)
    return print(old_list)
demo2(4)

'''
关键参数
'''
def add(a, b):
    return print(a+b)
add(a=10, b=200)
add(b=201, a=89)
'''
可变长度参数

1.多个位置参数的接收
2.多个关键参数的接收
'''
x = []
def x_list_add(*p):
    for i in p:
        x.append(i)
    return print(x)
x_list_add(1, 2, 3, 6, 90)
print(x)

y = []
def dict_add(**p):
    for i in p.values():
        y.append(i)
    return print(y)
dict_add(a=1, b=2, c=3, d=4)

'''
传递参数时的序列解包 --->实参的解包
1.位置参数的解包
2.关键参数的解包
'''
import random
def do(a, b, c, d, e, f):
    print(a-b-c-d-e-f)
z = [random.randint(1,10) for i in range(6)]
print(z)
print('-----------------')
do(*z)
print('-----------------')
w1 = [random.randint(1, 10) for i in range(6)]
w2 = ['a', 'b', 'c', 'd', 'e', 'f']
w3 = {}
for i in range(6):
    w3.setdefault(w2[i], w1[i])
print(w3)
print('-----------------')
do(**w3)