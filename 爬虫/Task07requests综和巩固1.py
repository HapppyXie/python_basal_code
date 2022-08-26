# Athour:Mr Xie
# 开发时间:2022/2/12 15:10
'''
    http://scxk.nmpa.gov.cn:81/xk/先发请求get看看拿不拿得到

浏览器请求显示企业信息，requests请求没有,说明企业的信息不是当前requstst中的url得到的,通过xhr请求
便捷验证：检查-网络-刷新（再次请求）-all中可找到当前网页的url请求包,其中无法查到其他企业详情信息，说明其他数据是其他url加载出来的（动态加载）
        再在xhr中发现了一个xhr请求包，包含企业详情信息,有其id id=c6fe0e0c374448128149352fc8aca2a3

进入企业详情页,得其url，后面id与前网页的xhr中获取的id一致
        http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=c6fe0e0c374448128149352fc8aca2a3
        http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=5bb6d98c6f264ebcae5b4005a31fb5b6
观察可得前网页域名+id可得企业详情页url

两家企业详情页的xhr的url一样,均为post请求，只有其携带的参数不同
        http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById
        http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById

即批量获取id，id和url形成一个完整的详情页对应的xhr数据包的url
'''

import requests
import json

# if  __name__=='__main__':
#     url='http://scxk.nmpa.gov.cn:81/xk/'
#     headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
#              '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
#     page_text = requests.get(url=url,headers=headers).text
#     with open('化妆品.html','w',encoding='utf-8') as fp:
#         fp.write(page_text)
#     print('over!!!')


if __name__=='__main__':
    id_list = []  # 存储企业ID
    all_data_list = []  # 存储所有企业的详情数据
    #1.批量获取url,到首页获取其xhr的url，请求后可获得首页的各企业详情页的id
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}

    #动态换页,需缩进
    for page in range(1,6):
        page=str(page)
        data={
            'on':'true',
            'page':page,         # 第1/385页
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
        }
        response = requests.post(url=url,data=data,headers=headers)
        #获取包含id的json数据
        json_ids = response.json()
        #其中json中的数据为字典类型，可通过key(list)查询，取出id
        #数据中的结构 {....."list":[   {'ID':'132545456',..."XK_COMPLETE_DATE":{....}}   ,{'ID':'132545456',...{....}},{'ID':'132545456',...{....}},.....].......}
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
        #print(id_list)


    #获取企业详情数据
    url2='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers2={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'}
    for id in id_list:
        data={
            'id':id
            }
        #几个id发几次请求
        detail_json = requests.post(url=url2,data=data,headers=headers2).json()
        #print(detail_json)
        all_data_list.append(detail_json)

    #持久化存储
    fp = open('化妆品_all_data.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')