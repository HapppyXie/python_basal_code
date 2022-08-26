# Athour:Mr Xie
# 开发时间:2021/12/3 22:30
#2． Python使用ADODB访问ACCESS数据库，读写数据。
import win32com.client
conn = win32com.client.gencache.EnsureDispatch(r'ADODB.Connection')  #联接ADODB接口
DSN = r'PROVIDER = Microsoft.ACE.OLEDB.12.0;DATA SOURCE = C:\Users\mike\Desktop\Database1.accdb;'  #联接数据库
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