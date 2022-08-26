# Athour:Mr Xie
# 开发时间:2021/11/15 22:16
#4.创建testnew.txt, 写入内容“五月天山雪，无花只有寒”，查看文件内容，
# 文件指针移到第6个字节位置，读取指针后的所有内容，将其中第12个字符修改为测试。

f1 = open(r'C:\Users\mike\Desktop\testnew.txt','w',encoding='cp936')
x = '五月天山雪，无花只有寒'
f1.write(x)
f1.close()

f1 = open(r'C:\Users\mike\Desktop\testnew.txt','r',encoding='cp936')
#f1.seek() 一次移动一个字节
print(f1.read(6))       #read(1) 读一个字节，不写默认全读
print(f1.read())
f1.read()
f1.close()

f1 = open(r'C:\Users\mike\Desktop\testnew.txt','a',encoding='cp936')
#修改会覆盖全部，追加只能写到后面,r+
f1.write('测试')
f1.close()





