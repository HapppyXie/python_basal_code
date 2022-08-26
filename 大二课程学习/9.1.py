# Athour:Mr Xie
# 开发时间:2021/11/27 12:41
#1．利用正则表达式判断字符串是否只有小写字母或数字（import re）
import re
a = '123456sajfk'
b = '()sd123'
c = 'Aldn*&123'
d = 'sadakd  jsakdj#1323'
e = '123/.{}sfQW'
f = '1234567890'
g = 'zcxvcvnmv'
pattern = re.compile(r'\b[a-z0-9]+\b')#生成只寻找小写字母和数字的正则表达式对象
list = [a,b,c,d,e,f,g]  #生成要判断的字符串列表
for i in list:    #遍历字符串列表，并进行正则表达式运算
    result = re.findall(pattern, i)
    if i == result[0]: #如果只含有小写字母或数字，运算后等于自身
        print('True')
        print(result)
    else:
        print('False')



pattern1 = re.compile('^[a-z0-9]+$') #以小写字母或数字，开头和结尾，长度可变
print(pattern.findall(d))