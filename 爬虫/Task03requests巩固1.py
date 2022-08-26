# Athour:Mr Xie
# 开发时间:2022/2/9 15:54
'''
实现一个简易的网页采集器

https://www.sogou.com/sogou?pid=sogou-netb-07cb5f86508f1467-8803&query=雷州
->简洁处理  https://www.sogou.com/sogou?query=雷州(%E9%9B%B7%E5%B7%9E)  url编码导致乱码

get(url, params=None, **kwargs):
    url网址   params用该网址查询什么的参数   **kwargs(headers,请求头信息)

User-Agent:请求载体的身份标识
浏览器浏览时，身份标识为浏览器，用python请求时，身份标识为程序
UA检测:门户网站的服务器会检测对应请求的载体的身份标识，如果检测到的载体身份标识为某一款浏览器，说明该请求正常
        ，但如果检测到的请求载体为不正常的请求（爬虫(myself)），服务器可能拒绝请求(基本80%网站都使用)
UA伪装:让爬虫对应的请求载体身份标识伪装乘一款浏览器
'''
import requests
if __name__=="__main__":
    #UA伪装,将请求对应的User-Agent封装到一个字典中,使用get的第三个参数
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    url='https://www.sogou.com/sogou?'
    #处理url所携带的参数,封装到字典中
    kw = input('enter a word:')         #使url查询动态化
    param = {'query':kw}
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    with open('C:Users\mike\Desktop\myData.html',mode='w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('保存成功!!!')