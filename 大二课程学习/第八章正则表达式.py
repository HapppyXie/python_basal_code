# Athour:Mr Xie
# 开发时间:2021/11/27 9:51
'''
正则表达式使用预定义的模式去匹配一类具有共同特征的字符串，可以快速、准确地完成复杂的查找、替换等处理要求
文本编辑与处理、网页爬虫
正则在线测试网站
         https://regexr-cn.com
在线练习网站
        https://codejiaonang.com

基本语法:   1.“\”开头的元字符与转义字符相同，则需要使用“\\”
          2.字符串前加上字符r或R之后表示原始字符串
          3.如果字符串以一个斜线“\”结束的话，则需要多写一个斜线，即以“\\”结束
          4.“()”表示一个子模式，圆括号内的内容作为一个整体对待
         5.正则表达式只是进行形式上的检查，并不保证内容一定正确
         6.'正则表达式'
标准库re模块提供了正则表达式操作所需要的功能
findall(pattern, string[, flags])返回包含字符串中所有与给定模式匹配的项的列表

match(pattern, string[, flags])从字符串的开始处匹配模式，返回match对象或None

search(pattern, string[, flags])在整个字符串中寻找模式，返回match对象或None
                                    search 找到一个就结束，返回对象
split(pattern, string[, maxsplit=0)根据模式匹配项分隔字符串

sub(pat, repl, string[, count=0])将字符串中所有与pat匹配的项用repl替换，
                                返回新字符串，repl可以是字符串或返回字符串的可调用对象，作用于每个匹配的match对象

其中函数参数“flags”的值可以是下面几个的不同组合（使用“|”进行组合）：
re.I（注意是大写字母I，不是数字1，表示忽略大小写）
re.L（支持本地字符集的字符）
re.M（多行匹配模式）
re.S（使元字符“.”匹配任意字符，包括换行符）
re.U（匹配Unicode字符）
re.X（忽略模式中的空格，并可以使用#注释
'''
import re
text = 'alpha. beta....gamma delta'
print(re.split('[\. ]+',text))      #使用指定字符作为分隔符进行分隔，以点或空格为分隔符
print(re.split('[\. ]+',text,maxsplit=2))
'''
^匹配行首，匹配以^后面的字符开头的字符串
$匹配行尾，匹配以$之前的字符结束的字符串
?匹配位于?之前的0个或1个字符,当此字符紧随任何其他限定符（*、+、?、{n}、{n,}、{n,m}）之后时，
    匹配模式是“非贪心的”。“非贪心的”模式匹配搜索到的、尽可能短的字符串，
    而默认的“贪心的”模式匹配搜索到的、尽可能长的字符串。例如，在字符串“oooo”中，“o+?”只匹配单个“o”，而“o+”匹配所有“o”
'''
pat = '[a-zA-Z]+'
print(re.findall(pat,text))#匹配所有单词
pat = '{name}'
text = 'Dear {name}...'
print(re.sub(pat,'Mr.Dong',text))
s = 'a s d'
print(re.sub('a|s|d','good',s))

w = "It's a very good good idea"
print(re.sub(r'(\b\w+) \1', r'\1', w))
 #处理连续的重复单词      r'(\b\w+) \1'  空格也算字符    \num 前面第num个子模式

print(re.match('done|quit', 'done'))#匹配成功
print(re.match('done|quit','doe!'))#匹配失败 None

print(re.search('done|quit', 'd!one!'))#失败 None
print(re.search('done|quit', 'd!one!done'))#成功返回match对象

s = 'aaa      bb      c d e   fff    '
print(' '.join(s.split()))#直接使用字符串对象的方法

print(' '.join(re.split('[\s]+',s.strip())))#同时使用re中的函数和字符串对象的方法
print(re.sub('\s+',' ',s.strip()))

#下面的代码使用几种不同的方法来删除字符串中指定内容：
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)    #使用search()方法返回的match对象
print(m)#匹配成功
print(email[:m.start()] + email[m.end():])  #字符串切片
print(email.replace('remove_this', ''))

#下面的代码使用以“\”开头的元字符来实现字符串的特定搜索
example = 'Beautiful is better than ugly.'
print(re.findall('\\bb.+?\\b', example))    #以字母b开头的完整单词
                                            #此处问号?表示非贪心模式
print(re.findall('\\bb.+\\b', example))     #贪心模式的匹配结果 空格也匹配进去了
print(re.findall('\\bb\w*\\b', example))    #匹配以b开头，任意数字或字母结尾的
print(re.findall('\\Bh.+?\\b', example))    #不以h开头且含有h字母的单词剩余部分             不懂

