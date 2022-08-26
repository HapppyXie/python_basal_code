# Athour:Mr Xie
# 开发时间:2021/9/28 22:03
print('祖国，你好')

#2.任意输入两个数字，求平均值
print('任意输入两个数字求平均值！')
x=float(input('请输入一个个数字'))
y=float(input('请再输入一个数字'))
print((x+y)/2)


#3. 气温转化   （华氏度-32）/1.8=摄氏度
TempStr=input('请输入带有符号的温度，如36c或36f:')
if TempStr[-1] in ['f','F']:
    C=(eval(TempStr[0:-1])-32)/1.8
    print('转换后的温度:{:.2f}C'.format(C))
elif TempStr[-1] in ['C','c']:
    F=(eval(TempStr[0:-1])*1.8)+32
    print('转换后的温度:{:.2f}F'.format(F))
else:
    print('你输入的格式有误!')

