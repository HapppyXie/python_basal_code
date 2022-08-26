# Athour:Mr Xie
# 开发时间:2021/10/17 12:29
a_dict = {1:'alex', 2:'jack', 3:'newton', 4:'黑姑娘'}
print(a_dict)
while True:
    x = eval(input('请输入键:'))
    if x in a_dict:
        print(a_dict[x])
    else:
        print('你输入的键不存在！')