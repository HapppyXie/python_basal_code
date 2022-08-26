# Athour:Mr Xie
# 开发时间:2022/5/3 11:22
from bs4 import BeautifulSoup
import pymysql.cursors

def get_html(path):
    htmlfile = open(path,'r',encoding='gbk')
    html = htmlfile.read()
    htmlfile.close()
    return html

def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    all_tr = soup.find_all('tr')[1:]
    all_tr_list = []
    info_list =[]
    for i in range(len(all_tr)):
        all_tr_list.append(all_tr[i])
    for element in all_tr_list:
        all_td = element.find_all('td')
        all_td_list = []
        for j in range(len(all_td)):
            all_td_list.append(all_td[j].string)
        info_list.append(all_td_list)
    return info_list

def save_mysql(info_list):
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        password='gduf123',
        db='webdb',
        charset='utf8'
    )
    cursor = connect.cursor()

    #插入数据
    for item in info_list:
        id=int(item[0])
        keyword=item[1]
        number=int(item[2])
        sql = "insert into search_index (id,keyword,number) values('%d','%s','%d')"
        data = (id,keyword,number)
        cursor.execute(sql % data)
        connect.commit()
        connect.close()
    print('成功插入数据')

def back():
    conn = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='gduf123',
        db='webdb',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = 'delete from search_index;'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('返回成功')

if __name__ == '__main__':
    path = 'web_demo.html'
    html = get_html(path)
    info_list = parse_html(html)
    save_mysql(info_list)


    #back()