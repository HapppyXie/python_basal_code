# Athour:Mr Xie
# 开发时间:2021/11/26 11:00
import shutil
#copy(src, dst) 复制文件，新文件具有同样的文件属性，如果目标文件已存在则抛出异常

#shutil.copyfile(r'test-0s1', 'test-012')  #复制文件，不复制文件属性，如果目标文件已存在则直接覆盖
#下面的代码演示了如何使用标准库shutil的copyfile()方法复制文件。
'''
make_archive(base_name, format, root_dir=None, base_dir=None)创建tar或zip格式的压缩文件

unpack_archive(filename, extract_dir=None, format=None)解压缩压缩文件

'''
import shutil                                   #导入shutil模块
#shutil.copyfile(r'D:\python\pythonProject\模块\testshutil.txt', r'D:\python\pythonProject\模块\testshutil2.txt')  #复制文件

#D:\python\pythonProject\模块\Dlls所有文件压缩至D:\python\pythonProject\模块\a.zip文件：
#shutil.make_archive(r'D:\python\pythonProject\模块\a', 'zip', 'D:\python\pythonProject\模块', 'Dlls')
#'D:\\a.zip‘           (压缩到什么目录的什么文件，格式，被压缩文件的目录，被压缩的文件)

#下面的代码将刚压缩得到的文件D:\python\pythonProject\模块\a.zip解压缩至D:\python\pythonProject\模块\a_unpack文件夹：
#shutil.unpack_archive(r'D:\python\pythonProject\模块\a.zip', r'D:\python\pythonProject\模块\a_unpack')     #(被解压文件，解压文件)

#下面的代码使用shutil模块的方法删除刚刚解压缩得到的文件夹：
#shutil.rmtree('D:\\a_unpack')
#rar的压缩包不行
shutil.unpack_archive(r'D:\谷歌浏览器\谷歌驱动程序\压缩包\chromedriver_win32.zip',r'D:\谷歌浏览器\谷歌驱动程序\压缩包\chromedriver_win32')


