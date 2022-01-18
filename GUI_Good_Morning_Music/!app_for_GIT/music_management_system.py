# import pandas as pd
from datetime import date
from PyQt6.QtWidgets import QMainWindow
from main_window import Ui_MainWindow
from parce_from_youtube import get_info_about_video
from NOT_FOR_GIT.db_connect import connect_to_db
from string_split import string_split


class Music_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_save.clicked.connect(self.add_row_in_db)

    def add_row_in_db(self):

        self.link = self.lineEdit_link.text()
        self.genre = self.lineEdit_genre.text()
        if self.genre == '':
            self.genre == 'undefined'
        self.date_of = date(2001, 1, 1)
        self.whether_sent = 0
        self.description, self.author = get_info_about_video(self.link)

        mydb, connection = connect_to_db()

        if connection == True:

            print('Connection is Established')

            if self.author == '' or self.link == '' or self.description == '' or self.whether_sent == '':
                print('заполнены не все поля')
                self.label_result.setText('Please fill all fields')
                self.label_result.setStyleSheet('color:red')
            else:
                try:
                    mycursor = mydb.cursor()
                    query = f"INSERT INTO music(link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (%s, %s, %s, %s, %s, %s)"
                    value = (self.link, self.genre, self.author, self.description, self.date_of, self.whether_sent)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print('Информация успешно записана')
                    self.label_result.setText('Information added successfully')
                    self.label_result.setStyleSheet('color:green')
                    self.lineEdit_genre.setText('')
                    self.lineEdit_link.setText('')
                except Exception as e:
                    e = string_split(str(e))
                    print(e)
                    self.label_result.setText('Can\'t add information to DB' + '\n' + e)
                    self.label_result.setStyleSheet('color:red')
        else:
            print(connection)
            self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result.setStyleSheet('color:red')



# df = pd.read_excel('SQL/music_fin.xlsx')
# def add_row_in_db_from_df(row):
#     """
#     для добавления старой музыки из excell в папке SQL
#     """
#     try:
#         # print(row)
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
# for row in df.itertuples():
#     add_row_in_db(row)





