# Athour:Mr Xie
# 开发时间:2021/11/27 13:50
#3. 编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。
import re
x = "I'm a little dog and I like eat meat! you are a pig"
pattern = re.compile(r'\b[a-zA-Z]{3}\b')#开头，结尾为字母，长度为3
after_x = re.findall(pattern,x)
print(after_x)

print(re.findall(r'^\w{3}$',x))
print(re.findall(r'^[a-zA-Z]{3}$',x)) #此匹配，开头结尾为字母，且长度必须为3，会匹配到空格，故结果