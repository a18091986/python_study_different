import mysql.connector as mc

def connect_to_db():
    try:
        mydb = mc.connect(
        host = '192.168.2.165',
        user = 'admin',
        password = '0gfyfctyr0MYSQL',
        database = 'music')
        print('Connected')
        connection = True
    except mc.Error as e:
        mydb = None
        connection = e
        print(e)

    return (mydb, connection)

connect_to_db()