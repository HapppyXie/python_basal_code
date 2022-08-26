# Athour:Mr Xie
# 开发时间:2021/12/3 19:39
'''
SQLite数据库已内嵌在Python中，使用时需要导入sqlite3
一个数据库就是一个文件
常用的SQLite可视化管理工具，www.sqlabs.com==>SQLiteManager关系形数据库

SQL语言，所有关系数据库语言
'''
'''
成功创建Connection对象以后，再创建一个Cursor对象，
并且调用Cursor对象的execute()方法来执行SQL语句创建数据表以及查询、插入、修改或删除数据库中的数据

connection = sqlite3.connect(r'数据库文件路径和名称') 创建数据库对象，即联接数据库
cur = connection.cursor() 获取游标-临时存储空间，返回结果


'''
'''
Connection对象 conn
conn.execute(sql语句[, parameters])  执行一条SQL语句
conn.executemany(sql[, parameters])  执行多条SQL语句
     cursor()       返回连接的游标，相当于一个临时操做台
    commit()        提交当前事务，如果不提交的话，那么自上次调用commit()方法之后的所有修改都不会真正保存到数据库中
    rollback()      撤销当前事务，将数据库恢复至上次调用commit()方法后的状态
    close()         关闭数据库连接
    create_function(name, num_params, func)         
创建可在SQL语句中调用的函数，其中name为函数名，num_params表示该函数可以接收的参数个数，func表示Python可调用对象

常用SQL语句
创建 creat table s(表格名)(sno text,xingm text)

增加 insert into s(sno,xingm) values('3','zzzz') 可不写前面的形式参数名，但后面的实际参数要对应前面的形参
删除 delet from s where xingbie = 'nan'
改 update s set lie(形参) = 'isi' where sno ='5'
查询 selet * from s 
'''
import sqlite3
conn = sqlite3.connect(r'C:\Users\mike\Desktop\example.db')
cur = conn.cursor()                 #数据名 数据类型
cur.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')  # 创建表
cur.execute("insert into stocks('date','trans','symbol',qty,price) values ('2006-01-05','BUY', 'RHAT', 100, 35.14)")
cur.execute("insert into stocks values ('2001-01-05','BddY', 'RhhAT', 99, 135.14)")
c = cur.execute("select * from stocks")
print(c)
print(list(c))
#结合遍历查询，按价格排序
for row in cur.execute("select * from stocks order by price"):
    print(row)
conn.commit()
conn.close()

from sqlite3 import connect
con = connect(r"C:\Users\mike\Desktop\test.db")
cur = con.cursor()
cur.execute("create table star(id integer,name text,age integer,address text)")
rows =[(1,'王俊凯',16,'重庆'),(2,'王源',15,'重庆'),(3,'易祥千玺',15,'怀化')]
for item in rows:
    cur.execute("insert into star (id,name,age,address) values (?,?,?,?)",item) # ?代表参数，<-item传递
cur.execute("select * from star")
for row in cur:
    print(row)
print('--------------------')
# 此处?代表参数
cur.execute('update star set age = ? where id = ?',(16,3))
cur.execute('select*from star')
for row in cur:
    print(row)
con.commit()
con.close()
