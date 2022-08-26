# Athour:Mr Xie
# 开发时间:2022/2/21 13:52
'''
爬取三国演义小说所有的章节标题和内容.
https://www.shicimingju.com/1870.html

三国演义首页:https://www.shicimingju.com/book/sanguoyanyi.html
三国演义第一页:https://www.shicimingju.com/book/sanguoyanyi/1.html
'''
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
    }
    page_text = requests.get(url=url,headers=headers)
    page_text.encoding = page_text.apparent_encoding
    soup = BeautifulSoup(page_text.text,'lxml')
    a_list = soup.select('.book-mulu > ul > li > a')

    #避免文件打开多次  ,其实追加模式即可
    fp = open('./三国.txt','a',encoding='utf-8')

    for a in a_list:
    #<a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义  斩黄巾英雄首立功</a>
    #  a['href']  获得  /book/sanguoyanyi/1.html
        title = a.string
        detail_url = 'https://www.shicimingju.com'+a['href']
        detail_page_text = requests.get(url = detail_url,headers=headers)
        #避免乱码
        detail_page_text.encoding = detail_page_text.apparent_encoding
        #创建BeautifulSoup对象
        detail_soup = BeautifulSoup(detail_page_text.text,'lxml')
        #属性定位
        div_tag = detail_soup.find('div',class_='chapter_content')    #此处select()无法定位到
        #得到内容
        content = div_tag.text
        content.replace(u'\xa0',u' ') #无法取消NBSP
        fp.write(title+':'+content+'\n')
        print(title+'爬取成功!!!')
