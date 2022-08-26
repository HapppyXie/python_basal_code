# Athour:Mr Xie
# 开发时间:2022/2/11 14:33
'''
破解百度翻译,抓取局部数据
通过检查发现为post请求,请求发送后为json数据

post(url, data=None, json=None, **kwargs):
    data为局部查找的数据，字典封装
'''
import requests
import json
if __name__ == "__main__":
    #1.制定url
    post_url='https://fanyi.baidu.com/sug'
    #2.UA伪装
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    #3.post请求参数处理(同get请求一致)
    #实现动态化
    kw = input('enter a word:')
    data = {'kw': kw}
    #4.发送请求
    response=requests.post(url=post_url,data=data,headers=headers)
    page_dict = response.json()
    #json()直接返回Object,确定响应数据为json类型才可
    fileName=kw+'.json'
    fp=open(fileName,mode='w',encoding='utf-8')
    json.dump(page_dict,fp,ensure_ascii=False)
    print('over!!')


