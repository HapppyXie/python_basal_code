# Athour:Mr Xie
# 开发时间:2022/3/12 21:50
'''
验证码是一种反爬机制
识别验证码的操作：云打码:网站没了，超级鹰
相信可以使用本地工具实现验证码提取,人工智能图像识别

模拟登录，当信息填写完毕，点击登录时，浏览器会发起一个请求,可通过抓包工具，network，勾上Perserve log

HTTP/HTTP协议特性:无状态，即用户登录成功后，不会实时记录用户的登录状态
                加上cookie（用来记录用户的活动）
        cookie：手动添加（抓包后手动添加），自动添加（第一次登陆后由服务器创建）

需求：对人人网进行模拟登录
    1.点击登录按钮后发起一个post请求
    2.post请求后会携带登录之前录入的相关登录信息(用户民，密码，验证码....)
    3.验证码每次请求都会动态变化

get请求登录成功后里面会包含登录信息
post请求，需在请求头加上登录信息
'''
import requests
import pytesseract
from lxml import etree

if __name__=='__main__':
    url='https://passport2.chaoxing.com/login?loginType=3&newversion=true&fid=-1&hidecompletephone=0&ebook=0&allowSkip=0&refer=https%3A%2F%2Fi.chaoxing.com&accounttip=&pwdtip=&doubleFactorLogin=0'
    headers={
       'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
       'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Cookie':'JSESSIONID=8BF3716976B7E0DEFE09F2E44FD0AB07; route=3a66e47c0ac92560e5c67cd5e1803201; fid=14294; source=""; uname=20250809202; lv=2; _uid=146839421; uf=b2d2c93beefa90dc55aee2f4737565eca020db6b783505f3bb0498a486433f9414b77cd7efdbb7a635bec763d746276630d92481d752d66f88b83130e7eb47041a57b67f4865bf460246270a56330e6c57113d8a7ab747e40ad4450f9132c2e0cc20e4e5a952aed7; _d=1656988533134; UID=146839421; vc=261D462C661FF1C704841DDFBD0F2D52; vc2=A951F6CE4AC3A6A7847EC6C783543B47; vc3=e%2Fi04fhpdLYp3cbeF7vprdjRxseD9hMttv8P7VV1N8XDnWFJHkiBLl%2FMt7q9AOGuWQYz3hhjilBa66ZUK6VavDScC6L2XW9wAgoN1ZZ%2BYayWIraDA7KLsvgoJ8tkiNaqhJikKLxZuagC0%2BEpHQ3XUEF%2FhkPliMZKn4X1v%2BcFMiE%3D8a5fd74b129d406d544cacfd0a8dd875; xxtenc=13a99a2a4020ee70b92329fa768ba23f; DSSTASH_LOG=C_38-UN_181-US_146839421-T_1656988533135; spaceFid=14294; spaceRoleId=""'
        ,
        'Host':'passport2.chaoxing.com',
        'Refere':'https://i.chaoxing.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
             }
    page = requests.get(url=url,headers=headers)
    #page.encoding=page.apparent_encoding
    #page_text = page.text
    print(page.status_code)
    print(page.text)

