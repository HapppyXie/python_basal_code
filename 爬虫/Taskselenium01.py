# Athour:Mr Xie
# 开发时间:2022/2/25 12:03
'''
49页
selenium模块（基于浏览器自动化的一个模块）
作用：1.便捷获取动态加载数据 2.便捷实现模拟登录
流程: 1.pip install selenium
     2.下载一个浏览器驱动程序
     路径：http://chromedriver.storage.googleapis.com/index.html
     驱动程序和浏览器的映射关系:http://blog.csdn.net/huilan_same/article/details/51896672
    3.实例化一个浏览器对象
        #实例化一个浏览器对象(有选择),传入浏览器驱动程序路径
         bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
    4.基于浏览器自动化的操作代码
        发起请求:get(url)
        标签定位：find系列的方法
        标签交互：send_keys('xxx')
        执行js程序:execute_script('jsCode')
        前进,后退：back(),forward()
        关闭浏览器:quit()

    selenium处理iframe(可处理滑块)
    如果定位到的标签存在于iframe之中的则须在如下操作在进行标签定位bro.switch_to.frame('id')
            动作链(拖动):from selenium.webdriver import ActionChains
                    1.实例化一个动作链对象：action = ActionChains(bro)
                    2.action.click_and_hold(div)  长按且点击操作
                    3.action.move_by_offset(x,y)
                    4.perform()让动作链立即执行
                    5.action.release()释放动作链资源



对url请求后有的的内容是动态加载的，在获得的源码没有，可以通过抓包
可以全体搜索通过ctrl+all找到
'''
from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象(有选择),传入浏览器驱动程序路径
bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
#让浏览器发起请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')
#获取浏览器源码数据,包含了动态加载的数据
page_text = bro.page_source
#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
bro.quit()
