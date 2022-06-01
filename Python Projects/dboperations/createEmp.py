import mysql.connector;

def delete(id):
    conn = mysql.connector.connect(host='192.168.0.187',database='Aftabtestdb',user='root',password='')

    if conn.is_connected():
        print("Connected to mysql db")
        cursor = conn.cursor()

    try:
        cursor.execute("delete from emp where id='%d'")
        conn.commit()
        print("Employee Added")
    except:
        conn.rollback()

    cursor.close()
    conn.close()
