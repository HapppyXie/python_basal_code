# Athour:Mr Xie
# 开发时间:2021/11/5 20:44
#3. 汉字转为拼音（汉字内容自选）
from pypinyin import lazy_pinyin,pinyin
x = '织密民生保障网络。坚持创业带动就业，完善就业公共服务体系，多举措扩大就业增收渠道'
y = lazy_pinyin(x)
print(y)
print('-------------------------')
z = lazy_pinyin(x,1)
print(z)
print('-------------------------')
q = pinyin(x)
print(q)