# Athour:Mr Xie
# 开发时间:2022/3/24 10:33

import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# html = response.read()
# print(html)

import urllib.parse
url='https://fanyi.baidu.com/sug'
# 2.发起POST请求之前，要处理POST请求携带的参数
#2.1 将POST请求封装到字典
data = {'kw':'苹果',}
# 2.2 使用parse模块中的urlencode(返回值类型是字符串类型)进行编码处理
data = urllib.parse.urlencode(data)
# 将步骤2.2的编码结果转换成byte类型
data = data.encode()
# 3.发起POST请求:urlopen函数的data参数表示的就是经过处理之后的POST请求携带的参数
response = urllib.request.urlopen(url=url,data=data)
data = response.read()
print(data)
#把上面print(data)执行的结果，拿到JSON在线格式校验网站（http://www.bejson.com/）进行处理，使用“Unicode转中文”功能可以得到如下结果：



