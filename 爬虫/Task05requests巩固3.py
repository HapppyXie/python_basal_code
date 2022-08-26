# Athour:Mr Xie
# 开发时间:2022/2/11 15:26
'''
划页面发现出现新数据，和百度翻译输入类似，同样发出来阿贾克斯请求
网页按检查（里面网址和浏览器显示的不一样），定位到network，看XHR阿贾克斯请求，
'''
import requests
import json

if __name__=="__main__":
    #问号后面的参数可封装到字典里 https://movie.douban.com/j/chart/top_list?
    #type=24&interval_id=100%3A90&action=&start=200&limit=20,检查下面有这些参数的分列
    #1.制定url
    url='https://movie.douban.com/j/chart/top_list?'
    #2.UA伪装
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    #3.get请求参数处理
    params = {'type':'24',
              'interval_id':'100:90',
              'action':'',
              'start':'0',#指定从1开始取
              'limint':'20'}  # 限制一次取20个，'limit':'20'
    response = requests.get(url=url,params=params,headers=headers)
    list_data = response.json()
    #4.持久化存储
    fp=open('douban.json','w',encoding='utf-8')
    json.dump(list_data,fp,ensure_ascii=False)
    print('over!!!')