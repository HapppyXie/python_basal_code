# Athour:Mr Xie
# 开发时间:2022/2/10 20:20
import pyinstaller
'''
使用-F参数，pyinstaller会将python脚步打包成单个exe文件
使用-D参数，pyinstaller会将python脚步打包成一个文件夹，运行程序时，需要进入该文件夹，点击运行相应的可执行程序
        其中 -D 参数或 -F 参数后面跟的是入口文件
此前为了美观，开源通过 -i 参数指定程序的icon(图标)，但这个命令只在windows下生效
使用 -n 参数定义打包后文件的名称
    
cmd中 pyinstaller -参数 路径名加文件名 
cmd中 pyinstaller -F 加文件带路径全名
        
'''
