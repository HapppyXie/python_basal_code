# Athour:Mr Xie
# 开发时间:2022/4/28 15:00
from bs4 import BeautifulSoup
import requests
import time

#采集网页数据保存到文本文件
#https://so.gushiwen.org/mingju/

#https://so.gushiwen.cn/mingju/ 新
#请求网页
def page_request(url,ua):
    response = requests.get(url,ua)
    html = response.content.decode('utf-8')
    return html

#解析网页
def page_parse(html):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')
    sentence = soup.select('div.main3>div.left>div.sons>div.cont>a:nth-of-type(1)')
    #得到所有诗句组成的列表
    poet = soup.select('div.main3>div.left>div.sons>div.cont>a:nth-of-type(2)')
    sentence_list = []
    href_list = []
    temp_list = []
    for i in range(len(sentence)):
        temp = sentence[i].get_text()+"-------"+poet[i].get_text()
        sentence_list.append(temp)
        href = sentence[i].get('href')
        href_list.append('https://so.gushiwen.cn'+href)
        #href="/mingju/juv_2d8bb03f1e19.aspx"
        temp_list.append(href_list)
        temp_list.append(sentence_list)
    return [href_list,sentence_list]

#写入文本文件
def save_txt(info_list):
    import json
    with open(r'sentence.txt','a',encoding='utf-8') as txt_file:
        for element in info_list[1]:
            txt_file.write(json.dumps(element,ensure_ascii=False)+'\n\n')

#子网页处理函数,爬取诗句内容
def sub_page_request(info_list):
    subpage_urls = info_list[0]
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    sub_html = []
    for url in subpage_urls:
        html = page_request(url,ua)
        sub_html.append(html)
    return sub_html

#子网页解析，获取完整诗句
def sub_page_parse(sub_html):
    poem_list = []
    for html in sub_html:
        soup = BeautifulSoup(html,'lxml')
        poem = soup.select('div.left > div.sons > div.cont > div.contson')
        #div.main3>div.left>div.sons>div.cont>div.contson
        poem = poem[0].get_text()
        poem_list.append(poem.strip())
    return poem_list

#保存子网页内容
def sub_page_save(poem_list):
    import json
    with open('poem.txt','a',encoding='utf-8') as txt_file:
        for element in poem_list:
            txt_file.write(json.dumps(element,ensure_ascii=False)+'\n\n')


if __name__=='__main__':
    print('-------------开始爬取古诗文网站---------------')
    ua={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    for i in range(1,4):
        url = 'https://so.gushiwen.cn/mingju/default.aspx?p='+str(i)+'&c=&t='
        time.sleep(1)
        html = page_request(url,ua)
        info_list=page_parse(html)
        save_txt(info_list)
        #处理子网页
        print('开始解析第%d '+str(i)+' 页')
        #开始解析名句子网页
        sub_html = sub_page_request(info_list)
        poem_list = sub_page_parse(sub_html)
        sub_page_save(poem_list)
    print('---------------爬取完成----------------')
    print('共爬取%d%'+str(i*50)+'个古诗名句')

