# Athour:Mr Xie
# 开发时间:2021/10/22 19:05
'''

满16进1
 0 1 2 3 4 5 6 7 8 9  A  B  C  D  E   F
 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14  15
几进制在底层都是2进制，只是展示得更短
'''
print(hex(28))
'''
输出结果0x1c  在各个语言中使用0x在前面表示16进制
10进制中  
  1  c 
  16 12
  
计算FC45 的10进制
'''
print(15*16**3+12*16**2+4*16**1+5)

#化10进制的5000为16进制
x1 = str(5000 % 16)
x2 = str((5000//16) % 16)
x3 = str(((5000//16)//16) % 16)
x4 = str((((5000//16)//16)//16) % 16)
print('10进制的5000化为16进制为：'+x4+x3+x2+x1)
print(hex(5000))


