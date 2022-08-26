# Athour:Mr Xie
# 开发时间:2021/11/5 17:14

'''
time库格式化
'''
import time
t = time.gmtime()
print(t)
t1 = time.strftime("%Y-%m-%d-%H:%M:%S",t)
print(t1)
#2022-03-23-10:19:46
#2022-03-23-10:20:02
timeStr = '2018-01-26-12:55:20'
t2 = time.strptime(timeStr, '%Y-%m-%d-%H:%M:%S')
print(t2)

t=time.localtime()
print(t)
t=time.strftime('%Y-%m-%d-%H:%M:%S',t)
print(t)