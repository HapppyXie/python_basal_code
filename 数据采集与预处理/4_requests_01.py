# Athour:Mr Xie
# 开发时间:2022/4/19 20:20
import requests

# response = requests.get('http://www.baidu.com')
# print('状态码:',response.status_code)
# print('url:',response.url)
# print('header:',response.headers)
# print('cookie:',response.cookies)
# print('text:',response.text)
# print('content:',response.content)

# data={'kw':'苹果',}
# response = requests.post('https://fanyi.baidu.com/sug',data)
# #以字节流形式打印网页源码 - 二进制
# print(response.content)

#定制requests

#1.传递url参数
# base_url='http://httpbin.org'
# param_data={'data':'xmu','password':123456}
# response = requests.get(base_url+'/get',params=param_data)
# print(response.url)
# print(response.status_code)


# 爬取网页,输出的信息中有时候会出现“抱歉，无法访问”等字眼，这就是禁止爬取,
# 需要通过定制请求头Headers来解决这个问题。定制Headers是解决requests请求被拒绝的方法之一
# 检查-doc-name-点击一个数据-headers,或All,name下点击一个数据-headers  滑倒下方
#Headers中有很多内容，主要常用的就是“User-Agent”和“Host”，它们是以键对的形式呈现的，
# 如果把“User-Agent”以字典键值对形式作为Headers的内容，往往就可以顺利爬取网页内容

#2.定制请求头
# url='http://httpbin.org'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
# response = requests.get(url,headers=headers)
# print(response.content)

#网络请求不可避免会遇上请求超时的情况，这个时候，
# 网络数据采集的程序会一直运行等待进程，造成网络数据采集程序不能很好地顺利执行
#可以为requests的timeout参数设定等待秒数，如果服务器在指定时间内没有应答就返回异常

#3.网络超时
import requests
from requests.exceptions import ReadTimeout,ConnectTimeout
try:
    response = requests.get('http://baidu.com',timeout=0.5)
    print(response.status_code)
except ReadTimeout or ConnectTimeout:
    print('Timeout')


