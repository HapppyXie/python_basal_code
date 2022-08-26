# Athour:Mr Xie
# 开发时间:2021/11/5 20:50
#6. 选做：三国演义（或红楼梦。。）中人名词频统计
import jieba
txt = open(file='C:/Users/mike/Desktop/三国演义.txt',mode='r',encoding='utf-8').read()
words = jieba.lcut(txt)
counts = dict()
exclues = {'却说','二人','不可','荆州','不能','如此','商议','后主','大叫','先主','天子','大军','忽报','赶来',
           '主公','军士','军马','引兵','如何','左右','都督','蜀兵','太守','后人','一面','先生','百姓','何故',
           '次日','大喜','天下','东吴','于是','人马','不知','上马','此人','背后','何不','然后','先锋','不如',
           '今日','不敢','魏兵','陛下','一人','汉中','只见','众将','夫人','城中','将军'}
'''
诸葛亮或孔明曰=孔明，关公或云长=关羽，玄德或玄德曰=刘备，孟德或丞相=曹操，
去掉 却说，二人，不可，荆州，不能，如此，商议，主公，军士，军马，引兵，//如何，左右，次日，大喜，天下，东吴
'''
for word in words:
    if len(word) == 1:
        continue
    elif word == '诸葛亮' or word == '孔明曰':
        rword = '孔明'
    elif word == '关公' or word == '云长':
        rword = '关羽'
    elif word == '玄德' or word == '玄德曰':
        rword = '刘备'
    elif word == '孟德' or word == '丞相':
        rword = '曹操'
    else:
        rword = word
    counts[rword] = counts.get(rword, 0)+1
for i in exclues:
    del counts[i]
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    if i % 5 == 0:
        print()
    print('{0}:  {1}'.format(word, count), end=' ')

