# Athour:Mr Xie
# 开发时间:2021/12/10 13:55
#异常值处理
import numpy as np
import pandas as pd
data = pd.DataFrame(np.random.randn(500,4)) #500行，4列的样本
print(data.describe())
print('-----------------')

col2 = data[2]# 第2列
print(col2[col2>1.0]) # 该列中大于1.0的数值
print('--------任意一列中有大于3的数值的行---------')
print(data[(data>3).any(1)])

'''
sign()是Python的Numpy中的取数字符号（数字前的正负号）的函数
'''
# 把所有数据都限定到[-2.5, 2.5]之间
data[np.abs(data)>2.5] = np.sign(data)*2.5
print('---把所有数据都限定到[-2.5, 2.5]之间----')
print(data.describe())

'''
数据离散化
Python实现连续数据的离散化处理主要基于两个函数：
1.pandas.cut根据指定分界点对连续数据进行分箱处理，

2.pandas.qcut可以指定箱子的数量对连续数据进行等宽分箱处理
（注意：所谓等宽指的是每个箱子中的数据量是相同的）
'''
from random import *
d = [randint(1,100) for x in range(10)]
print('-----------生成随机数据------------')
print(d)
category = [0,25,50,75,100]
print('----------pd.cut()--------------')
print(pd.cut(d,category))

print('-----------指定标签------------')
labels = ['low','middle','high']
category = [0,50,75,100]
print(pd.cut(d,category,labels=labels))


'''
2.pandas.qcut可以指定箱子的数量对连续数据进行等宽分箱处理
（注意：所谓等宽指的是每个箱子中的数据量是相同的）
'''
print('-------pd.qcut()--------')
print(pd.qcut(d,4)) #4个箱子