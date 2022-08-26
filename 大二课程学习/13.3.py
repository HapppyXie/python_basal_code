# Athour:Mr Xie
# 开发时间:2021/12/13 19:06
#3.一张图上，绘制多个线条
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
print(x)
plt.figure(figsize=(8,6))
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title of lpot")
plt.plot(x,x*1.5,'go-', x,x*2.5,'rx',x,x*3.5,'*',x,x*4.5,'b-.')
plt.show()