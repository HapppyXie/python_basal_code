# Athour:Mr Xie
# 开发时间:2021/10/3 16:39
#5.编写程序生成包含20个随机数的列表，然后将前10个元素升序，后10个降序排列

import random
x = [random.randint(1, 101) for i in range(20)]
print(x)
#整体排序
x.sort()
print(x)
#排出前十个数
y=x[0:10]
print(y)

#排出后后十个数
z=x[10:]
z.reverse()
print(z)

