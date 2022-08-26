# Athour:Mr Xie
# 开发时间:2021/11/5 14:51
def equavilent(s1, s2):         #判断两个字符串在Python意义上是否等价
	if s1 == s2:
		return True
	elif ' '.join(s1.split()) == ' '.join(s2.split()):
		return True
	elif ''.join(s1.split()) == ''.join(s2.split()):
		return True
	else:
		return False
print(equavilent('pip list', 'pip       list'))


table = ''.maketrans('abcdef123', 'uvwxyz@#$')
table2 = ''.maketrans('uvwxyz@#$','abcdef123')
s = "Python is a greate programming language. I like it!"
print(s)
print('---------------------------')
#按映射表进行替换
print(s.translate(table))
print('---------------------------')
s1 = s.translate(table)   #加密
print(s1)
print('---------------------------')
s2 = s1.translate(table2)    #解密   由于映射表不全，解密不全
print(s2)

print('---------------------------')
#问题解决：凯撒加密，每个字母替换为后面第k个。
import string
def kaisaEncode(s, k):
    lower = string.ascii_lowercase          #小写字母
    upper = string.ascii_uppercase          #大写字母
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)     #创建映射表
    return s.translate(table)

s = "Python is a greate programming language. I like it!"
s1 = kaisaEncode(s, 3)
print(s1)
#kaisa解密
def kaisaDecode(s,k):
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	before = lower[k:]+lower[:k]+upper[k:]+upper[:k]
	after = string.ascii_letters
	table = ''.maketrans(before, after)
	return s.translate(table)
print('----------------------')
s2 = kaisaDecode(s1, 3)
print(s2)


