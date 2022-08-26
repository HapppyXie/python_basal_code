# Athour:Mr Xie
# 开发时间:2022/2/16 20:36
#三种数据解析:1.正则 2.bs4 3.xpath(***)
'''
打开页面源码,找到要解码的数据，大部分存储于对应的标签中(定位中对应的标签)

需求：爬取糗事百科中的所有图片 (爬取一张页面的全部图片)
    复制图片地址，百度可打开
'''
import  requests
import re
import os

#图片爬取
if __name__=='__main__':
    url='https://img-nos.yiyouliao.com/inforec-20220216-e7e7f55f7e03b736c838b8eeceb930c6.jpg?time=1645016170&signature=2571852106C5B6A9E81364232B06CB14'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
    }
    #图片返回二进制文件数据，content ;  字符串text，对象json
    image_data = requests.get(url=url,headers=headers).content
    #注意wb写入二进制文件
    with open('C:Users\mike\Desktop\myImage.jpg','wb') as fp:
        fp.write(image_data)
    print('over!!!')



'''

<div class="summary-text">
<p>                         detail\d{2}/\d{5}
<a target="_blank" href="/detail59/58636.html">
<img src="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/04/0E/ChMkJ1mvdSaIViq4ADYK5g0qldQAAgOcgAF2PYANgr-558.gif" alt="因为电击，手的肌肉收紧，也无法松开导电的东西..." title="点击查看大图">
</a>
</p>
</div>


<div class="summary-text">
<p>
<a target="_blank" href="/detail59/58579.html">
<img src="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/03/00/ChMkJ1mo3peIcA7bAB7Iv-1d8F8AAgHFQDWNEEAHsjX116.gif" alt="水平入水满分" title="点击查看大图">
</a>
</p>
</div>

<div class="summary-text">
<p>
<a target="_blank" href="/detail52/51381.html">
<img src="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/0C/0D/ChMkJlfA75CIJQWuACzj1YHkfh8AAUwfwM1ksIALOPt366.gif" alt="广东五华：五岁男童“驾”摩托撞上货车" title="点击查看大图">
</a>
</p>
</div>

只匹配了5个
第六个
<div class="summary-text">
<p>
<a target="_blank" href="/detail51/50826.html">
!!前面为<img src   ->修改 <img .*?src="
<img loadsrc="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/06/0B/ChMkJletZHGIP3NpADJcM-usFToAAUYDwFcWpMAMlxL497.gif" alt="巴西的人不靠谱，马更不靠谱。。。" title="点击查看大图" src="https://xiaohua-fd.zol-img.com.cn/t_s300x2000/g5/M00/06/0B/ChMkJletZHGIP3NpADJcM-usFToAAUYDwFcWpMAMlxL497.gif" shid="1" style="opacity: 1;">
</a>
</p>
</div>
'''

# if __name__=='__main__':
#     # 图片存储到文件夹中os块,创建一个文件夹  ./原地创建目录
#     if not os.path.exists('./qiutulibs'):
#         os.mkdir('./qiutulibs')
#
#     url='https://xiaohua.zol.com.cn/qutu/qiushi/'
#     headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
#     }
#     data_text = requests.get(url=url,headers=headers).text
#     #正则解析，匹配图片链接
#     #detail\d{2}/\d{5}                                                                      <img .*?src="
#     pattern = '<div class="summary-text"><p><a target="_blank" href="/detail\d{2}/\d{5}.html"><img .*?src="(.*?)" alt.*?</a></p></div>'
#     #print(data_text)
#     id_list = re.findall(pattern=pattern,string=data_text)
#     #print(id_list)
#     #得到一页图片url
#     #遍历依次获得图片,id为str类型
#     for id in id_list:
#         image_data=requests.get(url=id,headers=headers).content
#         #生成图片名称，其url最后的即是其名称
#         image_name=id.split('/')[-1]
#         #指定图片最终存储的路径
#         imagePath='qiutulibs/'+image_name
#         with open(imagePath,'wb') as fp:
#             fp.write(image_data)
#             print(image_name,'下载成功!')


'''
换页爬取
第一页 https://xiaohua.zol.com.cn/qutu/qiushi/1.html
第二页 https://xiaohua.zol.com.cn/qutu/qiushi/2.html
发现后面变量
'''

# if __name__=='__main__':
#     if not os.path.exists('./qiutulibs'):
#         os.mkdir('./qiutulibs')
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
#     }
#     #url变动，先循环10页
#     for page in range(1,11):
#         url='https://xiaohua.zol.com.cn/qutu/qiushi/'+str(page)+'.html'
#         #url='https://xiaohua.zol.com.cn/qutu/qiushi/'
#
#         data_text = requests.get(url=url,headers=headers).text
#         pattern = '<div class="summary-text"><p><a target="_blank" href="/detail\d{2}/\d{5}.html"><img .*?src="(.*?)" alt.*?</a></p></div>'
#         id_list = re.findall(pattern=pattern,string=data_text)
#         for id in id_list:
#             image_data=requests.get(url=id,headers=headers).content
#             image_name=id.split('/')[-1]
#             imagePath='qiutulibs/'+image_name
#             with open(imagePath,'wb') as fp:
#                 fp.write(image_data)
#                 print(image_name,'下载成功!')