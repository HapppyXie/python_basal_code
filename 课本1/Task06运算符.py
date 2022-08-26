# Athour:Mr Xie
# 开发时间:2021/12/24 14:44
print(0.4-0.3)#实数相加减,稍微有变差
print(0.4-0.3==0.1)
x=4+9j
y=4-9j
print(x*y)#支持复数
1_000_000#予许使用单个下划线作为分隔符提高数字可读性
print(9**9)#幂运算
print(8/3)#整除法
print(8//3)#求整商
print(8%3)#求余数
print(True+1)#True为1
print(False+1)#False为0
print(1<3<5)# 1<3and3<5 惰性求值
import math
print(math.sqrt(9))#开方
import numpy as np
print(np.eye(3)*3)#生成单位矩阵
print(''.join(map(str,(333,444,555))))#python的str为字符类型
print(''.join(map(chr,(333,444,555))))#chr()返回unicode编码对应的字符  ord('字符')返回字符对应的unicode编码
