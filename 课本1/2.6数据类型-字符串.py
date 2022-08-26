# Athour:Mr Xie
# 开发时间:2021/10/4 11:04
'''
定义：一个有序的字符集合，用于存储和表示文本信息，''huo'' ''或  ''' ''' 中间包含的内容称为字符串
'''

a = 'Hello,Eva! How are you?'
print(a[0])
print(a[5])
print(a)
print(a[::])
print(a[::-1])
print(a[::2])
name = 'jack'+'\n'    #
print(name)

names = r'ja\tck\n'     #前面加r告诉系统不要转义
print(names)

#       a[0] = 45   字符串不支持修改

s = "Oh my god! I'm sleepy now"
print(s.capitalize())   #capitalize()首字母大写
print(s.casefold())     #casefold()所有字符串小写
print(s.center(150, ' '))     #center(宽度，填充内容)


#count()统计     count(要统计的字符,开始,结束)  #此处的开始 结束 类似切边
print(s.count('o'))
print(s.count('o', 0, 10))


#endswith('结尾的字符')  判断一以什么结尾
x = 'welcome to apeland'
print(x.endswith('d'))
print(x.endswith('land'))
print(x.endswith('lan'))

#find('要找的字符',开始，结束) ，找到放回下标，没找到放回-1
print(x.find('c'))
print(x.find('q'))
print(x.find('e', 2, 13))

#format()   字符串的格式化
'''
{下标}
'''

q = "Welcome {0} to Apeland,you are No.{1} user."
q.format('Eva', 9)
print(q.format('Eva', 9))

q = "Welcome {0} to Apeland,you are No.{1} user, {0}咳咳."
print(q.format('Eva', 99))

q = "Welcome {name} to Apeland,you are No.{user_num} user, {name}咳咳."
q.format(name='Eva', user_num=1)
print(q.format(name='Eva', user_num=1))


#    index(要找的字符串，开始，结束)    找到最先出现的字符的下标
n = 'Oh!My babay dog.Where do you go?'
print(n.index('o', 4, 16))
#print(n.index('F'))     #没找到报错

#  isdigit() 判断是不是一个整数   返回 True或False
x = '9'
print(x.isdigit())
print('6'.isdigit())
print('6.3'.isdigit())

# islower()  判断是不是全是小写
b = 'you are so happy!'
print(b.islower())
print('Alice'.islower())


#  isspace()   判断是不是空格  什么都没写不是空格
print(' '.isspace())
print(''.isspace())

# '间隔'.join(要用间隔拼接的对象)
l1 = ['jack', 'alice', 'mike']
print('-'.join(l1))
l2 = 'hello,world!'
print('-'.join(l2))

# ljust(宽度，'要填充的内容') l从右边   格式化
# rjust()  r从左边

w = 'Author xie'
print(w.ljust(150, '-'))
print(w.rjust(150, '-'))

m = 'HHHHHHH'
print(m.casefold())
print(m.lower())

#   strip()   去掉字符串两边去掉\n 空格  中间无法    lstrip() 只去右边   rstrip() 只去左边
g = '\t       小-谢              \n'
print(g.strip())

#  replace('旧的字符串','新的字符串',count) count=2 改两次

z = 'my score is 590, not 590 very good.'
print(z)
print(z.replace('590', '666', 1))
print(z.replace('590', '666', 2))


#   split('指定分隔符',maxsplit)  maxsplit:分隔几次  split()从左边     rsplit()从右边
#   以指定字符分隔，分隔成多个字符串，返回包含分隔符结果的列表 ; 若原字符串中没有指定分隔符，这形成列表

s1 = 'alice, jack, mike'
print(s1.split(','))
print(s1.split(',', 1))
print(s1.split('-'))
print(s1.split(';'))

print(s1.rsplit(',', 1))


#   startswith() 判断一个字符以什么开始
s2 = 'My name is xiao xie.'
print(s2.startswith('M'))
print(s2.startswith('MDF'))
print(s2.startswith('My name'))
print(s2.startswith('Myname'))

#  swapcase()  大写换小写，小写换大写
s3 = 'my name is xiao xie.'
print(s3.swapcase())
print(s3.swapcase().swapcase())    #哈哈哈哈哈哈


#  upper() 全变大写
s4 = 'my name Is xiao XIE'
print(s4.upper())

#  zfill()







