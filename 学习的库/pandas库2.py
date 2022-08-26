# Athour:Mr Xie
# 开发时间:2021/12/10 12:10
r'''
DataFrame 类型  二维带“标签”数组
DataFrame是一个表格型的数据结构，每列值类型可以不同
DataFrame既有行索引也有列索引
DataFrame常用于表达二维数据，也可以表达多维数据

构建DataFrame的办法有很多，最常用的一种是直接传入一个字典：
'''
import pandas as pd
#创建
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000, 2001, 2002, 2001, 2002],
      'pop':[1.5, 1.7, 2.6, 2.4, 2.9]}
df = pd.DataFrame(data)
print(df)
print(df.head()) #默认查看前5行
print(df.head(3))  #查看前3行
print(df.tail(2))  #默认查看后5行，查看后2行
print('----------------')

#）构建DataFrame的办法有很多,可以从二维ndarray对象创建
# import numpy as np
# d = pd.DataFrame(np.arange(10).reshape(2,5))
# print(d)

# 查看
#df.index索引-行
print(df.index)
#df.columns列
print(df.columns)
#df.values数据
print(df.values)
print('-----------------')


#查看数据的统计信息
print(df.describe()) #mean平均值、std标准差、最小值、最大值等信息
print('------------------')



#数据选择 按条件选择
print(df[df.year>2001])
print('---------按条件选择---------')
print(df[df['state']=='Ohio'])
print('---------也可完全按数字索引-----------')
print(df[0:2])#0-2行，全部列


print('--------.loc切边---按行,列标签()索引-------')
#数据选择—— .loc 的使用   .loc[]中括号里面是先行后列，以逗号分割，
#行和列分别是行标签和列标签,支持切边
print(df.loc[0,'state'])
print('------------------------')
print(df.loc[0:2,'state'])
print('--------------------')
print(df.loc[:,'year':'pop'])
print('--------------------')



'''
—— . iloc的使用 .iloc[] 根据 行数 与 列数 来索引，
    中括号里面也是先行后列，行列标签用逗号分割
'''
print('----------.iloc----数字--------')
print(df.iloc[0])#第0行
print('-----------------')
print(df.iloc[0,0])#第1行第1个
print('-----------------')
print(df.iloc[0:3,0:2])# 第1-3行的第1-2行
print('----------------------')
#指定列最大的前3行
d = {'A':[20,26,63,69],
         'B':['2013-01-01','2013-01-02','2013-01-03','2013-01-04'],
         'C':[1.0,2.0,3.0,4.0],
         'D':[3,3,3,3],
         'E':['test','train','test','train'],
         'F':['foo','foo','foo','foo']}
dk = pd.DataFrame(d)
dk.index=['zhang','li','zhou','wang']
#返回指定列最大的前3行
print('----------返回指定列最大的前3行------------')
print(dk.nlargest(3,['C']))






# 改 二维数据的索引、列名修改
df.index=['a','b','c','e','d']
#df.columns=[1,2,3]
print(df)

#排序  axis=0按行排，axis=1按列排    ascending=False降序  ascending=True升序
df.sort_index(axis=0, ascending=False)
print(df)

data1 = {'A':[20,26,63,69],
         'B':['2013-01-01','2013-01-02','2013-01-03','2013-01-04'],
         'C':[1.0,2.0,3.0,4.0],
         'D':[3,3,3,3],
         'E':['test','train','test','train'],
         'F':['foo','foo','foo','foo']}
df1 = pd.DataFrame(data1)
df1.index=['zhang','li','zhou','wang']
print(df1)
#可以使用by=['A','B']按多列进行排序
df1.sort_values(by='A')
