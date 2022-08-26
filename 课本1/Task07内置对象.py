# Athour:Mr Xie
# 开发时间:2021/12/24 15:36
x=list(range(11))
print(x)
import random
random.shuffle(x)
#sorted(x) #原地排序  sorted(排序对象，key=排序标准，reverse=True/False)
#print(x)
reversed(x)#逆序,返回reversed对象
print(x)
print(list(enumerate(x)))#枚举，返回索引和值的元组
print(list(range(0,5)))#range()  起，结，步长
print(list(zip(range(0,3),'abc')))#zip() 将多个可迭代对象压缩到一起,返回一个可迭代的zip对象
print(zip(range(0,3),'abc'))

'''
range(start,stop,step)  [start=0,stop)默认左开右闭 step默认=1
三种写法： range(stop)   range(start,stop)  range(start,stop,step)

'''

print(list(range(5)))
