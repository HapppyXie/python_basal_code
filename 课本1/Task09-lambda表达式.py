# Athour:Mr Xie
# 开发时间:2021/12/25 18:56
'''
lambda表达式常用来声明匿名函数，有名字的临时小函数
        使用于内置函数sorted（）和列表方法sort的key参数，内置函数map（）和filter()的第一个参数
        如何定义  lambda 参数:语句
        只可以包含一个表达式，不予许包含其他复杂的语句，但可以调用其他函数
'''
f=lambda x,y,z:x+y+z#注意它的官方认为没有名字的,但其实可以起名字
print(f(1,2,3))
l =[(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]
print(l[0](2),l[1](2),l[2](2))
