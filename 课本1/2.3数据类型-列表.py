# Athour:Mr Xie
# 开发时间:2021/10/1 13:04
#切片
a=['金角大王', '黑姑娘', 'rain', 'eva', 'alice', 'eva', '银角大王']
print(len(a))
print(a[1:4])
print(a[1:5])          #顾头不顾尾
print(a[1:-2])
print(a[0:])   #全取
print(a[:6])    #默认从零开始
print('--------------')
'''
倒着切，实质是正着切
'''
print(a[-1:-5])    #因为只能正着切，所以打出[]
print(a[-5:-1])
print(a[-5:])
print('--------------')
'''
步长：步子的长度
'''
print(a[0::1])
print(a[0::2])
print(a[0::3])
print(a[0::4])
print('-------------')

print(a[-1:-5:-1])
print(a[-1:-5:-2])

print('-------------')
print(a[::1])
print(a[::-1])

print('-------------')
#字符串原理也如此
s = '谢狗狗'
print(s[::1])
print(s[::-1])

#使用列表增加元素
alist=[3,5,7]
print(alist[len(alist):])
alist[len(alist):]=[9]      #列表尾部增加列表元素,不可以=9
print(alist)
alist[:0]=[1,2]
print(alist)

#列表推导式式
a = [x*x for x in range(10)]
print(a)