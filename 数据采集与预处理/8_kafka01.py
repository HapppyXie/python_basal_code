# Athour:Mr Xie
# 开发时间:2022/5/12 14:14
from kafka import KafkaProducer

#编辑生产者
#连接kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')
#发送内容，必须是bytes类型
msg = 'Hello World'.encode('utf-8')
#发送的topic为test
producer.send('test',msg)
producer.close()

'''
启动Zookeeper服务和Kafka服务，然后，先执行producer_test.py，
再执行consumer_test.py，就可以看到屏幕上打印出“Hello World”。
'''


