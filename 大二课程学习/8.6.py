# Athour:Mr Xie
# 开发时间:2021/11/16 16:40
#.6.例题9-8 使用csv模块读写文件内容。
import csv
with open(r'C:\Users\mike\Desktop\test.csv','w',newline='') as fp:
        test_writer = csv.writer(fp, delimiter=' ', quotechar='"')
        test_writer.writerow(['red', 'blue', 'green'])
        test_writer.writerow(['test_string'] * 5)
with open(r'C:\Users\mike\Desktop\test.csv','r',newline='') as fp:
    test_reader = csv.reader(fp, delimiter=' ', quotechar='"')
    for row in test_reader:
        print(row)

