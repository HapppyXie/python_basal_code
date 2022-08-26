# Athour:Mr Xie
# 开发时间:2021/12/13 20:23
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#绘制子图plt.subplot（）
# 画第1个图：折线图
# x=np.arange(1,100)
# plt.subplot(211)#两行一列第一个图
# plt.plot(x,x*x)
#
# # 画第2个图：散点图
# plt.subplot(212)#两行一列第二个图
# plt.scatter(np.arange(0,10), np.random.rand(10))
# #显示
# plt.show()

x= np.arange(1,100)#生成1-99的整数
plt.subplot(221)
plt.plot(x,x*x)

plt.subplot(222)
plt.scatter(np.arange(0,10),np.random.rand(10))

plt.subplot(223)#画第三图，前面的两个图占了221和222的位置，如果下面只放一个plt.subplot(212)
plt.pie(x=[12,30,45,13],labels=list('ABCD'))

plt.subplot(224)
plt.bar([20,10,30,25,15],[25,15,35,30,20],color='b')

plt.show()