# Athour:Mr Xie
# 开发时间:2021/9/13 20:01
money = input('请输入带有符号的货币，人民币转美元或美元转人民币：')
if money[-1] in ['d','D']:
    print(money[-1])
    rmb = eval(money[0:-1])*6
    print('转换后的货币为{:.2f}rmb'.format(rmb))
elif money[-1] in ['r','R']:
    print(money[-1])
    dollar = eval(money[0:-1])/6
    print('转换后的货币为{:.2f}dollar'.format(dollar))
else:
    print('输入的格式有误！')