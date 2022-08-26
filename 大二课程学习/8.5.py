# Athour:Mr Xie
# 开发时间:2021/11/16 16:20
#5.例子9-7使用标准库json进行数据交换。
import json
x1 = '["123","456","abc","true"]'#创建字符串序列
y1 = json.loads(x1)         #转换为python数据
print(y1)

x2 = [123,456,789,1011]
y2 = json.dumps(x2)
print(y2)

