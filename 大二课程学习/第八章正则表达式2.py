# Athour:Mr Xie
# 开发时间:2021/11/27 12:54
#使用re模块的compile()方法将正则表达式编译生成正则表达式对象，再使用正则表达式对象提供的方法进行字符串处理
#提高字符串处理速度，也提供了更强大的文本处理功能。
'''
match(string[, pos[, endpos]])方法在字符串开头或指定位置进行搜索，模式必须出现在字符串开头或指定位置；
search(string[, pos[, endpos]])方法在整个字符串或指定范围中进行搜索；
findall(string[, pos[, endpos]])方法在字符串指定范围中查找所有符合正则表达式的字符串并以列表形式返回
'''
import re
example = 'ShangDong institute of Business and Technology'
pattern = re.compile(r'\bB\w+\b') #生成正则表达式对象
print(pattern.match(example))
print(pattern.search(example))

m = pattern.search(example)
print(m.group(0))

pattern = re.compile(r'\b\w*a\w*\b') #查找说有含有字母a的单词
print(pattern.findall(example))

text = "He was carefully disguised but captured quickly by police."
print(re.findall(r'\w+ly',text))

'''
正则表达式对象的match方法和search方法匹配成功后返回match对象。match对象的主要方法有：
group()：返回匹配的一个或多个子模式内容
groups()：返回一个包含匹配的所有子模式内容的元组
groupdict()：返回包含匹配的所有命名子模式内容的字典
start()：返回指定子模式内容的起始位置
end()：返回指定子模式内容的结束位置的前一个位置
span()：返回一个包含指定子模式内容起始位置和结束位置前一个位置的元组。
'''
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0)) #返回整个模式内容
print(m.group(1)) #返回第1个子模式内容
print(m.group(2)) #返回第2个子模式内容
print(m.group(1,2)) #返回指定的多个子模式内容

#提取字符串中的电话号码
telNumber = '''Suppose my Phone No. is 0535-1234567,
            yours is 010-12345678,
            his is 025-87654321.'''
pattern = re.compile(r'\d{3,4}-\d{7,8}')
print(pattern.findall(telNumber))
