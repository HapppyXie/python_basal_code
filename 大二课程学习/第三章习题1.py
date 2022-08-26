# Athour:Mr Xie
# 开发时间:2021/10/3 11:54
x=list(range(1, 10, 2))
print(x)
y=list(range(10, 0, -2))
print(y)


for i in range(4):
    print(3, end=' ')

print()
# 逆序输出，得出200内可以被17整除的最大整数
for i in range(200,0,-1):
    if i % 17 == 0:
        print(i)
        break

list1=[1, 2, 3, 4, 5, 6]
list2=['小写','小戈', '小兰', '小臂']
print(list(zip(list1, list2)))

for item in zip('abcd',range(3)):
    print(item, end=' ')
print()#换行


