# Athour:Mr Xie
# 开发时间:2022/2/25 13:00
'''
https://www.taobao.com
'''
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
bro.get('https://www.taobao.com')

#标签定位 find_element_by_.....一系列标签定位元素
search_input = bro.find_element_by_id('q')

#标签交互,传入参数
search_input.send_keys('Iphone')

#执行一次js代码  选择滑轮向下滑动 按console     指令window.scrollto(x,y)  x横向，y纵向(document.body.scrollHeight，滚动一屏高)     js代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#再定位到搜索按钮
btn = bro.find_element_by_class_name('btn-search')
#点击按钮
btn.click()
sleep(1)

#还可以再次向其他网址发请求
bro.get('https://www.baidu.com/')
sleep(2)
#回退 到淘宝
bro.back()
sleep(2)
#再前进到百度
bro.forward()
sleep(2)
bro.quit()





