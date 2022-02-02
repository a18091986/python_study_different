import pandas as pd
import datetime
from datetime import date, datetime

df = pd.read_excel('NOT_FOR_GIT/backup/INFO/backup_DS_info_db_01_02_2022_20_28_14.xlsx') #когда записвыаю из бэкапа
# df = pd.read_excel('SQL/music_fin.xlsx') #когда записываю из music_fin

def add_row_in_db_from_df(row, table, path):
    """
    для добавления информаци в Базу данных из файла excell
    """
    for row in df.itertuples():
        print(row)

    try:
        df = pd.read_excel('NOT_FOR_GIT/backup/INFO/' backup_DS_info_db_01_02_2022_20_28_14.xlsx')
        mycursor = mydb.cursor()
        query = f"INSERT INTO {table}({','.join(df.columns)}) VALUES ({','.join(row)})"
        print(query)
        mycursor.execute(query)
        mydb.commit()
        print('Информация успешно записана')
    except Exception as e:
        # e = string_split(str(e))
        print(e)


