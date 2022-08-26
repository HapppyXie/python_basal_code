# Athour:Mr Xie
# 开发时间:2022/2/25 14:17
'''
selenium处理iframe(可处理滑块)
如果定位到的标签存在于iframe之中的则须在如下操作在进行标签定位bro.switch_to.frame('id')
动作链(拖动):from selenium.webdriver import ActionChains
    1.实例化一个动作链对象：action = ActionChains(bro)
    2.click_and_hold(div)  长按且点击操作
    3.move_by_offset(x,y)
    4.perform()让动作链立即执行
    5.action.release()释放动作链资源


'''

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains

bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
#菜鸟教程
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#无法查到
#div = bro.find_element_by_id('draggable')
#需通过iframe定位  被拖模块被嵌套在iframe

#如果定位到的标签存在于iframe之中定位的则须在如下操作在进行标签
bro.switch_to.frame('iframeResult')#切换浏览器标签的作用域
div = bro.find_element_by_id('draggable')

#动作：点击-长按-移动-松开
#导入动作链   from selenium.webdriver import ActionChains
#实例化动作链 , 将浏览器参数传入
action = ActionChains(bro)
#已定位到
action.click_and_hold(div)


#模拟人
# for i in range(5):
#     #perform表示立即执行
#     #action.move_by_offset(x,y)
#     action.move_by_offset(17,0).perform()
#     sleep(0.3)
#释放动作链
action.release()

#bro.quit()