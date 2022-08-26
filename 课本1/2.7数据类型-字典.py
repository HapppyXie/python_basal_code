# Athour:Mr Xie
# 开发时间:2021/10/10 17:34
# 知道公司员工姓名，年龄，职务，工资
import string

staff_list = [['Alex', 23, 'CEO', 66000], ['黑姑娘', 24, '行政', 4000], ['佩奇', 26, '讲师', 40000]]
'''
当有一万员工时，不能像现在这样直接看到
可以通过for来遍历
'''
for i in staff_list:
    if '黑姑娘' in i:
        print(i[-1])

# 但这样做，前面的循环无意义

'''
字典定义：{key1:value2 , key2:value2}

键与值用冒号 : 隔开

项与项用 , 隔开 
'''

info = {'name': '小猿圈', 'mission': '帮一万极客高效学编程', 'website': 'http://apeland.com'}
print(info)
# info.keys() 查看所有的key  info.values() 查看说有的value
print(info.values())
print(info.keys())

# info['name'] 下标写key找value

print(info['name'])
print(info['mission'])
print(info['website'])


#字典的创建 1.参数创建
person1 = dict(name='laex', age=29)
print(person1)
#2. 直接赋值
person2 = {'name': '强哥', 'age': 35}
print(person2)

#批量生成value
keys = [1, 2, 3, 4, 5]
num1 = {}.fromkeys(keys)#num1=dict.fromkeys(keys)
print(num1)
print('--------------------')
num2 = {}.fromkeys(keys, '呵呵')
print(num2)


#字典的增加
d = {'name': 'alex', 'age': 29}

d['job'] = 'teacher'
print(d)
d['name'] = 'jack'
print(d)
#d.setdefault(key , value) 没有则增加，有该key则返回其value
d.setdefault('salary', 2000)
print(d)
d.setdefault('salary', 1300)
print(d)


#字典的删除    del(d)全删
#del(d)

del(d['name'])  #删除指点key
print(d)

# d.pop('salary') 删除指定key
d.pop('salary')
print(d)


d = {'name': 'alex', 'age': 29}

#d.popitem()随机删除一个  d.clear()清空列表
d.popitem()
print(d)
d.clear()
print(d)

#修改 1.直接赋值   2.d1.update(d2)将d2的键值对添加到d1中 key重合，改掉，key不重合，添加
d1 = {'name': 'alex', 'age': 29}
d2 = {'name': 'jack', 'age': 28}
print(d1)
print('---------------------')
d1.update(d2)
print(d1)
print('-------------------')
d3 = {'job': 'teacher', 'where': '雷州和Peking'}
d1.update(d3)
print(d1)
print('-----------------')

# 字典查询
print(d1['name'])
print(d1.get('name'))
print('name' in d1)
#print('jack' in d1) 返回False 只可key  调用字典时，如果不明确调用的是key或values，系统默认是key
print(d1.keys())
print(d1.values())

print(d1.items())

# 循环
for i in d1:
    print(i, d1[i])
for i in d1.items():
    print(i)
#分别打印
for k, v in d1.items():
    print(k, v)

#字典get()方法返回指定键对应的值，并且予许指定该键不存在时返回特定的值
import random
x = string.ascii_letters+string.digits+string.punctuation
z=''.join((random.choice(x) for i in range(1000)))
d=dict()
for ch in z:
    d[ch]=d.get(ch,0)+1
for k,v in sorted(d.items()):
    print(k,':',v,'|',end=' ')