# Athour:Mr Xie
# 开发时间:2022/2/22 19:53
'''
获得58同城二手房的名称数据

https://zhanjiang.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0031-78b7-dfab-412963c9e8fd&ClickID=4
https://zhanjiang.58.com/ershoufang/p2/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0031-78b7-dfab-412963c9e8fd&ClickID=1
'''
import requests
from lxml import etree

if __name__=='__main__':
    url = 'https://zhanjiang.58.com/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0031-78b7-dfab-412963c9e8fd&ClickID=4'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
    }
    #无乱码
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)

    #获得第一个房源名称,发现变量为div[1]
    #r = tree.xpath('//section[@class="list"]/div[1]//div[@class="property-content-title"]/h3/@title')
    div_list = tree.xpath('//section[@class="list"]/div')#获得<div tongji-tag...>列表
    print(div_list)
    for div in div_list:
        #去除的div含有html源码，仍可调xpath
        title = div.xpath('.//div[2]//h3/@title')[0]          #./表示左侧的div,如果不写,直接/表示重新从根开始
        with open('58house_title.txt','a',encoding='utf-8') as fp:
            fp.write(title+'\n')