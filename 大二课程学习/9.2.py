# Athour:Mr Xie
# 开发时间:2021/11/27 13:36
#2 编写程序，检查重复的单词，并只保留一个。例如：文本内容为“This is is a desk”,程序输出为“This is a desk”
import re
text = "This is is a desk | This is is a desk"
after_text1 = re.sub(r'(\b\w+) \1',r'\1',text)
print(after_text1)

pattern = re.compile(r'(\b\w+) \1')
after_text2 = re.sub(pattern, r'\1',text)
print(after_text2)