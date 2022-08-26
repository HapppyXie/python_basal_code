# Athour:Mr Xie
# 开发时间:2021/12/13 19:08

#4.图中显示中文和文本
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0,5.0,0.02)
y=np.cos(2*np.pi*x)
plt.figure(figsize=(8,6))
plt.xlabel("横轴",fontproperties="SimHei",fontsize=25,color="green")
plt.ylabel("纵轴",fontproperties="SimHei",fontsize=25,color='red')
plt.title(r'正炫波 $y=cos(2\pi x)$',fontproperties='SimHei',fontsize=25)
plt.text(2,3,r'$\mu=100$',fontsize=15)
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.plot(x,y,'-ob')
plt.show()