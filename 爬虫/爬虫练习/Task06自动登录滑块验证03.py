# Athour:Mr Xie
# 开发时间:2022/2/27 22:29
'''
使用前 1.打开电脑搜索框输入cmd，确保电脑联网，然后在cmd中输入：[pip install selenium]（第三方库）[]内为要输入内容
        同上依次下载下列第三方库: requests
      2.无法下载库，要升级pip时, cmd中输入:[python -m pip install --upgrade pip]，再重新下载
      3.安装Chrome谷歌浏览器驱动引擎

'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import requests
import cv2
from selenium.webdriver import ActionChains

def getDistance(bro):
    # #class可以取，但src取不到，做了隐藏
    # big_url = big_ele.get_attribute('src')
    # 网站做了图片隐蔽，但下面可以找到其原图，滑块图片为其缩小版
    # 得到大原图地址
    big_ele = bro.find_element_by_xpath('//*[@id="cdn1"]')
    big_url = big_ele.get_attribute('src')
    # 得到小原图地址,即滑块
    small_ele = bro.find_element_by_xpath('//*[@id="cdn2"]')
    small_url = small_ele.get_attribute('src')
    # 下载图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
    with open('big.jpg', 'wb') as f1:
        f1.write(requests.get(url=big_url, headers=headers).content)
        f1.close()
    with open('small.jpg', 'wb') as f2:
        f2.write(requests.get(url=small_url, headers=headers).content)
        f2.close()
    # 图片下载后复制到本地磁盘可查看最原始大小，先查看原始大小估计距离，再通过缩放比例计算实际移动距离
    # 使用人工智能匹配大图和小图重叠后x轴的距离 cv2
    big_gray = cv2.imread('big.jpg', 0)  # 表示加载大图片   0以灰度模式加载图片 ,缺块部分为灰色，人才可判断划在哪里
    small_gray = cv2.imread('small.jpg', 0)  # 加载小图
    result = cv2.matchTemplate(big_gray, small_gray, cv2.TM_CCORR_NORMED)  # 匹配对象
    value = cv2.minMaxLoc(result)  # 匹配小图和大图最左边和最右边的结果   就是小图（包含白色边框）从大图最左边到缺口的长度
    # print(value)
    x = value[2][0]
    print(x)
    # (0.5749441981315613, 0.8430253267288208, (472, 103), (472, 14))
    # 小图边缘有大概11的白色像素  472+11(大概)=483
    # 缩放比例以及校准滑块偏移量 原图680*390  实际282*162   比例=实际282/原图680
    x = int(x * 282 / 680)
    # print(x)
    # !!!此处的20，11在不同电脑可以是不同的，需要重新量
    py = 20 - int(6 * 286 / 680)  # 偏移量  大图左边边缘距离滑块左边的距离20（实际）-int(11（原图中的白色边框长度）*286/680)
    x = x - py
    return x

#滑块自动化
def moveSlider(bro,distance):
    # 获得滑块
    slider = bro.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
    # 通过ActionChains滑动解锁
    action = ActionChains(bro)
    action.click_and_hold(slider)
    action.pause(0.2)
    sleep(1)
    action.move_by_offset(distance - 20, 0)
    action.pause(0.2)
    action.move_by_offset(10, 0)
    action.pause(0.2)
    action.move_by_offset(5, 0)
    action.pause(0.2)
    action.move_by_offset(5,0)
    action.release()
    action.perform()
    sleep(3)

def login():
    bro.switch_to.frame(0) # 0代表第一个  ，只要是iframe的参数就可以传
    bro.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    bro.find_element_by_xpath('//*[@id="username"]').send_keys('13428394849')
    sleep(0.5)
    bro.find_element_by_xpath('//*[@id="password"]').send_keys('1234567890')
    sleep(0.5)
    bro.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
    # 获取滑块及滑板的图片地址
    # 加上隐性等待以防超时报错
    sleep(1)
    # 加载后切换frame
    bro.switch_to.frame(bro.find_element(By.XPATH, '//*[@id="tcaptcha_iframe"]'))
    return bro


#此处的executable_path='谷歌浏览器驱动引擎位置'
bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
bro.get('http://www.douban.com/')
sleep(1)


#循环登录三次
for i in range(4):
        bro = login()
        distance = getDistance(bro)
        moveSlider(bro, distance)
        sleep(1.5)
        # title认为豆瓣说明没有登录成功,刷新图片
        if bro.title == '豆瓣':
            bro.refresh()
            sleep(1.5)
        elif bro.title != '豆瓣':
            break;






