# Athour:Mr Xie
# 开发时间:2021/10/29 18:57
#3.	求润年Leapyear(n)，输入年份，统计该年是不是润年，如果是润年，返回True；否则返回False。
def judgeLeapYear(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print('True')
    else:
        print('False')
while True:
    i = eval(input('请输入年份，判断是闰年还是平年：'))
    judgeLeapYear(i)






