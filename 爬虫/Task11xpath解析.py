# Athour:Mr Xie
# 开发时间:2022/2/21 21:11
'''
xpath解析:最常用，最高效
1.标签定位
2.实例化一个etree的对象，将需要解析的源码数据加载到该对象中
3.调用etree中的xpath方法结合xpath表达式实现标签定位和内容获取

 pip install lxml

 实例化
 from lxml import etree
 1.将本地html文档中的源码数据加载到etree对象中etree()
    etree.parse(filepath)
 2.加载互联网上获取的源码数据到etree()
    etree.HTML('page_text')

 xpath('xpath表达式')   返回列表，通过层级定位：
 1./表示从根节点开始,也可表示一个层级，//表示多个层级
 2.tree.xpath('//div')#表示可从任意位置定位标签
 3.属性定位 //tag[@attrName = "attrValue"]
 4.索引定位,tree.xpath('//div[@class="top-nav"]/ul/li[1]')#在ul下有多个li,从1开始
 5.*任意元素
 取文本：/text()获得直系内容  //text()获得非直系的内容
 取属性：/@attrName

网页抓包中，element中可以通过ctrl+f实验xpath表达式


有时候xpath定位不到元素，需要手写xpath
1.元素没有id，name，class等明显的唯一属性
2.元素id是动态的
3.元素定位工具抓取不到
4.复制的xpath不稳定
    元素本身没有变，其他元素修改导致该元素定位失败

特点：灵活，稳定，效率
 第24集
 http://www.sogou.com/
'''
from lxml import etree
if __name__=='__main__':
    parser = etree.HTMLParser(encoding='utf-8')#本地html文档书写不规范，编制解析器
    tree = etree.parse('testData.html',parser=parser)#导入本地文档

    #r = tree.xpath('/html/head/meta')#定位的是标签,返回最后的标签里的内容的列表,内容被抽象成element元素类型
    # r = tree.xpath('/html/body/div')
    # print(r)

    # r = tree.xpath('/html//div')#//多个层级
    # print(r)

    # r = tree.xpath('//div')#表示可从任意位置定位标签      #<div(标签) class=".."(属性)>
    # print(r)
    # r = tree.xpath('//div[@class = "header"]')#属性定位 //tag[@attrName = "attrValue"]
    # print(r)

    #r = tree.xpath('//div[@class="top-nav"]/ul/li[1]/span/text()')#在ul下有多个li,索引定位，从1开始
    # print(r)

    #r = tree.xpath('//div[@class="top-nav"]//li[2]/a/text()')[0]
    #print(r)

    #r = tree.xpath('//li[7]/a/text()')
    # r = tree.xpath('//li[7]//text()')#//text()获得非直系的内容
    # print(r)

    # r = tree.xpath('//ul//text()')
    # r = tree.xpath('//div[@class ="top-nav"]/ul//text()')
    # print(r)

    # r = tree.xpath('//div[@class="ft"]/a/@href')#取属性/@attrName
    # print(r)