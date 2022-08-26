# Athour:Mr Xie
# 开发时间:2021/12/10 15:30
#DataFrame 数据合并(merge，join，concat)
import pandas as pd
df1 = pd.DataFrame({'a':range(5),'b':range(50,55),
                    'c':range(60,65)})
print(df1)
df2 = pd.DataFrame({'a':range(3,8),'d':range(30,35)})
print(df2)
print('---创建原始数据完毕----')
#数据合并merge
print('----内连接-----')
print(pd.merge(df1,df2))
print('------右连接------')
print(pd.merge(df1,df2,how='right'))
print('-----左连接--------')
print(pd.merge(df1,df2,how='left'))
print('------外连接------')
print(pd.merge(df1,df2,how='outer'))


'''
join
join是默认按照index、
以left方式实现两个DataFrame的合并，
默认左外连接how=left
'''
df1 = pd.DataFrame({'A':['A0','A1','A1'],
                    'B':['B0','B1','B1']},
                   index=['k0','k1','k2'])
df2 = pd.DataFrame({'C':['C1','C2','C3'],
                    'D':['D0','D1','D2']},
                   index=['K0','K1','K3'])
print('-------生成数据--------')
print(df1)
print('----------------------')
print(df2)
print('----------默认左连接------------')
df3 = df1.join(df2)
print(df3)#默认左连接
df4 = df1.join(df2,how='outer')
print('-----------外连接-----------')
print(df4)
print('-----------内连接-----------')
df5 = df1.join(df2,how='inner')
print(df5)
print('----------------------')

'''
数据合并Concat:制定按某个轴进行连接（可横向可纵向），
concat是单纯的对DataFrame进行堆叠，并且空值填充为NaN

属性                      描述
objs           合并的对象集合。可以是Series、DataFrame
axis        合并方法。默认0，表示纵向，1横向
join        默认outer并集，inner交集。只有这两种 
join_axes   按哪些对象的索引保存
ignore_index    默认Fasle忽略。是否忽略原index

'''
df1 = pd.DataFrame({'A':['A0','A1','A1'],
                    'B':['B0','B1','B1']},
                   index=['k0','k1','k2'])
df2 = pd.DataFrame({'C':['C1','C2','C3'],
                    'D':['D0','D1','D2']},
                   index=['K0','K1','K3'])
df3 = pd.concat([df1,df2])
print(df3)
df4 = pd.concat([df1,df2],join='inner')
print(df4)

print('------------------')
d1=pd.DataFrame({'学号':['one','two','two'],
                 '分数':[0,1,2]})
d2 =pd.DataFrame({'学号':['one','three','three'],
                  '等级':[0,1,2]})
dk1 = pd.concat([d1,d2])#默认并集
print(dk1)
print('-------------------')
df2 = pd.concat([d1,d2],join='inner')
print(df2)