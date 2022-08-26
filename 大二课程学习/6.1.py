# Athour:Mr Xie
# 开发时间:2021/11/1 10:18
#1. 生成6位数随机密码，检查并判断密码字符串的安全程度。
import string
x = string.digits+string.ascii_letters+string.punctuation
import random
#生成k长度的随机密码
def gerneratePwd(k):
    passWord = ''.join(random.choice(x) for i in range(k))
    print('生成密码位:',passWord)
    return passWord
#检查密码安全性
def checkPwd(pwd):
    if not isinstance(pwd, str) or len(pwd)<6:
        return print('not suitable for password!')
    d = {1:'weak', 2:'below middle',3:'above middle',4:'strog'}
    r = [False]*4
    for p in pwd:
        if p in string.digits:
            r[0] = True
        elif p in string.ascii_lowercase:
            r[1] = True
        elif p in string.ascii_uppercase:
            r[2] = True
        elif p in string.punctuation:
            r[3] = True
    level = d.get(r.count(True), 'error')
    return print(level)

while True:
    print("请输入密码长度，随机生成密码，并检查其安全性：")
    n = eval(input("建议输入生成6-14位的密码："))
    checkPwd(gerneratePwd(n))
