# Athour:Mr Xie
# 开发时间:2021/12/14 21:10
#8.绘制组合图形，把5、6、7三个图画在一张图纸上
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10
matplotlib.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(10,8))

labels = 'Frogs','Hogs','Dogs','Logs'
sizes=[15,30,45,10]
plt.subplot(221)
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("title of plot")
explode = (0,0,0,0.1)#部分图形分离
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.legend(loc="upper right", fontsize=8,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
plt.axis('equal')

plt.subplot(222)
orignalData = [random.randint(20,81) for x in range(100)]
data = np.array(orignalData[4:]).reshape(8,12)#去掉4个数据，96个数据平分为8组
plt.title("title of hist")
plt.hist(data,bins=50)
plt.subplot(212)
num = 1000
x = np.random.randn(num)
y = np.random.randn(num)
plt.scatter(x, y,s=1,linewidths=6,marker='*')
plt.title("a scatter of 1000 statics")
plt.show()