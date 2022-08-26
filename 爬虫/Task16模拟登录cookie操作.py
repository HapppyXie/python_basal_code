# Athour:Mr Xie
# 开发时间:2022/3/12 22:33
'''
发请求服务器没有记录过去请求的状态（已登录），导致请求到登录页面，无法拿到源码数据
http/https特性：无状态，服务器端不会记录当前请求的状态
cookie：用来让服务器端记录客户端的相关状态（已经登录），有有效时长，不同网站可能会变化

解决：
    1.在需要发请求的页面，通过抓包，找到对应url的数据包，有对应的cookie，将cookie封装到headers中，发情求时带上(不建议，手动)
    2.cookie来自，进行模拟登录后，请求后由服务器端创建(set-cookie)
        session会话对象:
            作用：1.可以进行请求的发送（方式和requests相同）；
                 2.人工请求过程中产生cookie，则该cookie会自动存储/携带在该session对象中

    1.创建一个session对象，session = requests.Seesion()
    2.使用session对象进行模拟登录，发送请求(cookie就会自动存储在session中)
    3.session对象对目标主页发送请求(携带了cookie)

    模拟登录后的数据包：含有login的，在其页面发现set-cookie，复制数据包url，有参数则封装为data


'''

from selenium import webdriver
from time import sleep
import time
import requests
from selenium.webdriver import ActionChains
import json

def getCookie():
    bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
    bro.maximize_window()
    bro.implicitly_wait(5)#隐形等待5秒
    bro.get('https://www.jd.com/')
    bro.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
    sleep(0.5)
    bro.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
    sleep(0.5)
    username = bro.find_element_by_xpath('//*[@id="loginname"]')
    username.clear()
    username.send_keys('13428394849')
    sleep(0.5)
    bro.find_element_by_xpath('//*[@id="nloginpwd"]').send_keys('wsAD1643156841')
    sleep(0.5)
    bro.find_element_by_xpath('//*[@id="loginsubmit"]').click()
    cookies = bro.get_cookies()
    print(cookies)

    sleep(100)

def loginCookie():
    #settings-Editor-general-soft wrap -加如py文件格式  :自动换行
    #cookies中记录了登录状态，用户，密码，时间，干了什么事情
    cookies=[{'domain': '.jd.com', 'expiry': 1673082263, 'httpOnly': False, 'name': '3AB9D23F7A4B3C9B', 'path': '/', 'secure': False, 'value': 'L53IM7MTMLHI5EFJ4YHAC3UBMMFONMAI2Z7NIDEHLCNWINO4ECFYK5J6DIK2LPMODRCVQREWHN4HGXCJNFWFYFVYR4'}, {'domain': '.jd.com', 'expiry': 1662714262, 'httpOnly': False, 'name': '__jda', 'path': '/', 'secure': False, 'value': '122270672.16471622606431272528372.1647162261.1647162261.1647162261.1'}, {'domain': '.jd.com', 'expiry': 1648026261, 'httpOnly': False, 'name': 'areaId', 'path': '/', 'secure': False, 'value': '19'}, {'domain': '.jd.com', 'expiry': 1647164062, 'httpOnly': False, 'name': 'shshshsID', 'path': '/', 'secure': False, 'value': 'ea4dd705a2068ec03766463bd6886287_1_1647162262177'}, {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfpb', 'path': '/', 'secure': False, 'value': 'jnl1YRkYh-A-yyKfg7oWGzw'}, {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfpa', 'path': '/', 'secure': False, 'value': '830a68e2-106a-63d9-7a33-6e39051a6a0f-1647162262'}, {'domain': '.jd.com', 'httpOnly': False, 'name': '__jdc', 'path': '/', 'secure': False, 'value': '122270672'}, {'domain': '.jd.com', 'expiry': 1647767061, 'httpOnly': False, 'name': 'PCSYCityID', 'path': '/', 'secure': False, 'value': 'CN_440000_440100_0'}, {'domain': '.jd.com', 'expiry': 1648026261, 'httpOnly': False, 'name': 'ipLoc-djd', 'path': '/', 'secure': False, 'value': '19-1601-0-0'}, {'domain': 'passport.jd.com', 'httpOnly': False, 'name': '_t', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'tXs4HAzNliW2BDgpgyrCaAG9kJ4rlNsa31iysjopoaw='}, {'domain': '.jd.com', 'expiry': 2511162262, 'httpOnly': False, 'name': 'shshshfp', 'path': '/', 'secure': False, 'value': 'b821c3f63261cf769679275970b3ed54'}, {'domain': '.jd.com', 'httpOnly': False, 'name': 'wlfstk_smdl', 'path': '/', 'secure': False, 'value': 'mg4gpe5c0lh4w0rj4ciezpfhqcb9phib'}, {'domain': '.jd.com', 'expiry': 1647164062, 'httpOnly': False, 'name': '__jdb', 'path': '/', 'secure': False, 'value': '122270672.3.16471622606431272528372|1.1647162261'}, {'domain': '.jd.com', 'expiry': 1662714265, 'httpOnly': False, 'name': '__jdu', 'path': '/', 'secure': False, 'value': '16471622606431272528372'}, {'domain': 'passport.jd.com', 'httpOnly': True, 'name': 'alc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'fAkRFbN3TLHA2+Z0tjSTCA=='}, {'domain': '.jd.com', 'expiry': 1648458260, 'httpOnly': False, 'name': '__jdv', 'path': '/', 'secure': False, 'value': '76161171|direct|-|none|-|1647162260644'}]
    bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
    bro.maximize_window()
    bro.implicitly_wait(5)
    bro.get('https://www.jd.com/')
    sleep(2)
    #清除浏览器中的cookies信息
    bro.delete_all_cookies()
    #添加之前登录成功的cookies信息
    for cookie in cookies:
        temp_cookie = {}
        #expiry有效期 - 时间戳  'expiry': 1673082263
        # for key in cookie.keys():
        #     if key == 'expiry':
        #         # #直接设置expiry,获得最新时间戳
        #         # now = int(time.time()+10000)
        #         # cookie['expiry']=now
        #         cookie.pop('expiry')
        bro.add_cookie(cookie)
    bro.get('https://www.jd.com/')
    sleep(100)

def getTime():
    expiry= 2511162262 #1662714262 有效到什么时候
    timeArray = time.localtime(expiry)
    formatTime = time.strftime('%Y-%M-%D %H:%M:%S',timeArray)
    print(formatTime)






if __name__ == '__main__':
   # getCookie()
    loginCookie()
    getTime()



