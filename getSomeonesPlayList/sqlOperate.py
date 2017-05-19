import pymysql

def connect():
    conn = pymysql.connect(
        host='192.168.1.50', port=3306, user='outsider', password='root', database='musicsinfo', charset='utf8')
    cur = conn.cursor()
    conn.client_flag

    return cur, conn

def closeLinking(cur, conn):
    conn.commit()
    cur.close()
    conn.close()

def query(sqlStr, **params):
    cur, conn = connect()
    cur.execute(sqlStr, params)
    closeLinking(cur, conn)
