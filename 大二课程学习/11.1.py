# Athour:Mr Xie
# 开发时间:2021/12/3 22:01
import sqlite3
conn = sqlite3.connect(r"C:\Users\mike\Desktop\mydata.accdb")
cur = conn.cursor()
cur.execute("create table test(Id integer,Name text)")
cur.execute("insert into test(Id,Name) values('1','张三')")
cur.execute("insert into test(Id,Name) values('2','李四')")
x = cur.execute("select * from test")
x = list(x)
for row in x:
    print(row)
conn.commit()
conn.close()
print('---------------')
conn = sqlite3.connect(r"C:\Users\mike\Desktop\mydata.accdb")
cur = conn.cursor()
cur.execute("update test set Name = '章子怡' where Name = '张三'")
cur.execute("delete from test where Name ='李四'")
conn.commit()
x = cur.execute("select * from test")
x = list(x)
for row in x:
    print(row)
conn.commit()
conn.close()
