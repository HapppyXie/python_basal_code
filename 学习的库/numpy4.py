# Athour:Mr Xie
# 开发时间:2021/12/14 20:36
'''
广播是指不同形状的数组之间执行算术运算的方式。
当两个数组的形状并不相同的时候，
我们可以通过扩展数组的方法来实现相加、相减、相乘等操作，
这种机制叫做广播（broadcasting）
'''
import numpy as np
a = np.arange(0,60,10).reshape(-1,1)#行向量
b = np.arange(0,6)#列向量
print(a)
print(b)
print(a+b)
print(a*b)