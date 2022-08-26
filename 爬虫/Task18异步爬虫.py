'''
异步爬虫：
    -多线程，多进程：
       各线程单独执行，不用串行执行；但无法无限制开启多个线程
    -线程池，进程池：
        可以降低系统对线程创建，销毁的频率，降低系统开销；池中线程或进程的数量有限制
'''
import time
from multiprocessing.dummy import Pool

# #单线程
# def get_page(str):
#     print('正在下载',str)
#     time.sleep(2)
#     print('下载完毕',str)
#
# name_list = ['xiaoxie','xiaoke','xiaomi','xiaoliu']
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%d second'%(end_time-start_time))


#
# #多线程
# start_time = time.time()
#
# def get_page(str):
#     print('正在下载',str)
#     time.sleep(2)
#     print('下载完毕',str)
#
# name_list = ['xiaoxie','xiaoke','xiaomi','xiaoliu']
#
# #实例化一个线程池对象
# pool = Pool(4)#4个线程
# #将列表中每一个列表元素传递给get_page进行处理
# pool.map(get_page,name_list)
#
# end_time=time.time()
# print(end_time-start_time)