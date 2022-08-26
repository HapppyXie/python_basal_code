# Athour:Mr Xie
# 开发时间:2021/11/5 19:38
import jieba
#1.精确模式：把文本精确的切分开，不存在冗余单词，返回一个列表类型的分词结果
x = jieba.lcut('我的生活开始混乱了')
print(x)
#2.全模式：把文本中所有可能的词语都扫描出来，有冗余,返回一个列表类型的分词结果
y = jieba.lcut('为什么人生总是被无意义的消耗',cut_all=True)
print(y)
#3.搜索引擎模式：在精确模式基础上，对长词再次切分,返回一个列表类型的分词结果
z = jieba.lcut_for_search('有的时候只是想静静，就像小时候上课经常发呆那样，什么也不想')
print(z)

#普通分词
x1 = '分词的准确度直接影响了后续文本处理和挖掘算法的最终效果。'
print(jieba.cut(x1))
print(list(jieba.cut(x1)))

print(list(jieba.cut('纸杯')))
print(list(jieba.cut('花纸杯')))
#增加词条
jieba.add_word('花纸杯')
print(list(jieba.cut('花纸杯')))



