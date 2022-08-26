# Athour:Mr Xie
# 开发时间:2021/11/21 22:22
import wordcloud
from wordcloud import STOPWORDS
import jieba
t = open(r'C:\Users\mike\Desktop\test.txt',mode='r',encoding='utf-8')
txt = t.read()
t.close()
stopwords=set(STOPWORDS)
stopwords.add("和")
stopwords.add("等")
stopwords.add("的")
w = wordcloud.WordCloud(width = 1000, font_path='msyh.ttc',height=700,\
                        background_color='white',min_font_size=20,\
                        max_font_size=100,font_step=2,max_words=100,\
                        stopwords=stopwords)
w.generate(' '.join(jieba.lcut(txt)))
#print(w) 返回一个可调用的词云对象
w.to_file(r'C:\Users\mike\Desktop\乡村振兴.png')