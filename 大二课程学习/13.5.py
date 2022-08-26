# Athour:Mr Xie
# 开发时间:2021/12/13 19:14
#5.绘制饼图
import matplotlib.pyplot as plt
labels = 'Frogs','Hogs','Dogs','Logs'
sizes=[15,30,45,10]
plt.figure(figsize=(8,6))
plt.rcParams['font.sans-serif']=['SimHei']
plt.title("title of plot")
explode = (0,0,0,0.1)#部分图形分离
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.legend(loc="upper right", fontsize=15,bbox_to_anchor=(1.1,1.05),borderaxespad=0.3)
plt.axis('equal')
plt.show()