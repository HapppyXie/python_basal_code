# Athour:Mr Xie
# 开发时间:2021/12/10 9:47
import pandas as pd
#读入数据
df = pd.read_csv(r'C:\Users\mike\Desktop\salary.csv',encoding='utf-8')
print('--------------查看前三行--------------------')
print(df.head(3))
print('--------------查看后两行--------------------')
print(df.tail(2))
print('--------------查看索引和值--------------------')
print(df.index)
print(df.columns)
print(df.values)

print('----按应发工资大小排序，找出工资最高的3人-----')
print(df.nlargest(3,['实发工资']))

print('----基本工资>3000的人的姓名-----')
d = df[(df['基本工资']>3000.0)]
print(d['姓名'])

print('-----基本工资3000-6000的人的信息------')
df1 = df[(df['基本工资']>=3000.0)]
print(df1[(df1['基本工资']<=6000.0)])

print('------显示所有人的姓名和实发工资-------')
print(df[['姓名','实发工资']])#0,5

print('------查看财务处人员的姓名和部门-------')
df2 = df[(df['部门']=='财务')]
print(df2[['姓名','部门']])

print('------查看所有数值变量的统计信息（平均值、标准差、最小值、最大值、25%、50%、75%等信息）-------')
print(df.describe())

print('------查看基本工资的平均值、最大值-------')
print('基本工资平均值：',df['基本工资'].mean())
print('基本工资最大值：',df['基本工资'].max())

print('----按部门分组，显示分组后的各组人员的所有信息，计算各组人数、各组应发工资的最大值----')
df3 = df.groupby('部门')
l = list(df3)
for i in l:
    print(i)
    print()
print('----------')
print('人数',df3['姓名'].count())
print('----------')
print('应发工资最大值：',df3['应发工资'].max())

print('----按部门、职务分组，计算各组所有数值列的平均值----')
print(df.groupby(['部门','职务']).mean())

print('----查看聚集函数aggregate的结果----')
print(df.iloc[:,3:].aggregate(['sum','max','min','mean']))
