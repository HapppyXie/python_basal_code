# Athour:Mr Xie
# 开发时间:2021/10/3 15:50

import math
x = input('请输入两条边长及其夹角（度）,以空格为间隔：')
a, b, theta = map(float, x.split())
c = math.sqrt(a**2+b**2-2*a*b*math.cos(theta*math.pi/180)) #math.sqrt()开方
print('c=', c)





a=float(input('请输入一条边：'))
b=float(input('请输入另一条边：'))
theta=float(input('请输入上面输入的两边的夹角：'))
c = math.sqrt(a**2+b**2-2*a*b*math.cos(theta*math.pi/180))
print('c=', c)