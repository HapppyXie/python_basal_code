# Athour:Mr Xie
# 开发时间:2021/12/10 16:22
#DataFrame 分组与聚合
#分组  groupby
import pandas as pd
import numpy as np
#from random import *
df1 = pd.DataFrame({'A':np.random.randint(1,5,8), #随机1-5的整数8个
                    'B':np.random.randint(10,15,8),
                    'C':np.random.randint(20,30,8),
                    'D':np.random.randint(80,100,8)})
print(df1)
print('--------数据分组计算-----------')
print(df1.groupby('A').sum()) #以A的数据为组别，分组计算

print('---------分别以A，B的数据为组别，分组计算平均值------------')
print(df1.groupby(['A','B']).mean())

group=df1.groupby(['A'])
print(group) #gruop对象地址
print('--------A分组后，多个1,2,3,4组里，最大的那组----------')
print(group.max())
print('--------------求A的分组里最大的那组的分组------------------')
print(group.aggregate(max))

'''
聚合 aggregate
DataFrame.aggregate()函数的主要任务是将聚合应用于一个或多个列。最常用的聚合是：
sum：用于返回所请求轴的值之和。
min：用于返回所请求轴的最小值。
max：用于返回所请求轴的最大值。
DataFrame.aggregate(func, axis=0, *args, **kwargs)
'''
df = pd.DataFrame({'A':np.random.randint(1,5,8),
                   'B':np.random.randint(10,15,8),
                   'C':np.random.randint(20,30,8),
                   'D':np.random.randint(80,100,8)})
print('---------aggregate------------')
print(df.aggregate(['sum','max','min','mean']))

#CSV文件读写
# #将df数据保存为csv文件
#pd.read_csv('filename',header=None,sep=' ')
# df.to_csv(r'C:\Users\mike\Desktop\test.csv')
# # 读取csv文件中的数据
# dd = pd.read_csv(r'C:\Users\mike\Desktop\test.csv')
# print(dd)