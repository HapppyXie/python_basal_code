# Athour:Mr Xie
# 开发时间:2021/10/16 19:10
'''


'''
x = 3
print(type(x))
print(isinstance(x, int)) #测试x是否为int类型 isinstance
print('Hello World!'.encode('utf-8'))    #使用utf-8格式进行字符编码
print('Hello World!'.encode('gbk'))
print('阿旺！'.encode('utf-8'))
'阿旺！'.encode('utf-8')
print('阿旺！'.encode('utf-8'))

print(b'\xe9\x98\xbf\xe6\x97\xba\xef\xbc\x81'.decode('utf-8'))

# 使用ord()可查其字符编码ASCII   支持中英文
print(ord('A'))
print(bin(ord('A')))
print(ord('阿'))
print(ord('0'))
print(bin(ord('0')))
print(str(0b110000))
print(bin(ord('x')))
'''
    128  64  32  16  8  4  2  1
65   0   1   0   0   0  0  0  1
108  0   1   1   0   1  1  0  1
48   0   0   1   1   0  0  0  0   

计算机设定 最多每8个二进制位代表一个字符，用不到8位，前面补0
短句重要性
每一位1或0所占的空间单位为bit(比特)，计算机最小单位
8bits = 1 bytes 字节， 代表一个字符   2**8=256
1024bytes = 1 kb 
1024kb = 1mb
1024mb = 1G
1024G = 1TB
1024T = EB 一个国家一年的数据量


'''


'''
#中文如何显示,ASCII中没有中文,中国人自己搞了一张表 1980年GB2312  共计6763个字符      1995 GBK1.0 20000多个字符 
                                            # 2000 GBK  280000字符
数据过大，一个字节8位，导致无法存储，用2个8位 2**16=65535

我的名字是Jack , 两种字符
0101010101010101010101

2mb ASCII
4mb gbk  存储内容过大 ，英文用ASCII即可 ，于是有了兼容ASCII和GBK的，中文两个字节，英文一个字节

如果两个高位字节，同时出现，认定其为中文，去gbk找中文字符
否则，使用ascii


中国人使用自己gbk的同时， 日本使用shift_JIS  ,
日本游戏在中国没有日本的编码，运行会导致乱码，要想不乱，装语言包，可以正常显示中文
很麻烦，文化交流障碍
联合国，万国码 1.支持全球语言  unicode 2-4字节 已经收录136690个字符，并还在不断扩展
            2.还可以与全球各个语言进行转换， unicode -> gbk/shift_JIS / Big5(台湾)
        1980 1.但是，当时已有很多软件发售，不可能将它们回购，重新编写成unicode ,等于推到重来
             2.unicode像英语，gbk像汉语，没有强烈需求要全转成unicode
             全球计算机厂商都支持unicode，gbk-> unicode <-shift_JIS  
             大多数软件都支持unicode
             
unicode 带来了新问题 ，内存空间大，可存储，没问题，传输或存到硬盘里，空间大了一倍，浪费+效率低
针对传输和存储硬盘做了新的编码，utf
UTF-8:使用1，2，3，4个字节表示所有字符，优先使用一个字符，无法满足增加一个字符，最多4个字符。
      英文占1个字节，欧洲语系占2个字节，东亚占3个，其他及特殊字符占4个
UTF-16:使用2，4个字节表示所有字符，优先使用2字符，否则使用4个字节表示
UTF-32:使用4个字节表示所有字符

py 2 ascii
py 3 unicode

py2 和py3 的区别
py3全面unicode,支持中文，所有可直接输入中文


'''
















