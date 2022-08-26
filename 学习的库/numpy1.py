# Athour:Mr Xie
# 开发时间:2021/12/14 19:28
'''
用于数据分析、科学计算与可视化的扩展模块主要有：numpy、scipy、pandas、
SymPy、matplotlib、Traits、TraitsUI、Chaco、TVTK、Mayavi、VPython、OpenCV。

用于数据分析与科学计算可视化的模块有很多：
statistics提供了一些常用的统计分析的函数，
numpy科学计算包作数值计算扩展库(将python当成matlab来用)，
scipy作为numpy的拓展，
pandas提供了高效地操作大型数据集所需的工具
matplotlib做数据可视化。

NumPy(Numerical Python) 是一个开源的 Python 科学计算基础库，主要用于数组计算，包含：
一个强大的N维数组对象 ndarray
广播功能函数
整合 C/C++/Fortran 代码的工具
线性代数、傅里叶变换、随机数生成等功能

'''

# ndarray（数组）是存储单一数据类型的多维数组。
# ndarray是一个多维数组对象，由两部分构成：
#       实际的数据
#        描述这些数据的元数据（数据类型、数据维度等）
#创建多维数组    numpy.array([[],[],[]])
import numpy as np
a = np.array([[0,1,2,3,4],[9,8,7,6,5]])# 2行5列
print(a)

#a.ndim数组维度  a.shape数组尺寸tuple(行，列) a.size元素总数：行*列
# a.dtype 数组元素类型    a.itemsize数组的每个元素的大小（以字节为单位）
#创建n维数组对象

print(a.ndim)
print(a.shape)

# 把列表转换为数组
print(np.array([1, 2, 3, 4, 5]))
# 把元组转换成数组
print(np.array((1, 2, 3, 4, 5)))
# 二维数组
print(np.array([[1, 2, 3], [4, 5, 6]]))

# 类似于内置函数range()
print(np.arange(1, 10, 2))

# 全0一维数组
print(np.zeros(3))
# 全1一维数组
print(np.ones(3))
# 全0二维数组，3行3列
print(np.zeros((3,3)))
