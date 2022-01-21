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
        connection = 'connected'
    except mc.Error as e:
        mydb = None
        connection = f'Ошибка соединения с базой данных! \n {e}'
        print(connection)

    return (mydb, connection)

# connect_to_db()

