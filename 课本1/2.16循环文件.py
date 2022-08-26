# Athour:Mr Xie
# 开发时间:2022/2/9 21:53
# f=open(file='2.15我的测试',mode='r',encoding='utf-8')
# data = list()
# link = list()
# for line in f:
#     temp = line.split()
#     data.append(temp)
# for i in data:
#     if(int(i[2])>=175 and int(i[3])<=50):
#         link.append(i)
# print(link)



#f=open(file='2.15我的测试',mode='r',encoding='utf-8')
#把光标移到某个位置,移动字节，utf-8中文3个字节，英文一个字节一个,gbk两个字节一个中文
'''
seek(offset,[whence=0])  把文件指针移动到新的字节位置，offset表示相对于whence的位置。
whence为0表示从文件头开始计算，1表示从当前位置开始计算，2表示从文件尾开始计算，默认为0
'''
# print(f.readline())
# print(f.tell())#告知光标在哪里
# f.seek(2)
# print(f.tell())
# print(f.readline())

# print(f.tell())
# f.seek(28)
# print(f.readline())

# #缓存慢或close()再写进硬盘，flush强制写入
# f=open(file='2.15我的测试',mode='w',encoding='utf-8')
# for i in range(10):
#     f.write('小美女 我的 175 50 13428394849\n')

#print(f.writable())

# a = ['f 雷州 176 49 13426894847\n','f 雷州 176 49 13426894847\n','f 雷州 176 49 13426894847\n','f 雷州 176 49 13426894847\n']
# f.writelines(a)
# f.truncate(100)
# #有些网站访问量大，可以隔一段时间就截断
# f.close()

# #用不占内存的方式修改文件
# f=open(file='2.15我的测试',mode='r',encoding='utf-8')
# f_new = open(file='2.15我的测试.new',mode='w',encoding='utf-8')
#
# old_str = '我的'
# new_str = '大家的'
# for line in f:
#     if old_str in line:
#         line = line.replace(old_str,new_str)
#     f_new.write(line)
# f.close()
# f_new.close()
#
# import os
# #对文件重命名
# old_file = '2.15我的测试'
# new_file = '2.15我的测试.new2'
# os.rename(old_file,new_file)
#优先级顺序 not and or

# x=True
# y=False
# z=False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x :
#     print(3)
# else:
#     print(4)


