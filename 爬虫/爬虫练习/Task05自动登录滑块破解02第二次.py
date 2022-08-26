# Athour:Mr Xie
# 开发时间:2022/3/1 13:19
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from PIL import Image
import cv2
from selenium.webdriver import ActionChains


bro = webdriver.Chrome(executable_path='D:\谷歌浏览器\谷歌驱动程序\chromedriver_win32\chromedriver.exe')
bro.get('https://www.cods.org.cn/')
sleep(2)
bro.find_element_by_id('checkContent_index').send_keys('猫猫')
sleep(1)
btn = WebDriverWait(bro,10).until(ec.presence_of_element_located((By.ID,'checkBtn')))
bro.execute_script("arguments[0].click()",btn)
sleep(1)
bro.refresh()
sleep(1)

#实际图片260*160(实际滑动的距离)   获得实际图片320*197(电脑和手动的截图获取的距离)  滑块大小51*49
img = WebDriverWait(bro,10).until(ec.presence_of_element_located((By.CLASS_NAME,'geetest_canvas_img')))
location = img.location
size = img.size
left,top,right,buttom = location['x']+97,location['y']+52,location['x']+size['width']+155,location['y']+size['height']+88
bro.get_screenshot_as_file('full.png')
img = Image.open('full.png')
img = img.crop((left,top,right,buttom)) #xmin ymin xmax ymax
img.save('big.png')
sleep(1)

big_gray = cv2.imread('big.png',0)#表示加载大图片   0以灰度模式加载图片 ,缺块部分为灰色，人才可判断划在哪里
small_gray = cv2.imread('small.png',0)#加载小图
sleep(1)
result = cv2.matchTemplate(big_gray,small_gray,cv2.TM_CCORR_NORMED) #匹配对象
value = cv2.minMaxLoc(result)  #匹配小图和大图最左边和最右边的结果   就是小图（包含白色边框）从大图最左边到缺口的长
print(value)
#value中有两个元组数，value[2][0] value[3][0]
x = value[2][0]#方块自身的长度
x = int(x*260/320)
#大图左边距离小图的距离
py = 9
x = x - py
print('转换后的距离:',x)


sleep(2)
slider=bro.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
action = ActionChains(bro)
action.click_and_hold(slider)
action.pause(0.2)
action.move_by_offset(x+5,0)
action.pause(0.2)
action.move_by_offset(-10,0)
action.pause(0.2)
action.move_by_offset(5,0)
action.pause(0.2)
action.release()
action.perform()
sleep(3)
#bro.quit()
