# Athour:Mr Xie
# 开发时间:2021/12/13 20:38
import numpy as np
import matplotlib.pyplot as plt
#多个图形在一起显示
# x = np.linspace(0, 2*np.pi, 500)
# y = np.sin(x)
# z = np.cos(x*x)
# plt.figure(figsize=(8,4))
# # 标签前后加$将使用内嵌的LaTex引擎将其显示为公式
# plt.plot(x,y,label='$sin(x)$',color='red',linewidth=2)
#   # 红色，2个像素宽
# plt.plot(x,z,'b--',label='$cos(x^2)$')
# # 蓝色，虚线
# plt.xlabel('Time(s)')
# plt.ylabel('Volt')
# plt.title('Sin and Cos figure using pyplot')
# plt.ylim(-1.2,1.2)
# plt.legend()                                         # 显示图例
# plt.show()


#绘制三维图形
# Matplotlib 的 3D 绘图函数 plot_surface，真的非常强大，
# 图片质量可以达到出版级别，而且 3D 图像可以旋转
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
# x,y = np.mgrid[-2:2:20j, -2:2:20j]        # 步长使用虚数
#                                           # 虚部表示点的个数
#                                           # 并且包含end
# z = 50 * np.sin(x+y)                      # 测试数据
# ax = plt.subplot(111, projection='3d')    # 三维图形
# ax.plot_surface(x,y,z,rstride=2, cstride=1, cmap=plt.cm.Blues_r)
# ax.set_xlabel('X')                        # 设置坐标轴标签
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.show()


import pylab as pl
import numpy as np
import mpl_toolkits.mplot3d
# rho, theta = np.mgrid[0:1:40j, 0:2*np.pi:40j]
# z = rho**2
# x = rho*np.cos(theta)
# y = rho*np.sin(theta)
# ax = pl.subplot(111, projection='3d')
# ax.plot_surface(x,y,z)
# pl.show()

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10        # 图例字号
fig = plt.figure()
ax = fig.gca(projection='3d')               # 三维图形
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-4, 4, 100)*0.3             # 测试数据
r = z**3 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()
plt.show()
