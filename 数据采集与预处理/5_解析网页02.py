# Athour:Mr Xie
# 开发时间:2022/4/23 16:57
from bs4 import BeautifulSoup
import re

if __name__=='__main__':
    fp = open('data02.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.find_all('a'))

    # for tag in soup.find_all(re.compile('b')):
    #     print(tag)

    #print(soup.find_all(['a','b']))

    #print(soup.find_all(id=True))

    # def has_class_but_no_id(tag):
    #     return tag.has_attr('class') and not tag.has_attr('id')
    # print(soup.find_all(has_class_but_no_id))

    # print(soup.find_all(id='link2'))
    # print(soup.find_all(href=re.compile('spark')))
    #使用多个指定名字的参数可以同时过滤Tag的多个属性
    #print(soup.find_all(href='http://example.com/hadoop',id='link1'))
    #如果指定的key是Python的关键词，则后面需要加下划线
    #print(soup.find_all(class_='software'))

    # print(soup.a)
    # print(soup.find_all(text='Hadoop'))
    # print(soup.find_all(text=['Hadoop','Spark','Flink']))
    # print(soup.find_all(text='Bigdata'))
    # print(soup.find_all(text='BigData Software'))
    # print(soup.find_all(text=re.compile('bigdata')))

    # print(soup.find_all('a'))
    # print(soup.find_all('a',limit=2))

    # print(soup.find_all('a'))
    # print(soup.find_all('a',recursive=False))#a标签在p标签内，p标签在body内

    # print(soup.select('a'))
    # print(soup.select('.software'))
    # print(soup.select('#link1'))
    # print(soup.select('p #link1'))#组成查找

    # print(soup.select('head > title'))
    # print(soup.select('p > a:nth-of-type(1)'))
    # print(soup.select('p > a:nth-of-type(2)'))
    # print(soup.select('p > a:nth-of-type(3)'))

    #print(soup.select('a[class="software"]'))#a标签中，类为software
    #print(soup.select('p a[href="http://example.com/hadoop"]'))
    #以上的select方法返回的结果都是列表形式，
    # 可以以遍历的形式进行输出，然后用 get_text()方法来获取它的内容
    #print(type(soup.select('title')))
    #print(soup.select('title')[0].get_text())




