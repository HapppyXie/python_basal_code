# Athour:Mr Xie
# 开发时间:2021/10/29 19:54
'''
python实现累乘multi函数（函数参数不限）
def multi(*n):
    result=1
    for i in n:
        result=result*i
    return result
print(multi(1,3,4))#参数不限个数
'''
#5.	实现multi()函数，参数个数不限，返回所有参数的乘积
def multi(p):
    result = 1
    for i in p:
        result = result*i
    return print(result)
while True:
    x = eval(input('请输入要累乘的数，个数不限：'))
    multi(x)