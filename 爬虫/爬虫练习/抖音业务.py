# Athour:Mr Xie
# 开发时间:2022/2/25 19:05
'''
http://api.xingguangma.com/index/login/login?username=qfdyhs016&password=952640

'''

from time import sleep
import sys
from selenium import webdriver
import requests
import cv2
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
    }


    # 1.用户登录 获得token
    def getToken():
        url = 'http://api.xingguangma.com/index/login/login?username=qfdyhs016&password=952640'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.12151 SLBChan/25'
        }
        params = {
            'username': 'qfdyhs016',
            'password': '952640'
        }
        page = requests.get(url=url, params=params, headers=headers)
        page.encoding = page.apparent_encoding
        page_dict = page.json()
        # msg1为token
        msg1 = page_dict['msg']
        print(msg1)
        return msg1


    # 2.组装,获取手机号码
    def getPhone(msg1):
        url_phone = 'http://api.xingguangma.com/index/index/getphone?token=' + msg1
        page_phone = requests.get(url=url_phone, headers=headers)
        page_phone.encoding = page_phone.apparent_encoding
        page_p_dict = page_phone.json()
        phone = page_p_dict['msg']
        print(phone)
        return phone



    # .手机输入后，获得短信验证码
    def getCode(token):
        url_code = 'http://api.xingguangma.com/index/index/getmessage?token=' + token
        page_code = requests.get(url=url_code, headers=headers)
        page_code.encoding = page_code.apparent_encoding
        page_c_dict = page_code.json()
        code = page_c_dict['msg']
        print(code)
        return code


    # 异常调用
    # -1.释放号码接口（无短信或其他原因调用该接口，避免超过取号上限。接到短信之后无需调用该接口，系统自动释放，加黑。）
    def getRelease(msg1,phone):
        url_release = 'http://api.xingguangma.com/index/index/getrelease?token=' + msg1 + '&phone=' + phone
        status_release = requests.get(url=url_release, headers=headers)
        status_release.encoding = status_release.apparent_encoding
        page_s_r_dict = status_release.json()
        status_s_r = page_s_r_dict['msg']
        print(status_s_r)
        return status_s_r


    # -2.加黑号码接口（判定该号码无用或其他原因调用该接口，会加到该账号个人加黑库。接到短信之后无需调用该接口，系统自动释放，加黑。）
    #该页面尚不清楚
    def getBlack(msg1,phone):
        url_black = 'http://api.xingguangma.com/index/index/getblack?token=' + msg1 + '&phone=' + phone
        status_black = requests.get(url=url_black, headers=headers)
        status_black.encoding = status_black.apparent_encoding
        page_s_b_dict = status_black.json()
        status_s_b = page_s_b_dict['msg']
        print(status_s_b)
        return status_s_b

        # 获得滑动距离
    def getDistance(bro):
        sleep(1)
        big_ele = bro.find_element_by_xpath('//*[@id="captcha-verify-image"]')
        big_url = big_ele.get_attribute('src')
        small_ele = bro.find_element_by_xpath('//*[@id="captcha_container"]/div/div[2]/img[2]')
        small_url = small_ele.get_attribute('src')
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
            }
        with open('Todaybig.jpg', 'wb') as f1:
            f1.write(requests.get(url=big_url, headers=headers).content)
            f1.close()
        with open('Todaysmall.jpg', 'wb') as f2:
            f2.write(requests.get(url=small_url, headers=headers).content)
            f2.close()
        sleep(1)
        big_gray = cv2.imread('Todaybig.jpg', 0)
        small_gray = cv2.imread('Todaysmall.jpg', 0)
        sleep(1)
        result = cv2.matchTemplate(big_gray, small_gray, cv2.TM_CCORR_NORMED)
        value = cv2.minMaxLoc(result)
        print(value)
        x = value[2][0]
        # 得到图片522*344    实际图片340*212
        x = int(x * 340 / 522)
        py = 13 - int(5 * 340 / 522)
        # 获得移动距离
        return x - py

        # 自动模拟登录，滑块验证  需增加code的自动填入
    def moni(phone):
        try:
            while True:
                #输入密码和滑块验证
                for i in range(5):
                    # 4次错误刷新页面
                    if i == 0:
                        bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
                        bro.get('https://www.douyin.com/')
                        sleep(1)
                        bro.find_element_by_xpath('//*[@id="qdblhsHs"]/button').click()
                        sleep(1)
                        bro.find_element_by_xpath('//*[@id="login-pannel"]/div[3]/div/article/article/div[1]/div[1]/div/article/article/form/div[1]/div/input').send_keys(phone)
                        bro.find_element_by_xpath('//*[@id="login-pannel"]/div[3]/div/article/article/div[1]/div[1]/div/article/article/form/div[2]/div/span').click()
                    elif i == 4:
                        bro.refresh()
                        sleep(1.5)
                        bro.find_element_by_xpath('//*[@id="qdblhsHs"]/button').click()
                        sleep(1)
                        bro.find_element_by_xpath('//*[@id="login-pannel"]/div[3]/div/article/article/div[1]/div[1]/div/article/article/form/div[1]/div/input').send_keys(phone)
                        bro.find_element_by_xpath('//*[@id="login-pannel"]/div[3]/div/article/article/div[1]/div[1]/div/article/article/form/div[2]/div/span').click()

                    x = getDistance(bro)
                    sleep(1)
                    slider = bro.find_element_by_xpath('//*[@id="secsdk-captcha-drag-wrapper"]/div[2]')
                    action = ActionChains(bro)
                    action.click_and_hold(slider)
                    action.pause(0.2)
                    action.move_by_offset(x - 50, 0)
                    action.pause(0.2)
                    action.move_by_offset(20, 0)
                    action.pause(0.2)
                    action.move_by_offset(20, 0)
                    action.pause(0.2)
                    action.move_by_offset(20, 0)
                    action.pause(0.2)
                    action.move_by_offset(-10, 0)
                    action.release()
                    action.perform()
                    sleep(20)

        except Exception as e:
            print(e)

    while True:
        print('--------------------------------------------------------------------------')
        print('请先获得token和phone')
        print('1.获得token；2.获得手机号；3模拟登录，滑块验证,获得和输入短信验证码；4.释放号码接口；5.加黑号码接口；6.退出')
        select = int(input('请输入选项:'))
        global token
        global phone
        if select == 1:
            token = getToken()
        elif select == 2:
            if token == None:
                print('请先获得token')
                continue
            else:
                phone = getPhone(token)
        elif select == 3:
                if phone == None:
                    print('请选获得手机号')
                else:
                    moni(phone)
                    sleep(3)
                    #获得验证码
                    yzm = getCode(phone)
                    print(yzm)

        elif select == 4:
            if token == None:
                print('请先获得token')
            elif phone == None:
                print('请先获得phone')
            else:
                getRelease(token,phone)
        elif select == 5:
            if token == None:
                print('请先获得token')
            elif phone == None:
                print('请先获得phone')
            else:
                getBlack(token,phone)
        elif select == 6:
            break
            sys.exit()

