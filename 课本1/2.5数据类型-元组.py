# Athour:Mr Xie
# 开发时间:2021/10/4 10:15

names = ('alice', 'jack')
'''
元组不可修改，只可查看，查看可以使用切片，count,index 
len() map() fliter()
'''
print(names[::-1])
print(names[::])
print(names[0])
print(names[1])
print(names.index('alice'))
print(names.count('alice'))
#names.append('x') #不支持修改

print(names[::])
print(names.count('alice'))
print(names.index('alice'))
print(len(names))    #len()不是tuple的属性，而是内置函数

ages = (11, 22, 33, 44, 55)
print(ages[0])

for age in ages:
    print(age, end=' ')


print()
print(11 in ages)
print(22 not in ages)


'''
元组本身不可变，如果元组中包含其他可变元素，这些可变元素可变
'''
data = (99, 88, 77, ['alice', 'jack'], 55, 44, 33, 22,)
print(data)
print('-------------------------------------------')
data[3][0] = '金角大王'      #元组中第三个元素，列表中索引为0的元素    不可以直接data[3] = 4  ,只能找到其中的一个元素改变
print(data)
'''
因为元组中只是存每个元素的内存地址，上面['金角大王', 'jack']这个列表本身的内存地址存在元组里确实不变，
  但列表地址指向另一块存储地址，是可变的
'''

#  各有个的内存地址，互相独立  看其数据指向的地址死是否可变-这个元素是否可变
print(id(names))
print(id(names[0]))
print(id(names[1]))



