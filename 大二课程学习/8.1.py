# Athour:Mr Xie
# 开发时间:2021/11/15 21:39

#1.遍历并输出文本文件test.txt（内容自己拟定）的所有行内容。
f = open(r'C:\Users\mike\Desktop\test.txt','r',encoding='utf-8')
f1 = f.readlines()
f.close()
for line in f1:
    print(line)