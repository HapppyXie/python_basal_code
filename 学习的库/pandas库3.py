# Athour:Mr Xie
# 开发时间:2021/12/10 12:47
'''
DataFrame

'''
#代替
import pandas as pd
data1 = {'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]}
data2 = pd.DataFrame(data1)
print(data2)
print('--------------------')
print(data2.replace(1,5)) # 把所有values1替换为5
print('--------------------')
print(data2.replace([1,2],[5,6]))  #1->5，2->6

#删除
print(data2.drop(5,axis=0)) # 删除索引为5的行
data3 =data2
data3.drop(3,inplace=True)
print('--------------------')
print(data3) # 原地删除

print('--------------------')
#缺失值处理
d = {'A':[20,26,63,69],
         'B':['2013-01-01','2013-01-02','2013-01-03','2013-01-04'],
         'C':[1.0,2.0,3.0,4.0],
         'D':[3,3,3,3],
         'E':['test','train','test','train'],
         'F':['foo','foo','foo','foo']}
dk = pd.DataFrame(d)
dk.index=['zhang','li','zhou','wang']

#增加
print(dk)
print('--------------------')
dk1 = dk.reindex(columns=list(dk.columns)+['G'])
print(dk1)              #假设新增的一列为缺失值z然后再把缺失值补上

print('---------修改指定位置元素值，该列其他元素为缺失值NaN------------')
# 修改指定位置元素值，该列其他元素为缺失值NaN
dk1.iat[0,6] = 3
dk1.iat[1,6] = 3
print(dk1)
# 测试缺失值，返回值为True/False阵列
print(pd.isnull(dk1))
print('---------返回不包含缺失值的行------------')
# 返回不包含缺失值的行
print(dk1.dropna())
print('---------使用指定值填充缺失值------------')
# 使用指定值填充缺失值
dk1['G'].fillna(5,inplace=True)
print(dk1)
print('----------------------')

#重复值处理
d1 = pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})
print(d1)
print('---------检查重复行---------')
print(d1.duplicated())

print('---------返回新数组，删除重复行---------')
print(d1.drop_duplicates())
print('----------删除k1列的重复数据---------')
print(d1.drop_duplicates(['k1']))
print('------删除k1列的重复数据,保留最后重复列---------')
print(d1.drop_duplicates(['k1'],keep='last'))

