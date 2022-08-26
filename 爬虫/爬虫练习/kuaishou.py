# Athour:Mr Xie
# 开发时间:2022/3/9 21:20
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import os
'''

https://graph.qq.com/oauth2.0/show?

'''

if __name__=='__main__':

    def getCookie():

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25',
        }
        bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
        bro.get('https://www.kuaishou.com/')
        bro.find_element_by_xpath('//*[@id="app"]/div[1]/section/div/div/header/div/div[3]/ul/li[3]/div/p').click()
        bro.implicitly_wait(10)
        bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/div[1]/div/input').send_keys('13428394849')
        bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/span').click()
        code = input('yzm:')
        sleep(5)
        bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/div[2]/div/input').send_keys(code)
        sleep(1)
        bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div/div/div[1]/div/button').click()
        sleep(5)
        print(bro.get_cookies())
        sleep(5)



    #使用cookie登录
    def denglu():
        bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
        bro.get('https://www.kuaishou.com/')
        bro.implicitly_wait(10)
        bro.delete_all_cookies()
        cookies=[{'domain': 'www.kuaishou.com', 'httpOnly': False, 'name': 'kuaishou.server.web_ph', 'path': '/', 'secure': False, 'value': '497cd3a731043d8ef622c1f1a4967ff96534'}, {'domain': 'www.kuaishou.com', 'httpOnly': True, 'name': 'kuaishou.server.web_st', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABRxwCWE74rEfAnsKZAEaj92ToLYCLv1STExUvkAfMb9P0LTC49CGc8GTwnGYmL-KmH47dQfojoAwmT_Z7e9GJS7zEBzwNrAMaBa2Qn_I_hZ2lwRQOTyjDz9EmXEKxWDi6q-aAOY_-83C1_lr7KUCpgbAOU1bFn2QSV__sMkyQadLLfjXbcrOd-WUVadJRycv2GYx1M2DVk35W3y00c0I9rhoSoJCKbxHIWXjzVWap_gGna5KjIiCzeVQWmPy3UBXCoJzAqsgl59TqWsjJTtzpzrLKIOfqzigFMAE'}, {'domain': '.kuaishou.com', 'expiry': 1678377077, 'httpOnly': False, 'name': 'did', 'path': '/', 'secure': False, 'value': 'web_4b3067d2b687e8ecc0e06b62d4d3a831'}, {'domain': '.kuaishou.com', 'httpOnly': False, 'name': 'userId', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2813285325'}, {'domain': '.www.kuaishou.com', 'expiry': 1678377077, 'httpOnly': True, 'name': 'kpf', 'path': '/', 'secure': False, 'value': 'PC_WEB'}, {'domain': '.kuaishou.com', 'expiry': 1678377077, 'httpOnly': True, 'name': 'clientid', 'path': '/', 'secure': False, 'value': '3'}, {'domain': '.www.kuaishou.com', 'expiry': 1678377077, 'httpOnly': True, 'name': 'kpn', 'path': '/', 'secure': False, 'value': 'KUAISHOU_VISION'}]

        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            bro.add_cookie(cookie)
        bro.refresh()
        bro.get('https://www.kuaishou.com/')
        sleep(20)

#getCookie()

denglu()

#23:35获得cookie
#[{'domain': '.kuaishou.com', 'expiry': 1678376075, 'httpOnly': True, 'name': 'clientid', 'path': '/', 'secure': False, 'value': '3'}, {'domain': '.www.kuaishou.com', 'expiry': 1678376075, 'httpOnly': True, 'name': 'kpn', 'path': '/', 'secure': False, 'value': 'KUAISHOU_VISION'}, {'domain': '.kuaishou.com', 'expiry': 1678376075, 'httpOnly': False, 'name': 'did', 'path': '/', 'secure': False, 'value': 'web_9ba56af0680392cccdcf68e903a822f2'}, {'domain': '.www.kuaishou.com', 'expiry': 1678376075, 'httpOnly': True, 'name': 'kpf', 'path': '/', 'secure': False, 'value': 'PC_WEB'}]
