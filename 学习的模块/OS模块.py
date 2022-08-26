# Athour:Mr Xie
# 开发时间:2021/11/26 9:42
import os
path = r'test-os1'
print(os.getcwd())          #返回当前工作目录
print(os.listdir())         #返回path目录下的文件和目录列表

#os.remove(path)                    #  remove(path)
                                    #删除指定的文件，要求用户拥有删除文件的权限，并且文件没有只读或其他特殊属性
#os.rename('test-os', 'test-os1')    #rename(src, dst)
                                    #重命名文件或目录，可以实现文件的移动，若目标文件已存在则抛出异常，不能跨越磁盘或分区
#os.startfile(r'test-os1')        #startfile(filepath [, operation]) 使用关联的应用程序打开指定文件或启动指定应用程序
#os.system(r'C:\Users\mike\Desktop\python397.chm')                         #system(path)


#os.path模块
print(os.path.dirname(path))      #返回路径的文件夹名
print(os.path.basename(path))    #返回路径的最后一个组成部分

'''
import os
import os.path      #os.path 模块主要用于获取文件的属性。
os.rename('C:\\dfg.txt', 'D:\\test2.txt') #rename()可以实现文件的改名和移动
[fname for fname in os.listdir('.')
     if fname.endswith(('.pyc', '.py', '.pyw'))]  #结果略
'''
#os.mkdir(os.getcwd()+'\\temp')         #创建目录
#os.chdir(os.getcwd()+'\\temp')         #改变当前工作目录
print(os.getcwd())
#os.rmdir('temp')                       #删除目录

print(os.environ.get('path'))            #获取系统变量path的值
#os.startfile('notepad.exe')           #启动记事本程序


#os.path模块
print(os.path.exists(r'test-os1'))                 #判断文件是否存在
print(os.path.getsize(r'test-os1'))                 #返回文件的大小

print(os.path.isdir(r'test-os1'))               #判断path是否为文件夹
print(os.path.isfile(r'test-os1'))               #判断path是否为文件

#os.path.join(path, *paths)连接两个或多个path
print(os.path.split(r'C:\Users\mike\Desktop\python397.chm'))#以路径中的最后一个斜线为分隔符把路径分隔成两部分，以元组形式返回
print(os.path.join(r'C:\\Users\\mike\\Desktop',r'python397.chm'))


