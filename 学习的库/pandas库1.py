# Athour:Mr Xie
# 开发时间:2021/12/10 10:10
r'''
Pandas(Python Data Analysis Library )是Python第三方库
pandas含有使数据分析工作变得更快更简单的高级数据结构和操作工具。它是基于NumPy构建的，让以NumPy为中心的应用变得更加简单。
Pandas更关注数据的应用，建立数据与索引间的关系

主要数据结构：
1）Series，带标签的一维数组；
2）DataFrame，带标签且大小可变的二维表格结构；


'''
import pandas as pd
a = pd.Series([1,2,3,4])
print(a)
print('-----------')
#可以自己定义索引
b = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(b)
#b.values获取数据  b.index获取索引
print(b.values)
print(b.index)
#支持单个索引，和自定义索引查询
print(b[0])
print(b['a'])

print(b[[0,3]])#查询索引为0，3的数据，这种查询，不管行还是列，均可
print('-----------')   #注意要[[]]
print(b[['a','d']])

print('-------------')
#支持切边，跨步切边
c = pd.Series([9,8,7,6,5,4,3,2,1],index=['a','b','c','d','e','f','g','h','f'])
print(c[1:8:2])
print('-------------')
print(c['b':'h':2])
print('-------------')
d1 = pd.Series([9,8,7,6],index=['a','b','c','d'])
d2 = pd.Series([1,2,3],index=['c','d','e'])
print(d1+d2)    #NaN空值,csv文本文件
print('-------------')
#索引相同，则做加法运算,索引不同无法运算，空值
d3 = pd.Series([1,2,3],index=['a','b','c'])
d4 = pd.Series([4,5,6],index=['a','b','c'])
print(d3+d4)



