import mysql.connector as mc

def connect_to_db(host, port, user, password, database):
    try:
        mydb = mc.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = database)
        print('Connected')
        connection = True
    except mc.Error as e:
        mydb = None
        connection = e
        print(e)

    return (mydb, connection)

# connect_to_db()

