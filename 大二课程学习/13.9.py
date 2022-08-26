# Athour:Mr Xie
# 开发时间:2021/12/14 21:44
#9. 读取下表数据，选择相关的变量， 画折线图、散点图、柱状图(bar)、条形图(bar)、饼图、箱线图（boxplot）等 6个图
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(10,8))

#读取数据
df = pd.read_csv(r'C:\Users\mike\Desktop\salary.csv',encoding='utf-8')
print(df.columns)
print(df.values)

p1 = df.loc[0:5,'姓名']
p2 = df.loc[0:5,'实发工资']
# plt.subplot(221)
# plt.plot(p1,p2)
# plt.grid(visible='True')
# plt.title('员工工资波动折线图')
#
# plt.subplot(222)
# plt.scatter(p1,p2)
# plt.title('员工工资散点图')
#
# plt.subplot(223)
# plt.bar(p1,p2)
# plt.title('员工工资柱状图')
#
# plt.subplot(224)
# plt.hist(p2,bins=40)
# plt.title('员工工资直方图')
# plt.show()

p1 = df.loc[0:5,'姓名']
p2 = df.loc[0:5,'实发工资']
p3 = df[df.职务=='经理'].loc[0:,'实发工资'].sum()#经理实发工资总和
p4 = df[df.职务=='职员'].loc[0:,'实发工资'].sum()#职员实发工资总和
plt.subplot(211)
data = [p3,p4]
labels = [('经理2人实发工资总和',p3),('职员3人实发工资总和',p4)]
plt.pie(data,labels=labels,autopct='%1.1f%%')
plt.title('经理和职员实发工资饼状图')

plt.subplot(212)
plt.boxplot(p2)
plt.title('员工工资箱线图')
plt.show()


