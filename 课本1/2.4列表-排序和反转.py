# Athour:Mr Xie
#, 开发时间:2021/10/3 10:07
a = ['牛逼', '小猫猫', '小狗狗', '小老鼠', '哎哟']
a.reverse()
print(a)  #a.reverse() 使对象a反转
print('-----------------')
s = [4, 5, 2, 98, 64, 12, 35]
s.sort()   #里面key不写，数字默认升序,不同数据类型，按计算机数据表排序
print(s)

for i in s:
    print(i, end=' ')

print()
for i in a:
    if i == '小狗狗':
        print('小狗狗，来抱抱')
    else:
        print(i)

print(len(a))
print(max(a))

