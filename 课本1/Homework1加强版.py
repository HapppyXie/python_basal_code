# Athour:Mr Xie
# 开发时间:2021/9/30 18:51
import random
'''
询问用户是否继续玩 如果回答1，让其猜三次，2退出系统   猜对后退出系统
'''
def myGame():
    print('进入游戏页面：')
    print('年龄范围为19-30,共三次机会')
    # 生成随机数
    n = random.randint(19, 30)
    count=0
    while count<3:
        x=int(input('请输入要猜的数'))
        if x > n:
            print('猜大了...')
        elif x < n:
            print('猜小了...')
        else:
            print('恭喜猜对!')                        #猜对后应直接退出 ，不然又会出现提示语句
            break
        count += 1

while True:
    print('欢迎来到猜年龄游戏！')
    x=eval(input('请输入单个数字以选择：1.开始游戏;2.退出'))
    if (x==1):
        myGame()
    else:
        print('谢谢你玩我的游戏！')
        exit()








