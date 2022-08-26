# Athour:Mr Xie
# 开发时间:2021/11/5 10:33
'''
生成器函数，包含yield的函数
yield执行就返回，后面的代买搁置
定义了一个生成器函数
'''
def f():
    a,b=1,1
    while True:
        yield a   #执行一次返回一次a， 后面暂停
        a,b=b,a+b
a = f() # 创建生成器对象
for i in range(10):
    print(a.__next__(), end=' ')
print(a.__next__())

b = f() #再生成一个
print(next(b))

def f2():
    yield from 'abcdefg'
x = f2()
for i in x:
    print(i, end=' ')
print()
#next(x) 前面已经遍历结束，再生成一个,从a开始
x2 = f2()
print(next(x2))