# Athour:Mr Xie
# 开发时间:2021/9/25 15:06
'''
while 条件：
    执行代码
'''
count1=0
while count1<3:
    print('记得写作业...')
    count1+=1

'''
打印1-100的偶数

'''
count2=0
while count2<100:
    if count2%2==0:
        print(count2)
    count2+=1
#exit()程序退出
 #break 终止循环  continue终止当次循环
import random
r = random.randint(1,10)
count3=0
while count3<5:
    x=int(input('请输入你猜的数字'))
    if x<r:
        print('try bigger...')
    elif x>r:
        print('try smaller...')
    else:
        print('Bingo,you got it...')

        break
    count3+=1

print(r)

