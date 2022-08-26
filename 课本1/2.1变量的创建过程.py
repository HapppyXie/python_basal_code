# Athour:Mr Xie
# 开发时间:2021/9/30 19:14
name = 'Alex'
id(name)   #pyhton本身存有，创建，实际为将name指向Alex
print(id(name))

name = 'jack'
print(id(name))
'''
python 解释器有自动垃圾回收机制，自动隔一段时间把没有跟变量名相关联的内存数据回收，相当于删掉前面的Alex


'''

name1 = name
print(name1)
print(id(name1))

'''
此处name为什么打印出来是jack，因为name = name1 时 name = 'jack' ,是将name1指向 'jack' （name把内存地址给了name1）
                            所有此处的name改为黑姑娘后，name指向 '黑姑娘'

'''
name = '黑姑娘'
print(name1)

