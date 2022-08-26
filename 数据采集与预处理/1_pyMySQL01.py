# Athour:Mr Xie
# 开发时间:2022/3/22 17:11
# mysql1.py
import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    host='localhost',  # 主机名
    port=3306,  # 端口号
    user='root',  # 数据库用户名
    passwd='gduf123',  # 密码
    db='school',   # 数据库名称
    charset='utf8'  #编码格式
)


# # 获取游标
# cursor = connect.cursor()
# # 执行SQL查询
# cursor.execute("SELECT VERSION()")
# # 获取单条数据
# version = cursor.fetchone()
# # 打印输出
# print("MySQL数据库版本是：%s" % version)
# # 关闭数据库连接
# connect.close()



# cursor = connect.cursor()
# # 如果表存在，则先删除
# cursor.execute("DROP TABLE IF EXISTS student")
# # 设定SQL语句
# sql = """
# CREATE TABLE student(
#     sno char(5),
#     sname char(10),
#     ssex char(2),
#     sage int);
# """
# # 执行SQL语句
# cursor.execute(sql)
# # 关闭数据库连接
# connect.close()



# # 获取游标
# cursor = connect.cursor()
# # 插入数据
# sql = "INSERT INTO student(sno,sname,ssex,sage) VALUES ('%s', '%s', '%s', %d)"
# data1 = ('95001','王小明','男',21)
# data2 = ('95002','张梅梅','女',20)
# cursor.execute(sql % data1)
# cursor.execute(sql % data2)
# connect.commit()
# print('成功插入数据')
# # 关闭数据库连接
# connect.close()


# # 获取游标
# cursor = connect.cursor()
# # 修改数据
# sql = "UPDATE student SET sage = %d WHERE sno = '%s' "
# data = (19, '95002')
# cursor.execute(sql % data)
# connect.commit()
# print('成功修改数据')
# # 关闭数据库连接
# connect.close()


# # 获取游标
# cursor = connect.cursor()
# # 查询数据
# sql = "SELECT sno,sname,ssex,sage FROM student WHERE sno = '%s' "
# data = ('95001',)    #元组中只有一个元素的时候需要加一个逗号
# cursor.execute(sql % data)
# for row in cursor.fetchall():
#     print("学号:%s\t姓名:%s\t性别:%s\t年龄:%d" % row)
# print('共查找出', cursor.rowcount, '条数据')
# # 关闭数据库连接
# connect.close()



# # 获取游标
# cursor = connect.cursor()
# # 删除数据
# sql = "DELETE FROM student WHERE sno = '%s'"
# data = ('95002',)  #元组中只有一个元素的时候需要加一个逗号
# cursor.execute(sql % data)
# connect.commit()
# print('成功删除', cursor.rowcount, '条数据')
# # 关闭数据库连接
# connect.close()


