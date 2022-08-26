# Athour:Mr Xie
# 开发时间:2021/12/26 15:51
'''
JSON通常用于在Web客户端和服务器数据交换，
    即把 字符串类型的数据 转换成 Python基本数据类型
    或者将 Python基本数据类型 转换成 字符串类型。

json.loads(obj) 将字符串序列化成python基本数据类型，注意单引号与双引号
json.dumps(obj) 将python基本类型序列化成字符串

json.load(obj)  读取 文件中的字符串序列 ，化成python基本数据类型
json.dump(obj)  将python的基本数据类型序列化成字符串并写入到文件中
'''

dict_str = '{"k1":"v1","k2":"v2"}'
import json
dict_json = json.loads(dict_str)
print(dict_json)

json_li = [11,22,33,44]
json_str = json.dumps(json_li)
print(json_str)     #输出为字符串，'[11, 22, 33, 44]' 系统解释为[11, 22, 33, 44]