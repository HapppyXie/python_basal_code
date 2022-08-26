import requests
from lxml import etree
'''
视频动态加载出来
'''

if __name__=='__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url='https://www.pearvideo.com/'
    page = requests.get(url=url,headers=headers)
    page.encoding = page.apparent_encoding
    page_text = page.text
    etree = etree.HTML(page_text)
    li_list = etree.xpath('//*[@id="actwapSlideList"]/li/a/@href')
    for i in li_list:
        detail_url = 'https://www.pearvideo.com/'+i
        detail_page = requests.get(url=detail_url,headers=headers).text

#https://video.pearvideo.com/mp4/adshort/20220607/cont-1764629-15892192_adpkg-ad_hd.mp4
#https://video.pearvideo.com/mp4/adshort/20220607/1657014614215-15892192_adpkg-ad_hd.mp4
#


