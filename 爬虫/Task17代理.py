# Athour:Mr Xie
# 开发时间:2022/3/13 14:37
'''
一个客户端请求过多，服务器检测到会封掉
借助某种方式伪装客户端-代理，突破自身IP的限制，隐藏自身IP地址
代理：本机-代理服务器（中介，桥梁发送请求，返回信息）-服务器

遇上封ip的反爬策略，使用代理

您的iP地址是：[119.140.115.39 ] 来自：中国广东湛江雷州市 电信

找到代理服务器地址，通过代理服务器转发请求
代理IP类型：
http：只能用于http类型的url
https：只能用于https类型的url

代理ip的匿名度：
    -透明：服务器知道使用了代理，真实ip
    -匿名：知道使用了代理，但不知道真实的ip
    -高匿：不知道使用了代理，也不知道真实的ip


'''
import requests
import os


url='https://www.baidu.com/s?wd=ip'
url2='https://www.ip138.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
proxies={'https://':'202.109.157.66'}
page = requests.get(url=url,headers=headers,proxies=proxies)
page.encoding=page.apparent_encoding
with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page.text)





