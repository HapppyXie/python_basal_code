# Athour:Mr Xie
# 开发时间:2022/5/14 20:37
'''
传输json格式数据
'''
from kafka import KafkaProducer
import json
#连接kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=lambda v : json.dumps(v).encode('utf-8'))

data={'sno':'95001',
      'sname':'John',
      'ssex':'M',
      'sage':'23'
      }

producer.send('json_topic',data)

producer.close()


#kafka.errors.NoBrokersAvailable: NoBrokersAvailable
#生产者构造中加入api_version=()