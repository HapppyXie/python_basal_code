# Athour:Mr Xie
# 开发时间:2021/10/16 18:24

s_1024 = {'佩奇', '老男孩', '海锋', '马JJ', '老村长', '黑顾念', 'Alex'}
s_pornhub = {'Alex', 'Egon', 'Rain', '马JJ', 'Nick', 'Jack'}

#交集 &

print(s_1024 & s_pornhub)

#并集 |

print(s_1024 | s_pornhub)

# 只看第一个的 - 差集

print(s_1024 - s_pornhub)

#    ^  对称差集 两个都有的踢出去

print(s_1024 ^ s_pornhub)

# 判断s_1024和s_pornhub  是不是不相交
print(s_1024.isdisjoint(s_pornhub))

'''
s_1024.issubset(s_pornhub)   判断集合一是不是集合二的子集
s_1024.issuperset(s_pornhub)  判断集合一是不是集合二的父集
'''

print(s_1024.issubset(s_pornhub))
print(s_1024.issuperset(s_pornhub))



print({1, 2, 3}.issubset({1, 2, 3, 4, 5, 6}))
print({1, 2, 3, 4, 5, 6}.issuperset({1, 2, 3}))

















