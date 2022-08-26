# Athour:Mr Xie
# 开发时间:2021/12/14 19:49
import numpy as np
# 单位矩阵
print(np.identity(3))
print(np.eye(3))
print(np.ones((5,3)))
# 对角矩阵
print(np.diag([1,2,3,4]))

#改变数组大小
a = np.arange(1, 11, 1)
print(a)
a.shape = 2,5
print(a)
a.shape=5,2#= a.reshape(2,5) # reshape()方法返回新数组
print(a)

#改变数组元素值
x=np.arange(8)
print(x)
print(np.append(x,8))
x[3]=8#原地修改
print(x)
print(np.insert(x,1,8))#np.insert(x,索引，插入数据)

#一维数组索引、切片
print('-----------------')
print(x[3])
print(x[3:6])
print(x[:5])
print(x[0:])
print(x[::-1])

