# Athour:Mr Xie
# 开发时间:2022/4/28 19:23
import requests
from bs4 import BeautifulSoup

if __name__=='__main__':
    url='https://so.gushiwen.cn/mingju/juv_2d8bb03f1e19.aspx'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    html = requests.get(url,headers)
    soup = BeautifulSoup(html.content,'lxml')

