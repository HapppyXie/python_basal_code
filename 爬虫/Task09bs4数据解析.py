# Athour:Mr Xie
# 开发时间:2022/2/20 11:59
'''
需调用两个模块
pip install bs4模块
pip install lxml解析模块

bs4 python独有的数据解析
bs4数据解析原理:
            from bs4 import BeautifulSuop
            1.通过实例化一个beautifulSoup对象，并且将页面源码数据加载到该对象中
            2.通过调用beautifulSoup对象中的属性和方法进行标签定位和数据提取
对象的实例：
1.将本地的html文档中的数据加载到该对象中

2.将互联网上获取的页面源码加载到该对象中

'''
import requests
from bs4 import BeautifulSoup  #这样才可导对象
if __name__=='__main__':
    #1.将本地的html文档中的数据加载到该对象中
    fp = open('testData.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')

    # #2.将互联网上获取的页面源码加载到该对象中,常用
    # url = 'http://www.sogou.com/'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
    #                          '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    # page_text = requests.get(url=url,headers=headers).text
    # soup = BeautifulSoup(page_text,'lxml')

'''
定位以便获取文本或属性内容

soup.tagName 返回文档中第一次出现tagName对应的标签 文档中<tagName>
soup.a
find()  1.find('a') 等同于soup.a  返回文档中第一次出现tagName对应的标签 文档中<a>
        2.属性定位 find('div',class_/id/attr='属性值')
find_all()  1.找回符合标准的所有标签的列表 []
            2.属性定位
select()  1. select('某种选择器(id,class,标签...)') 就是某种属性值   参数A string containing a CSS selector
          2.层级定位 >表示层级  空隔表示多个层级        返回标签组成的列表，可同时定位到多个

soup.select('.top-nav > ul a')[0].text/string/get_text()  两个属性一个方法
 
 定位后的属性：  
.text/get_text()获取标签中的全部文本内容  不是直系也可   
.string 获取标签直系的内容
.attrs 获得属性
'''
#print(soup.find('div'))
#print(soup.find('div',class_='top-nav'))

#print(soup.find_all('a'))

# 此处.表示类
#print(soup.select('.wrapper'))
#先定位到 top-nav(标签) 再定位到ul(层级，而不是标签)  a(标签)
#print(soup.select('.top-nav > ul > li > a')[0])
#print(soup.select('.top-nav > ul a')[0])

# print(soup.select('.top-nav > ul a')[0].get_text())
# print(soup.select('.top-nav')[0].get_text())
print(soup.select('.top-nav')[0].string)
