# Athour:Mr Xie
# 开发时间:2021/10/29 19:24
'''
4.	计算三角形面积函数，TriangleArea(x,y,z)，其中x,y,z为分别为三角形三条边，面积公式为 。
#math.sqrt()开方
'''
import math
# def calTriangleArea(x, y, z):
#     c = 1/2*(x+y+z)
#     area = math.sqrt(c*(c-x)*(c-y)*(c-z))
#     return print(area)
# while True:
#     a, b, c = eval(input('请输入三角形的三边：'))
#     if a+b <= c:
#         print('该三边不满足三角形定义！请重新输入')
#         continue
#     elif a+c <= b:
#         print('该三边不满足三角形定义！请重新输入')
#         continue
#     elif b+c <= a:
#         print('该三边不满足三角形定义！请重新输入')
#         continue
#     else:
#         calTriangleArea(a, b, c)
x=[1,2,2,3,6,1,5]
print(x.sort())#sort()原地排序，不返回任何值