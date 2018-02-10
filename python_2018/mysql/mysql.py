import MySQLdb

def main():
    conn = MySQLdb.connect(
        user='root',
        passwd='aaki0092',
        host='localhost',
        db='newdb'
    )
    c = conn.cursor()

    #DB一覧
    sql = 'show databases'
    c.execute(sql)
    print('===== DB一覧 =====')
    l = c.fetchall()
    print (l)

    # テーブル一覧の取得
    sql = 'show tables'
    c.execute(sql)
    print('===== テーブル一覧 =====')
    print(c.fetchone())

    # テーブル内容取得
    sql = 'select * from members'
    c.execute(sql)
    print('===== テーブル一覧 =====')
    print(c.fetchone())

    c.close()
    conn.close()

main()
