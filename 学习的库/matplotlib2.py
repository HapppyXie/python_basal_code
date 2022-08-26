# Athour:Mr Xie
# 开发时间:2021/12/13 19:54
import matplotlib.pyplot as plt
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# #plt.bar(x=x_data, height=y_data )#绘制柱状图plt.bar()
# #plt.barh(y=x_data,width=y_data) #x轴表示y轴
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.bar(x=x_data, height=y_data,width=0.3, color='yellow', edgecolor='red', label='The First Bar', lw=3)
# plt.legend(loc='upper left')#设置图例
#
# plt.ylabel('Missing Rate(%)', fontsize=10)
# plt.title('生产总值', fontsize=10)
# plt.xlabel('年份', fontsize=10)
# plt.show()



# 多个柱值叠加
# import matplotlib.pyplot as plt
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# plt.bar(x_data, y_data)
# plt.bar(x_data, y_data2)
# plt.legend()
# plt.show()


# 多个柱并列
import numpy as np
import matplotlib.pyplot as plt
# x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
# x_range = np.arange(7)
# y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
# y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
# plt.bar(x=x_range, height=y_data, width=0.3, tick_label=x_data)
# plt.bar(x=x_range+0.3, height=y_data2, width=0.3)
# plt.show()



#绘制直方图plt.hist（）
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(10000)
print(data)
plt.hist(data, bins=100)#plt.hist(data, bins=箱子数)
plt.show()


