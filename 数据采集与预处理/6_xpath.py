# Athour:Mr Xie
# 开发时间:2022/5/3 15:12
from lxml import etree
if __name__=='__main__':
    with open('data02.html','r',encoding='utf-8') as fp:
        html=etree.HTML(fp.read())
        #html_data = html.xpath('body')
        # for element in html_data:
        #     print(etree.tostring(element))
        #
        # html_data = html.xpath('//a')
        # for element in html_data:
        #     print(etree.tostring(element))
        #
        # html_data = html.xpath('//p[@class="bigdata"]/a[@id="link2"]')
        # for element in html_data:
        #     print(etree.tostring(element))

        html_data = html.xpath('//body/p[@class="bigdata"]')
        for element in html_data:
            print(etree.tostring(element))


