# Athour:Mr Xie
# 开发时间:2021/11/5 19:53
#汉字到拼音的转换
from pypinyin import lazy_pinyin,pinyin
x = lazy_pinyin('小阿旺')
print(x)     #返回拼音
y = lazy_pinyin('小阿旺',1)
print(y)     #带声调的拼音
z = lazy_pinyin('小阿旺', 2)         #另一种拼音形式，数字表示前面字母的声调
print(z)

print(lazy_pinyin('重要',1))
print(lazy_pinyin('重阳',1))  #自动识别多音字
#pinyin('...')返回每个字符的拼音字符列表组成的列表
print(pinyin('重阳'))

x = '中英文混合test123'
print(lazy_pinyin(x))
import jieba
c = lazy_pinyin(jieba.lcut(x))
print(c)
