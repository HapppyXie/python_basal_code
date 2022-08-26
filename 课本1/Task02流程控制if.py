# Athour:Mr Xie
# 开发时间:2021/9/25 14:53
'''
猜随机数
'''
import random
x = random.randint(1,10)
print('随机猜数')
y = input('请输入你猜的数字')
y=eval(y)

if x<y:
    print('猜大了')
elif x>y:
    print('猜小了')
else:
    print('Bingo,you got it.....')
print(x)



