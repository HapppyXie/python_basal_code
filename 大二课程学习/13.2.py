# Athour:Mr Xie
# 开发时间:2021/12/13 18:59
'''
2.绘制如下折线图
x = np.linspace(0,1)，
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0.0,1.0)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.figure(figsize=(8,6))
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title of plot")
plt.plot(x,y,'-or')
plt.show()