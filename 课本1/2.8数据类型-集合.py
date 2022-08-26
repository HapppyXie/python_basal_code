# Athour:Mr Xie
# 开发时间:2021/10/15 21:21
py = [1, 2, 3, 4]
web = [2, 3, 5, 6, 8]
both = []
for i in py:
    if i in web:
        both.append(i)
print(both)

py.extend(web)#原地扩充，不返回任何对象
print(set(py))

'''
创建集合
'''

a = {1, 1, 2, 2, 5, 8, 9}
print(a)#天生去重
a = [1, 1, 2, 2, 5, 8, 9]
a = set(a)
print(a)
a.add('黑哥哥')
print(a)
a.add(2)
print(a)
#a.add([1, 2, 3])  可变数据类型不可加
a.add((1, 5))
print(a)

#a.discard(数据)
a.discard(a) #没有该数据则不做
a.discard(5) #有该数据则删
print(a)
#a.pop()随机删除
a.pop()
print(a)

#a.remove(数据) 没有会报错



