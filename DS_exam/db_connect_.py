import mysql.connector as mc

def connect_to_db():
    try:
        mydb = mc.connect(
        host = '192.168.2.165',
        user = 'admin',
        password = '****',
        database = 'DS_exam')
        print('Connected')
        connection = True
    except mc.Error as e:
        mydb = None
        connection = e

    return (mydb, connection)

# connect_to_db()