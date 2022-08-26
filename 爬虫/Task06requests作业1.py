# Athour:Mr Xie
# 开发时间:2022/2/12 14:41
import requests
import json
if __name__=='__main__':
    #1.url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    #2.UA伪装
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    #3.处理Post参数
    params = {'cname':'',
               'pid':'',
                'keyword': '湛江',
                'pageIndex': '1',
                'pageSize': '10'}
    #4.发出请求
    response = requests.post(url=url,params=params,headers=headers)
    data_text = response.text
    #5.对象持久化
    fp = open('kendeji.txt','w',encoding='utf-8')
    fp.write(data_text)
    print('over!!!')