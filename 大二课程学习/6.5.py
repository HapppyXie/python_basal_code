# Athour:Mr Xie
# 开发时间:2021/11/5 16:21
#5 编写文本进度条,单行动态刷新（注意：IDLE屏蔽了\r功能）
import time
for i in range(101):
    print('\r{:3}%'.format(i),end='')
    time.sleep(0.1)
