# Athour:Mr Xie
# 开发时间:2021/12/13 18:58
#1.按下列代码绘折线图，x[0,2,4,6,8]，y= [3,1,4,5,2],画如下折线图
import  matplotlib.pyplot as plt
import numpy as py
import pandas as pd
x = [0,2,4,6,8]
y = [3,1,4,5,2]
plt.figure(figsize=(8,6))
plt.xlabel("Y-variable")
plt.ylabel("X-variable")
plt.title("Matplotlib demo")
plt.plot(x,y)
plt.show()