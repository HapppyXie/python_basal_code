# Athour:Mr Xie
# 开发时间:2021/9/25 15:27

'''

break和continue只能在循环语句中使用
continue 终止当次循环
'''

count=0
while count<100:
    count+=1
    if 10<count<=20:
        continue     #
    print(count,end=' ')
    if count%10==0:
        print()
print(3 if 3>5 else 9)
'''
while 条件：
    满足执行的语句
    
else: #当循环正常结束时执行         如果有exit()和break   就不会执行
    语句
'''