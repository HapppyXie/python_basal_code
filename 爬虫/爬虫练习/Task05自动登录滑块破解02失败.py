# Athour:Mr Xie
# 开发时间:2022/2/25 19:56
'''
滑块距离不固定，每张图片都不同
每5次不成功，需要重试
'''
from selenium import webdriver
from time import sleep
#判断属性是否加载完毕
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
#导新包抠图片
from PIL import Image
from selenium.webdriver import ActionChains
import sys

bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
#无需UI伪装
bro.get('https://www.cods.org.cn/')
sleep(2)
#获取input属性值
bro.find_element_by_id('checkContent_index').send_keys('猫猫')
sleep(1)
#此为等待一个元素   all等待加载完毕
btn = WebDriverWait(bro,10).until(ec.presence_of_element_located((By.ID,'checkBtn')))
#执行一次js语句 此处使用bro.find...会报错
bro.execute_script("arguments[0].click()",btn)
sleep(1)
bro.refresh()

#定义公式通过扫描图层中颜色较深的地区
#查看每个点的颜色通道，越接近于0越黑，越接近于255越白
#(1, 47, 90, 255)
#(0, 49, 94, 255)
#(0, 49, 94, 255)
#连续三次出现说明是一片区域
def get_len():
    im = Image.open('yzm.png')
    chang=0
    for x in range(im.size[0]):
        a=0
        for y in range(im.size[1]):
            rgb = im.load()[x,y]
            #print(rgb)  0-r 1-g 2-b
            if rgb[0]<110 and rgb[1]<70 and rgb[2]<30:
                a+=1
            if a>=10:
                return x
    return chang

#自动计算距离，不保证每次一定正确,计算4次错误，bro.fresh()重新刷新
while True:
    for i in range(4):
        if i == 3:
            print('次数不够，刷新！！')
            bro.refresh()
            sleep(1.5)
        else:
            slider = WebDriverWait(bro,10).until(ec.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
            #有的class为双class，复制一个即可                                       ((一个元组参数))         标签里有img的才行
            img = WebDriverWait(bro,10).until(ec.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
            location = img.location
            size = img.size
            #从页面源码中获取数据
            left,top,right,buttom = location['x']+97,location['y']+52,location['x']+size['width']+155,location['y']+size['height']+88
            #标表1(左上)，坐标2(从坐标1左下)
            #坐标出现误差可能是故意的陷阱
            bro.get_screenshot_as_file('full.png')
            #打开图片
            img = Image.open('full.png')
            #开始用从页面源码得到的参数抠图 img.crop((元组参数))
            #用新变量接受
            img = img.crop((left,top,right,buttom)) #xmin ymin xmax ymax
            img.save('yzm.png')
            distance = get_len()
            print(distance)

            #distacne有时计算成0，有时计算大于或小于实际长度
            #测试结果 138，234，219，0，102，0，0，104，0，163    =0或>=250(一般是160)异常
            if distance == 0 or distance>210:
                #可能由于请求超时等引发，将线程暂时挂起，等刷新加载完，再刷新，不报错
                WebDriverWait(bro,20).until(ec.presence_of_element_located((By.CLASS_NAME,'geetest_refresh_1')))
                bro.find_element_by_class_name('geetest_refresh_1').click()
                #网速慢导致的刷新慢
                sleep(1.5)
                continue
            #距离计算正确，移动
            else:
                action_chains=ActionChains(bro)
                action_chains.click_and_hold(slider)
                action_chains.pause(0.2)
                action_chains.move_by_offset(distance+5,0)
                action_chains.pause(0.2)
                action_chains.move_by_offset(-10,0)
                action_chains.pause(0.2)
                action_chains.move_by_offset(5,0)
                action_chains.release()#松开
                action_chains.perform()
                sleep(1)
            if bro.title=='sorry':
                bro.quit()
                sys.exit()