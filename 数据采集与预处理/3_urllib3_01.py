# Athour:Mr Xie
# 开发时间:2022/4/19 20:05
'''
urllib3是一个功能强大、条理清晰、用于HTTP客户端的Python库，许多Python的原生系统已经开始使用urllib3。
urllib3提供了很多python标准库里所没有的重要特性，包括：线程安全、连接池、客户端SSL/TLS验证、
文件分部编码上传、协助处理重复请求和HTTP重定位、支持压缩编码、支持HTTP和SOCKS代理、100%测试覆盖率等。

'''
import urllib3
 #需要一个PoolManager实例来生成请求，
#由该实例对象处理与线程池的连接以及线程安全的所有细节，不需要任何人为操作
# http = urllib3.PoolManager()
# response = http.request('get', 'http://www.baidu.com')
# print(response.status)
# print(response.data)

http = urllib3.PoolManager()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
response = http.request('post','https://fanyi.baidu.com/sug',fields={'kw':'苹果',})
print(response.data)


