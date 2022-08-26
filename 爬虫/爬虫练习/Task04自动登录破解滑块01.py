# Athour:Mr Xie
# 开发时间:2022/2/25 17:53
from selenium import webdriver
from time import sleep
#隐形等待,每个人网页加载速度不一样
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
bro.get('https://mail.qq.com/')
sleep(0.4)
bro.switch_to.frame('login_frame')
bro.find_element_by_id('u').send_keys('2646793442')
bro.find_element_by_id('p').send_keys('1234567890')
sleep(0.4)
#页面对象bro等待10秒,10秒内加载出来不报错，10外报错             id此处需写为ID
WebDriverWait(bro,10).until(ec.element_to_be_clickable((By.ID,"login_button")))
bro.find_element_by_id('login_button').click()

sleep(1)
#加载出新的iframe,需重新加载
bro.switch_to.frame('tcaptcha_iframe')
sleep(0.4)
#获得拖动对象  滑块可以不精准
while True:
    slider = WebDriverWait(bro,10).until(ec.element_to_be_clickable((By.ID,'tcaptcha_drag_thumb')))
    distance = 178
    action = ActionChains(bro)
    #点击开始拖拽
    action.click_and_hold(slider)
    #假设认为拖动暂停 拖动过一点或少一点，再拖动对其
    action.pause(0.2)
    action.move_by_offset(distance+5,0)
    action.pause(0.2)
    action.move_by_offset(-10,0)
    action.pause(0.6)
    action.move_by_offset(5,0)
    action.release()
    action.perform()
    sleep(2)
    try:
        shuaxin = WebDriverWait(bro,1).until(ec.presence_of_all_elements_located((By.ID,'e_reload')))
        bro.find_element_by_id('e_reload').click()
    except:
        #不刷新说明验证成功，退出浏览器
        bro.quit()
        break;

