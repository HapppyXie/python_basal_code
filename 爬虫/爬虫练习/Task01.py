# Athour:Mr Xie
# 开发时间:2021/12/25 14:33

# a=['name','age','sex']
# b=['Done',38,'Male']
# d=dict(zip(a,b)) #zip(a,b)返回键值小元组，dict()将键值小元组转化为字典
# print(d)

#没隔三个数字取一个
# a=[1,1,1,2,2,2,3,3,3,4,4,4]
# for i in a[::3]:
#     print(i)
# #列表推导式推到含有10个5的列表
# print([5 for i in range(10)])

#函数相互嵌套
def linear(a,b):
    def result(x):
        return a*x+b
    return result
print(linear(1,1)(2))#返回函数result

# def emo(a,b=5):
#     print(a+b)
# emo(5)
# print(emo.__defaults__)#查看从左到右默认值参数的值


#位置参数，默认值参数，关键参数，可变长度参数
def demo(a,b,c):
    print(a+b+c)
#序列解包
#位置参数解包
a=[1,1,1]
demo(*a)

# b={1,1,1}
# demo(*b)

c=(1,1,1)
demo(*c)

d={1:'a',2:'b',3:'c'}
demo(*d)#字典默认取键
d={'a':1,'b':2,'c':3}
demo(**d)
