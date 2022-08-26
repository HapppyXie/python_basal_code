# Athour:Mr Xie
# 开发时间:2021/11/5 16:14
#4. 编写函数，实现字符串加密和解密
def crypt(password, key):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in password:
        result = result + chr(ord(ch) ^ ord(next(temp)))
    return result

password = 'wsAD147963'
key = 'AbCdEfGhIjJlMn'

print('Before Encrypted:'+password)
encrypted = crypt(password, key)
print('After Encrypted:'+encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:'+decrypted)

