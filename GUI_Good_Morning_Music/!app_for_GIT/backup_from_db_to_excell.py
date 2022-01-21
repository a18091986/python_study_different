import pandas as pd
# import datetime
from datetime import date, datetime
from NOT_FOR_GIT.db_connect import connect_to_db
from mysql.connector import connect

def save_into_excel():
    """
    для периодического бэкапа музыки из БД
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

save_into_excel()

#
#         date_of = date(datetime.strptime(row[1], "%d.%m.%Y"))
#     except TypeError:
#         date_of = date(2001, 1, 1)
#
#     link = row[2]
#     genre = row[3]
#     author = row[4]
#     description = row[5]
#     was = 1 if row[6] == 'было' else 0
#
#     # print(date_of, link, genre, author, description, was)
#
#     mydb, connection = connect_to_db()
#
#     if connection == True:
#
#         # print('Connection is Established')
#
#         if author == '' or link == '' or description == '' or was == '':
#             print('заполнены не все поля')
#             # self.label_result.setText('Please add all fields')
#             # self.label_result.setStyleSheet('color:red')
#
#         else:
#             try:
#                 mycursor = mydb.cursor()
#                 query = f"INSERT INTO music(link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (%s, %s, %s, %s, %s, %s)"
#                 value = (link, genre, author, description, date_of, was)
#                 mycursor.execute(query, value)
#                 mydb.commit()
#                 print('Информация успешно записана')
#                 # self.label_result.setText('Information added successfully')
#                 # self.label_result.setStyleSheet('color:green')
#                 # self.lineEdit_question_into_db.setText('')
#             except Exception as e:
#                 # e = string_split(str(e))
#                 print(e)
#                 # self.label_result.setText('Can\'t add information to DB' + '\n' + e)
#                 # self.label_result.setStyleSheet('color:red')
#
#     else:
#         print(connection)
#         # self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
#         # self.label_result.setStyleSheet('color:red')
#
# for row in df.itertuples():
#     add_row_in_db_from_df(row)