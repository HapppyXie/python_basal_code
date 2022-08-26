# Athour:Mr Xie
# 开发时间:2021/12/13 21:17
#6.绘制直方图：生成100个20-80间随机整数，分成8组，绘制直方图
import random
import matplotlib.pyplot as plt
import numpy as np
orignalData = [random.randint(20,81) for x in range(100)]
data = np.array(orignalData[4:]).reshape(8,12)#去掉4个数据，96个数据平分为8组
plt.hist(data,bins=50)
plt.show()
