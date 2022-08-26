# Athour:Mr Xie
# 开发时间:2021/12/26 17:08
'''
语法错误和逻辑错误不属于异常，单有些语法错误往往会导致异常
异常错误：程序运行时发生的错误
异常原因：除零，下标越界，文本不存在，网络异常
BaseException是所有内置异常类的基类
先捕获派生类，再捕获基类
'''
while True:
    x=input('please input:')
    try:
        x=int(x)
        print('You have inputed {0}'.format(x))
    except Exception as e:      #有异常则执行
        print('Error')
    else:
        print('如果try中的代码没有引发异常，则执行else块的代码')
    finally:
        print('无论try中语句是否异常，都执行finally中的语句块')