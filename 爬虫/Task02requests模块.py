# Athour:Mr Xie
# 开发时间:2022/2/9 15:21
'''
网络请求模块：requests模块,python中原生的一款基于网络请求的模块，强大简单
作用：模拟浏览器发送请求

url:是统一资源定位符，是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它

用法:
1.制定url
2.发送请求
3.获取响应数据
4.持久化存储

环境安装 pip install requests
实战编码：需求：抓取搜狗首页的页面数据
'''
import requests
#1.制定url
url = 'http://www.sogou.com/'
#2.发送请求,成功返回一个响应对象
response = requests.get(url=url)
#3.获得响应数据,获得字符串形式的数据以text存储
data = response.text
#print(data)
#4.持久化存储
#C:Users\mike\Desktop\testData.html
with open('testData.html', 'w', encoding='utf-8') as fp:
    fp.write(data)
print('抓取数据结束！！！')