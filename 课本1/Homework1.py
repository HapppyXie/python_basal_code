# Athour:Mr Xie
# 开发时间:2021/9/30 18:37
'''
猜年龄游戏

让用户猜三次，三次没猜对，直接退出，如果猜对，打印恭喜信息并退出
'''
import random
print('进入猜年龄游戏程序：')
print('年龄范围为19-30')
#生成随机数
n=random.randint(19,30)
count=0
while count<3:
    x=int(input('请输入要猜的数'))
    if x>n:
        print('猜大了...')
    elif x<n:
        print('猜小了...')
    else:
        print('恭喜猜对')
    count+=1
print('谢谢你玩我做的游戏')
print(n)





