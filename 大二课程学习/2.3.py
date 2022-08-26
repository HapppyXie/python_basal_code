# Athour:Mr Xie
# 开发时间:2021/10/3 16:13

    #3.任意输入一串数字，按降序排序

x = eval(input('请输入一串数字，以逗号为间隔'))
print(x)
x = list(x)
x.sort()
x.reverse()
print('-------------')
print(x)
