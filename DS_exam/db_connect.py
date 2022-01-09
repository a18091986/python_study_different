import mysql.connector as mc

def connect_to_db():
    try:
        mydb = mc.connect(
        host = '192.168.2.165',
        user = 'admin',
        password = '0gfyfctyr0MYSQL',
        database = 'DS_exam')

        print('Connected')
        return mydb
    except mc.Error as e:
        print(e)

# connect_to_db()