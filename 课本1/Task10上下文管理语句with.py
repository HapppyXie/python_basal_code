# Athour:Mr Xie
# 开发时间:2021/12/26 15:31
with open(r'C:\Users\mike\Desktop\testnew.txt','r',encoding='cp936') as src,\
        open(r'C:\Users\mike\Desktop\newtxt.txt','w',encoding='cp936') as dst:
    dst.write(src.read())
#with可以自动管理资源，无论发生什么原因（代码发生异常）跳出with块，总能保证文件被正确关闭