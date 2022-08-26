# Athour:Mr Xie
# 开发时间:2021/11/15 21:39
'''
3.将一个CP936编码格式的文本文件中的内容全部复制到另一个使用UTF8编码的文本文件中
'''
#创建编码为cp936的文件
f1 = open(r'C:\Users\mike\Desktop\k.txt','w',encoding='cp936')
x = '11月10日，广州市家庭经济核对和养老服务指导中心（以下简称“市核养中心”）\n'*5
f1.write(x)
f1.close()
#读取cp936文件内容
f1 = open(r'C:\Users\mike\Desktop\k.txt','r',encoding='cp936')
y = f1.read()
f1.close()
print(y)
#创建编码为utf-8文件
f2 = open(r'C:\Users\mike\Desktop\h.txt','w',encoding='utf-8')
f2.write(y)
f2.close()








