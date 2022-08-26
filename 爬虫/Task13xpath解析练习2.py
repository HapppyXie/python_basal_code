# Athour:Mr Xie
# 开发时间:2022/2/23 13:35
'''
需求：解析下载图片数据https://pic.netbian.com/

https://pic.netbian.com/4kmeinv/index_1.html
https://pic.netbian.com/4kmeinv/index_2.html

27页
'''
import requests
from lxml import etree
import os

# if __name__=='__main__':
#     if not os.path.exists('./meinv'):
#         os.mkdir('./meinv')
#
#     url = 'https://pic.netbian.com/4kmeinv/index.html'
#     headers = {
#         'User-Agent':'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
#     }
#     page = requests.get(url=url,headers=headers)
#     page.encoding = page.apparent_encoding
#     tree = etree.HTML(page.text)
#     li_list = tree.xpath('//ul[@class="clearfix"]/li')#获得li标签的列表
#     for li in li_list:
#         img_src = li.xpath('./a/img/@src')[0]#./表示li的同时也表示了一个层级
#         img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
#         #https://pic.netbian.com/uploads/allimg/220221/224056-16454544561986.jpg
#         img_url = 'https://pic.netbian.com'+img_src
#         img = requests.get(url=img_url,headers=headers).content
#         img_path = './meinv/'+img_name
#         #二进制本身就是一种编码
#         with open(img_path,'wb') as fp:
#             fp.write(img)
#             print(img_name+'下载成功!!!')

'''
换页
https://pic.netbian.com/4kmeinv/index_1.html
https://pic.netbian.com/4kmeinv/index_2.html

中文乱码问题通解: str.encode('iso-8859-1').decode('gbk')            
                str.encoding = 'utf-8'
                str.encoding = str.apparent_encoding
'''
if __name__=='__main__':
    if not os.path.exists('./meinv'):
        os.mkdir('./meinv')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) ' \
                                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 ' \
                                  'SLBrowser/7.0.0.12151 SLBChan/25'    }
    for num in range(2,5):
        url = 'https://pic.netbian.com/4kmeinv/index_'+str(num)+'.html'
        page = requests.get(url=url,headers=headers)
        page.encoding = page.apparent_encoding
        tree = etree.HTML(page.text)
        li_list = tree.xpath('//ul[@class="clearfix"]/li')#获得li标签的列表
        for li in li_list:
            img_src = li.xpath('./a/img/@src')[0]#./表示li的同时也表示了一个层级
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            #https://pic.netbian.com/uploads/allimg/220221/224056-16454544561986.jpg
            img_url = 'https://pic.netbian.com'+img_src
            img = requests.get(url=img_url,headers=headers).content
            img_path = './meinv/'+img_name
            #二进制本身就是一种编码
            with open(img_path,'wb') as fp:
                fp.write(img)
                print(img_name+'下载成功!!!')
