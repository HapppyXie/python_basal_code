# Athour:Mr Xie
# 开发时间:2022/2/25 14:49
'''
模拟qq登录

学到p54
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')

#切换账号登录
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()

#输入账户和密码
userName_tag = bro.find_element_by_id('u')
passWard_tag = bro.find_element_by_id('p')

userName_tag.send_keys('2646793442')
passWard_tag.send_keys('1234567890')

#点击登录
btn = bro.find_element_by_id('login_button')
btn.click()





