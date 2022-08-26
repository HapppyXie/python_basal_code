# Athour:Mr Xie
# 开发时间:2021/12/4 10:39
r"""
python -> connection - >ADODB -> DSN联接数据源
Python是没有自带访问windows系统API的库的，需要下载。库的名称叫pywin32

建立数据库连接
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')   #ADODB作为访问数据的COM接口，支持多种数据源，多种语言 创建ADODB接口
DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=C:/MyDB.mdb;'       联接数据源
conn.Open(DSN)

打开记录集
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs_name = 'S'       #表名
rs.Open('[' + rs_name + ']', conn, 1, 3)     ##后面的参数3使得表可以被编辑更新。

ADODB 是 Active Data Objects Data Base 的简称,是所有数据库的共同接口.
       不管后端数据库如何，存取数据库的方式都是一致的
Microsoft.Jet.OLEDB.4.0简称Jet引擎可以访问office 97-2003，
#rs的Open（Source,ActiveConnection,CursorType,LockType,Options)

几个重要的函数和属性
rs.MoveFirst() \ rs.MoveLast() \ rs.MoveNext() \ rs.MovePrevious\ rs.BOF \ rs.EOF  同时为True时说明当前rs中没有记录

操作记录集
rs.AddNew()
rs.Fields.Item(1).Value = 'data'
rs.Update()

AddNew添加新纪录可以避免编码问题，对于文本可以直接将unicode对象赋值给文本字段,
如果利用conn.Execute(insert_sql)或者 rs.Execute(insert_sql)对于insert_sql插入sql字符串，
不能插入unicode对象，需要编码为gbk、gb2312、gb18030、utf8等一系列编码，在一些偏僻中文字符上会出现乱码等一系列不可控问题

accdb(access Database)格式是Microsoft Access 2007软件使用的一种存储格式，
mdb是Microsoft Access 2007以前版本的数据库格式

基本步骤
过时的
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = C:\Users\mike\Desktop\MyDB.mdb;'
conn.Open(DSN)
conn.execute(sql_statement) 常用sql语句
conn.close()


"""
#python -> connection - >ADODB -> DSN联接数据源
import win32com.client
conn = win32com.client.gencache.EnsureDispatch('ADODB.Connection')  #联接ADODB接口
DSN = r'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = C:\Users\mike\Desktop\MyDB.accdb;'  #联接数据库
conn.Open(DSN)

rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs_name = '学生信息表'
rs.Open('['+rs_name+']', conn, 1, 3)
rs.AddNew()
rs.Fields.Item(1).Value = "1001"
rs.Fields.Item(2).Value = "肖战"
rs.Fields.Item(3).Value = "26"
rs.Fields.Item(4).Value = "男"
rs.Update()
rs.Fields.Item(3).Value = '20'
rs.Update()
rs.Close()
rs.Open('['+rs_name+']', conn, 1, 3)
rs.MoveFirst()
while not rs.EOF:
    for i in range(1,rs.Fields.Count):
        print(rs.Fields(i).Value, end=' ')
    print()
    rs.MoveNext()
conn.Close()


