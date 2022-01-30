import pandas as pd
from datetime import date, datetime
from NOT_FOR_GIT.db_connect import connect_to_db
from mysql.connector import connect

def save_into_excel():
    """
    для выгрузки информации из БД в файл txt
    """
    try:
        mydb = connect_to_db()[0]
        mycursor = mydb.cursor()
        mycursor.execute('select * from music')
        result = mycursor.fetchall()
        df = pd.DataFrame(result, columns=['id', 'link', 'genre', 'channel_author', 'description', 'date_when_send_into_group', 'whether_sent', 'date_when_added_into_table'])
        df.to_excel(f'SQL/backup_music_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx', index=False)
    except Exception as c:
        print(c)

# save_into_excel()
