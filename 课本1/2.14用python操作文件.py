# Athour:Mr Xie
# 开发时间:2021/10/24 21:12
'''
1.找到文件
2.读，修改
3.保存和关闭

py中 1.f = open(filename)
     2.f.read(100)读一百个字符  f.read() 读所有  f.write(YOURDATA)
     3.f.close() 关闭并保存
文件打开模式： 只能用一种模式打开文件，写w-创建模式，没有创建，有就文件覆盖，读r，追加a     w-write r-read a-append

创建模式 只能写
'''
f = open(file = 'D:/python/练习/py操作文件测试.txt', mode = 'w')

f.write('马老来咯！阿旺快跑！啊！原来是老八\n')
f.write('老爸来了 爸：把狗子拿过来 哦豁\n')

f.close()

'''
只读模式 r 只能读
没有写目录，直接用文件名，可直接调用此处文件
'''
f = open(file='2.15我的测试', mode='r')
print(f.readline())
#readline()只读一行
print('-------------分隔符-----------------')
data = f.read()
print(data)
 #f.write('hahha') 报错
f.close()

'''

追加模式  只能写
'''
f = open(file='2.15我的测试', mode='a')
f.write('我的狗狗 雷州 100 12\n')  #上次没有换行，此处会追加到文件尾部
#f.readline()
f.close()
