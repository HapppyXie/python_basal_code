# Athour:Mr Xie
# 开发时间:2021/9/19 13:17
#1.单分支
'''
if 条件:
    print()   //前面有四个空格，然后是满足条件的语句  一个tab自动缩进四个代码
'''
today_weather='rain_day'
if today_weather =='rain_day':
    print('take your umberlla with you')

#2.多分支
'''
if 条件：
    满足条件执行代码
else:
    if条件不满足执行的语句

'''
Age_of_me=19
if Age_of_me>50:
    print('Too old,time to retire..')
else:
    print('还能折腾几年！')


my_score=666
if my_score>=600:
    print('上985院校')
else:
    print('上蓝翔技校')


'''
插入知识点：缩进：代码有层级，通过缩进分级    1级2级...
            层次感       可以不是四个，但是不整洁   同一层级，缩进一致

python缩进原则：顶级代码必须顶行写，即如果代码本身不依赖于任何条件，那它必须不能进行任何缩进
              同一级的代码，缩进必须一致
              官方建议缩进用4个空格

'''
#3.多分支

'''
if 条件：
    满足条件执行代码
elif 条件：
    满足条件执行代码
elif 条件：
    满足条件执行代码
.................
else:
    上面条件都不满足执行代码

'''
age = 15
if age < 12:                        #自上而下 只走一条
    print('you are a child')
elif age < 18:
    print('you are a teenager')
elif age < 30:
    print('you are a young man')
else:
    print('you are a oil middle_age man')


#多分支，小作业
x=input('请输入成绩，1-100')
x=eval(x)
if 90<=x<=100:
    print('A')
elif 80<=x<=89:
    print('B')
elif 60<=x<=79:
    print('C')
elif 40<=x<=59:
    print('D')
elif 0<=x<=39:
    print('E')
else:
    print('分数范围错误')













