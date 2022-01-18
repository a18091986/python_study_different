import pandas as pd
from db_connect import connect_to_db
from datetime import datetime
import math


df = pd.read_excel('SQL/music_fin.xlsx')

# df.to_excel('music_fin.xlsx', index = False)

print(df)

# print(df.itertuples())

print(list(df.itertuples())[1][1])

print(datetime.date(datetime.strptime(list(df.itertuples())[1][1], "%d.%m.%Y")))

# def add_row_in_db(row):
#     try:
#         dateof = datetime.strptime(dateof, '%Y.%m.%d')
#     except:
#         dateof = datefromdatetime(2001,1,1)
#     link = row[2]
#     genre = row[3]
#     author = row[4]
#     description = row[5]
#     was = 1 if row[6] == 'было' else 0
#
#     print(date, link, genre, author, description, was)

    # mydb, connection = connect_to_db()
    #
    # if connection == True:
    #
    #     print('Connection is Established')
    #
    #     if author == '' or link == '' or description == '' or was == '':
    #         print('заполнены не все поля')
    #         # self.label_result.setText('Please add all fields')
    #         # self.label_result.setStyleSheet('color:red')
    #
    #     else:
    #         try:
    #             mycursor = mydb.cursor()
    #             query = f"INSERT INTO music(link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (%s, %s, %s, %s, %s, %s)"
    #             value = (link, genre, author, description, date, was)
    #             mycursor.execute(query, value)
    #             mydb.commit()
    #             print('Информация успешно записана')
    #             # self.label_result.setText('Information added successfully')
    #             # self.label_result.setStyleSheet('color:green')
    #             # self.lineEdit_question_into_db.setText('')
    #         except Exception as e:
    #             # e = string_split(str(e))
    #             print(e)
    #             # self.label_result.setText('Can\'t add information to DB' + '\n' + e)
    #             # self.label_result.setStyleSheet('color:red')
    #
    # else:
    #     print(connection)
    #     # self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
    #     # self.label_result.setStyleSheet('color:red')

# #
# for row in df.itertuples():
#     add_row_in_db(row)
#
#







