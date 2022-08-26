# Athour:Mr Xie
# 开发时间:2021/11/26 10:35
#如果需要遍历指定目录下所有子目录和文件，可以使用递归的方法。

from os import listdir
from os.path import join, isfile, isdir

directory = r'D:\作业\编程作业'
def listDirDepthFirst(directory):
    '''深度优先遍历文件夹'''
    #遍历文件夹，如果是文件就直接输出
    #如果是文件夹，就输出显示，然后递归遍历该文件夹
    for subPath in listdir(directory):
        path = join(directory, subPath)         #join(path, *paths)连接两个或多个path
        if isfile(path):
            print(path)
        elif isdir(path):
            print(path)
            listDirDepthFirst(path)
listDirDepthFirst(directory)