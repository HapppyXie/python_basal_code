# Athour:Mr Xie
# 开发时间:2022/5/14 21:05
from kafka import KafkaConsumer
import json
import pymysql

#恢复
def back():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='gduf123',
        db='school',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = 'delete from student_1 where sno = "95001";'
    cursor.execute(sql)
    conn.commit()
    print('恢复成功')



# #编辑消费者
# consumer = KafkaConsumer('json_topic',
#             bootstrap_servers=['localhost:9092'],
#             group_id=None,auto_offset_reset='smallest')

# #消费者返回消费者记录集 使用msg.属性值提取其中属性
# #ConsumerRecord(topic='json_topic', partition=0, offset=0, timestamp=1652537262691, timestamp_type=0, key=None, value=b'{"sno": "95001", "name": "John", "sex": "M", "age": "23"}', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=57, serialized_header_size=-1)
#
# for msg in consumer:
#     print(msg)
#     msg1 = str(msg.value,encoding='utf-8')#将字节转换为字符串
#     dict = json.loads(msg1)#将json对象转化为python基本数据类型
#     print(msg1)
#     #{"sno": "95001", "sname": "John", "sex": "M", "age": "23"}
#     connect=pymysql.Connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='gduf123',
#         db='school',
#         charset='utf8'
#     )
#     cursor = connect.cursor()
#     #插入数据
#     sql = "insert into student_1(sno,sname,ssex,sage) values('{0}','{1}','{2}',{3})".format(dict['sno'],dict['sname'],dict['ssex'],dict['sage'])
#
#     cursor.execute(sql)
#     connect.commit()
#     print('成功插入数据')
#     connect.close()


back()




