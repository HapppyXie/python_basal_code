# Athour:Mr Xie
# 开发时间:2021/10/16 19:47
'''
3.设计程序：假设已有若干用户名字及其喜欢的电影清单，现有某用户，已看过并喜欢一些电影，现在想找个新电影看看，又不知道看什么好。请推荐电影
'''

from random import randrange
data = {'user'+str(i): {'flim'+str(randrange(1, 10))\
                       for j in range(randrange(15))}\
        for i in range(10)}


user = {'flim1', 'flim9', 'flim7'}

similarUser, flims = max(data.items(), key=lambda item: len(item[1] & user))

for x, y in data.items():
    print(x, ':', y)
print('和你最相似的用户是：', similarUser)
print('它看过的电影有:', flims)
print('你没看过的有：', flims-user)
