# Athour:Mr Xie
# 开发时间:2021/12/14 19:03
#7.绘制散点图。使用numpy包的random函数随机生成1000组数据，然后通过scatter函数绘制了散点图。
import numpy as np
import matplotlib.pyplot as plt
num = 1000
x = np.random.randn(num)
y = np.random.randn(num)
plt.scatter(x, y,s=1,linewidths=6,marker='*')
plt.title("a scatter of 1000 statics")
plt.show()