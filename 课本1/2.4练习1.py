# Athour:Mr Xie
# 开发时间:2021/10/3 10:34
names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']

#names.index()默认返回第一个eva的索引值

x1 = names.index('eva')#index(值，起，结)
x2 = names.count('eva')
print(x1)    #获得第一个eva的索引3
print(len(names))    #获得列表的长度7
print(names.index('eva', 4, 7))#获取第二个eva的索引
print(x2)
print(help(names.index))

#2.把以上列表通过切片的形式实现反转
print(names[::-1])
print('------------')
names.reverse()      # x = names.reverse() 错误，x只能是空值None,内置方法reverse不返回任何值，直接对调用的的对象作用
print(names)
print('------------')
#3.打印列表中所有下标为奇数的值
for i in names:
    x = names.index(i)
    if x == 0:
        print(names[x])
    elif x % 2 != 0:
        print(names[x])

#4.通过names。index()方法找到第二个eva的值，并将其改为EVA
names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']
indexOfEva = names.index('eva',4,7)
names[indexOfEva]='EVA'
print(names)