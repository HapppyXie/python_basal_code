#识别古诗文网的验证码
import requests
from lxml import etree
import pytesseract
from PIL import Image

if __name__=='__main__':
    url='https://so.gushiwen.cn/user/login.aspx?'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    page = requests.get(url=url,headers=headers)
    #page.encoding = page.apparent_encoding
    page_text = page.text
    etree = etree.HTML(page_text)
    tmp=etree.xpath('/html/body/form[1]/div[4]/div[4]/img/@src')[0]
    #print(tmp)
    url_='https://so.gushiwen.cn'+tmp
    img_data=requests.get(url=url_,headers=headers).content
    with open('./code.jpg','wb') as fp:
        fp.write(img_data)
    #手动添加pytesseract路径
    tesseract_cmd=r'D:\谷歌浏览器\Tesseract\tesseract-ocr\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd=tesseract_cmd
    image = Image.open('code.jpg')
    image = image.point(lambda x: 0 if x < 143 else 225)
    code_text=pytesseract.image_to_string(image)
    print(code_text)




