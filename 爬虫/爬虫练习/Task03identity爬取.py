# Athour:Mr Xie
# 开发时间:2022/2/19 11:38
'''

<p>
	谭龙峰 430416199901117000</p>
<p>
	范斐 410104199910170000</p>

<p>\s*?(.{2,3})\s(\d{17}x)</p>

<p>
	古蕊会 610724199403025899 23 男</p>
'''
'''
处理乱码
方法一：将requests.get().text改为requests.get().content
方法二：手动指定网页编码 手动设定响应数据的编码格式response.encoding = response.apparent_encoding
方法三：使用通用的编码方法 img_name.encode('iso-8859-1').decode('gbk')
'''
import requests
import re
if __name__=='__main__':
    url='https://www.mitao521.com/zawen/201908095101.html'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
    }
    requests.encoding='utf-8' #设置编码
    response = requests.get(url=url,headers=headers)
    response.encoding=response.apparent_encoding
    #print(response.encoding)从http中猜测响应对象原始的编码
    pattern ='<p>\s*?(.{2,3})\s(\d{17}[X|\d])\s?\d?\d?\s?.?</p>'#正则编写正确,但
    data_list=re.findall(pattern,response.text)
    for data in data_list:
        key =data[0].strip()
        temp = ''
        if len(key) == 2:
            temp = key[0]+'   '+key[1]
            key = temp
        value = data[1]
        data_final = key+'----'+value+'\n'
        with open('C:Users\mike\Desktop\mydata.txt','a',encoding='utf-8') as fp:
            fp.write(data_final)
    print('over!!!')