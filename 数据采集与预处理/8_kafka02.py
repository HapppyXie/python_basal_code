# Athour:Mr Xie
# 开发时间:2022/5/12 14:52

from kafka import KafkaConsumer
#编辑消费者
consumer = KafkaConsumer('test',
    bootstrap_servers='localhost:9092',group_id=None,auto_offset_reset='smallest')
for msg in consumer:
    recv = "%s:%d:%d:key=%s value=%s"%(msg.topic,msg.partition,msg.offset,msg.key,msg.value)
    print(recv)

consumer.close()

