# Athour:Mr Xie
# 开发时间:2022/4/19 21:33
from bs4 import BeautifulSoup
import requests
if __name__ =='__main__':
    #     url = 'http://www.sogou.com/'
    # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    # page_text = requests.get(url,headers).text
    # soup = BeautifulSoup(page_text,'html.parser')#html.parser更换lxml

    # content = soup.prettify()
    # print(content)

    #利用tag
    #print(soup.a)
    # print(soup.title)
    #
    # #Tag有两个重要的属性，即name和attrs
    # print(soup.name)
    # print(soup.a.attrs)
    # #如果想要单独获取某个属性，比如要获取“class”属性的值，可以执行如下代码
    # print(soup.a['onclick'])
    # print(soup.a.get('onclick'))

    #NavigableString
    # print(soup.a.string)#提取标签内部的文字
    # #BeautifulSoup对象表示的是一个文档的全部内容，
    # # 大部分时候，可以把它当作Tag对象，是一个特殊的Tag
    # print(type(soup.name))
    # print(soup.name)
    # print(soup.attrs)

    #Comment
    # fp = open('data01.html','r',encoding='utf-8')
    # soup = BeautifulSoup(fp,'lxml')
    # print(soup.a)
    # print(soup.a.string)
    # print(type(soup.a.string))#文中的注释被提取为string，但从类型可知其为comment对象

    #.cotents属性
    fp = open('data02.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    # print(soup.body.contents[0])
    #
    # for child in soup.descendants:
    #     print(child)

    # print(soup.title)
    # print(soup.title.string)
    #
    # print(soup.head)
    # print(soup.head.meta)#标签内有标签

    #print(soup.body)
    # print(soup.body.string)#body内含有多个标签，不确定返回那个，返回None
    # print(soup.body.strings)#返回生成器
    # for string in soup.strings:
    #     print(repr(string)) #repr()返回一个对象的string格式
    #
    # for string in soup.stripped_strings:
    #     print(string)#.stripped_strings属性，可以获得去掉空白行的标签内的众多内容

    # p = soup.p
    # print(p.parent.name)
    # content  = soup.head.title.string
    # print(content)
    # print(content.parent.name)

    # content = soup.head.title.string
    # print(content)
    # for parent in content.parents:
    #     print(parent.name)

    # print(soup.p.next_sibling)#到一下p标签，要先换行，返回空白
    # print(soup.p.previous_sibling)#没有前一个兄弟节点，返回None 前面没有p标签
    #
    # print(soup.p.next_sibling.next_sibling)#换行后，有一个p标签

    # for next in soup.a.next_siblings:
    #     print(repr(next))

    # print(soup.head.next_element.next_element)
    # print(soup.head.next_element.next_element.next_element.next_element)

    # for element in soup.head.next_elements:
    #     print(repr(element))

