# Athour:Mr Xie
# 开发时间:2021/10/3 16:05


#2.任意输入3个英文单词，按字典表达顺序派出
s = input('请输入三个英文字母，以逗号为间隔：')
x, y, z =sorted(s.split(','))
d=dict()
d['1']=x
d['2']=y
d['3']=z
print(d)