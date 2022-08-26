import pytesseract

'''
queue模块是Python内置的标准模块，可以直接通过import queue引用。
在Queue模块中提供了三种同步的、线程安全的队列，分别由三个类Queue，LifoQueue和PriorityQueue表示，
它们的唯一区别是元素取出的顺序不同。并且LifoQueue和PriorityQueue都是Queue的子类

1. Queue（FIFO队列）
Queue类表示一个基本的FIFO（First In First Out）队列，即先进先出。创建方法是Queue.Queue（maxsize=0），其中maxsize是个整数，
指明了队列中能存放的数据个数的上限。以下是一个使用Queue的示例。
将四个数字依次存入Queue队列，再依次取出
'''
from queue import Queue
queue_object=Queue()
for i in range(4):
    queue_object.put(i)
while not queue_object.empty():
    print(queue_object.get())

print('---------')

'''
2. LifoQueue（LIFO队列）
LifoQueue类表示后进先出队列（Last in First Out），与栈类似，都是后进入的元素先出来。
创建方法也很简单，使用Queue.LifoQueue（maxsize=0）即可，
其中maxsize的含义与Queue类相同。以下是一个使用LifoQueue的示例：
'''
from queue import LifoQueue
lifo_queue = LifoQueue()
for i in range(4):
    lifo_queue.put(i)
while not lifo_queue.empty():
    print(lifo_queue.get())
print('------')

'''
3. PriorityQueue（优先级队列）
PriorityQueue类表示优先级队列，按级别顺序取出元素，级别最低的最先取出。
优先级队列中的元素一般采取元组（优先级别，数据）的形式来存储。
创建方法同样是Queue.PriorityQueue（maxsize=0）。
以下是一个使用PriorityQueue的示例：wq  
'''
from queue import PriorityQueue

priority_queue=PriorityQueue()
priority_queue.put((5,'中级别工作'))
priority_queue.put((10,'低级别工作'))
priority_queue.put((1,'重要工作'))
while not priority_queue.empty():
    print('开始工作,',priority_queue.get())


