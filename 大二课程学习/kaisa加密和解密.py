# Athour:Mr Xie
# 开发时间:2021/11/5 16:52
import string
#kaisa加密
def kaisaEncode(s, k):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    before = string.ascii_letters
    after = lower[k:] + lower[:k] + upper[k:] + upper[:k]
    table = ''.maketrans(before, after)
    return s.translate(table)

#kaisa解密
def kaisaDecode(s,k):
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	before = lower[k:]+lower[:k]+upper[k:]+upper[:k]
	after = string.ascii_letters
	table = ''.maketrans(before, after)
	return s.translate(table)
password = 'wsAD147963/!'
password1 = kaisaEncode(password, 9)
print(password1)
print('--------------------------------')
password2 = kaisaDecode(password1,9)
print(password2)