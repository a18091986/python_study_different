from NOT_FOR_GIT.db_connect_ import connect_to_db

def insert_into_db(message):
    try:
        mydb = connect_to_db()
        cursor = mydb.cursor()
        cursor.execute(f'insert into Question (question) VALUE ("{message.text.split(" Отправить в БД?")[0]}")')
        mydb.commit()
        return True
    except:
        return False

