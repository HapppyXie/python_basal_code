# Athour:Mr Xie
# 开发时间:2021/11/16 16:57
#7. 编写程序，使用pickle模块把包含学生成绩的字典保存为二进制文件，然后读取内容并显示
import pickle
x = {'小明':99,'小陈':88,'小谢':89,'小旺':80,'小笔':77}
y = {'小m':99,'小c':88,'小x':89,'小w':80,'小b':77}
data = (x,y)
with open(r'C:\Users\mike\Desktop\test2.bin','wb') as src:
    pickle.dump(data,src)
with open(r'C:\Users\mike\Desktop\test2.bin','rb') as src:
    print(pickle.load(src))

