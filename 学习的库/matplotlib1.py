# Athour:Mr Xie
# 开发时间:2021/12/13 19:23
'''
matplotlib是python最著名的绘图库，模块依赖于numpy模块和tkinter模块
matplotlib.pyplot是绘制各类可视化图形的命令子库，提供了和matlab类似的绘图API

'''

# x=[3,1,4,5,2]
# plt.figure(figsize=(8,4))#绘画窗口设置绘画窗口大小
# plt.xlabel("xlabel")
# plt.ylabel("ylabel")
# plt.rcParams['font.sans-serif']=['SimHei']#plt.rcParams['font.sans-serif']=['字体']
# plt.title("博哥的流量")
# plt.axis([-1,10,0,6])#x，y坐标轴尺寸
# plt.plot(x,'--1b')#绘制折线图plt.plot（参数x,参数y,'风格，标记，颜色字符',........）可放多个图
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 2.0*np.pi, 0.1)  #x轴数据
y = np.cos(x)             #y轴数据
plt.scatter(x,y,s=40,linewidths=6,marker='+')#plt.scatter()绘制散点图
plt.show()

# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif']=['SimHei']     #用来正常显示中文标签
# labels = ['娱乐','育儿','饮食','房贷','交通','其它']
# sizes = [2,5,12,70,2,9]
# explode = (0,0,0,0.1,0,0)#部分图形分离
# plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)#绘制饼状图plt.pie（）
# plt.title("饼图示例-8月份家庭支出")#
# plt.axis('equal')
# plt.legend(loc="upper right", fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
# plt.show()
'''
上面的图形为椭圆形，可加入以下一条命令将之显示为长宽相等的饼图。
plt.axis('equal')   #该行代码使饼图长宽相等
添加图例
plt.legend(loc="upper right", fontsize=10,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
'''
