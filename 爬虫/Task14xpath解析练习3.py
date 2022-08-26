# Athour:Mr Xie
# 开发时间:2022/3/8 20:20
'''
作业：爬取站长素材中免费简历模板

'''
import requests
from lxml import etree
import os
import re
if __name__=='__main__':
    if not os.path.exists('./jianlilibs'):
        os.mkdir('./jianlilibs')

    url = 'https://aspx.sc.chinaz.com/query.aspx?keyword=免费简历模板'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    page = requests.get(url=url,headers=headers)
    page.encoding = 'utf-8'
    page_text = page.text
    tree = etree.HTML(page_text)
    url_list = []
    div_list = tree.xpath('//div[@id="ulcontent"]/div[1]/div')
    for div in div_list:
        url = 'https:'+div.xpath('./div[1]/a/@href')[0]
        url_list.append(url)

    url_jianli = []
    for url in url_list:
        page = requests.get(url=url,headers=headers)
        page.encoding = page.apparent_encoding
        page_text = page.text
        tree = etree.HTML(page_text)
        #//*[@id="down"]/div[2]/ul/li[1]/a
        temp = tree.xpath('//div[@id="down"]/div[2]/ul/li[1]/a/@href')
        if temp == []:
            continue
        pattern = 'https:.*?rar'
        if re.match(pattern,temp[0]) == None:
            continue
        url_jianli.append(temp[0])

    for url in url_jianli:
        pattern = 'https://downsc.chinaz.net/Files/DownLoad/.*?/.*?/(.*?).rar'
        name = re.findall(pattern,url)[0]
        page = requests.get(url=url,headers=headers)
        #如何保存压缩文件
        page.encoding = page.apparent_encoding
        page_text = page.content
        #压缩包应该用什么二进制格式获取
        with open('jianlilibs/'+name+'.rar','wb') as fp:
            fp.write(page_text)
            exit()


