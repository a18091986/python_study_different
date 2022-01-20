# import pandas as pd
from datetime import date
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from main_window import Ui_MainWindow
from parce_from_youtube import get_info_about_video
from db_connect import connect_to_db
from string_split import string_split
# import mysql.connector


class Music_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


        self.pushButton_connect.clicked.connect(self.db_connect)
        self.pushButton_save.clicked.connect(self.add_row_in_db)
        self.pushButton_clear.clicked.connect(self.clear_add_into_db)
        self.pushButton_find_select.clicked.connect(self.select_from_db)
        self.pushButton_select_clear.clicked.connect(self.clear_select_from_music_where)
        self.pushButton_replace.clicked.connect(self.replace_by)
        self.pushButton_replace_clear.clicked.connect(self.clear_replace_by)
        self.pushButton_send_query.clicked.connect(self.execute_free_query)
        self.pushButton_clear_query.clicked.connect(self.clear_free_query)

    def db_connect(self):
        ip = self.lineEdit_ip.text() if self.lineEdit_ip.text() else '192.168.2.165'
        port = self.lineEdit_port.text() if self.lineEdit_port.text() else '3306'
        login = self.lineEdit_login.text() if self.lineEdit_login.text() else 'admin'
        password = self.lineEdit_pass.text() if self.lineEdit_pass.text() else ''
        database = self.lineEdit_name_of_db.text() if self.lineEdit_name_of_db.text() else 'music'

        self.lineEdit_ip.setText(ip)
        self.lineEdit_port.setText(port)
        self.lineEdit_login.setText(login)
        self.lineEdit_pass.setText(password)
        self.lineEdit_name_of_db.setText(database)

        mydb, connection = connect_to_db(ip, port, login, password, database)
        if connection == True:
            print('Connection is Established')
            self.label_result.setText('Connected to DB')
            self.label_result.setStyleSheet('color:green')
        else:
            print(connection)
            self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result.setStyleSheet('color:red')

    def clear_add_into_db(self):
        self.lineEdit_link.clear()
        self.lineEdit_genre.clear()
        self.lineEdit_date.clear()
        self.radioButton_add_into_not_sent.setChecked(True)

    def clear_replace_by(self):
        self.lineEdit_id_replace.clear()
        self.lineEdit_genre_replace.clear()
        self.lineEdit_author_replace.clear()
        self.radioButton_not_sent_replace.setChecked(True)
        self.lineEdit_date_replace.clear()
        self.lineEdit_link_replace.clear()
        self.lineEdit_description_replace.clear()

    def clear_select_from_music_where(self):
        self.lineEdit_id_select.clear()
        self.lineEdit_genre_select.clear()
        self.lineEdit_author_select.clear()
        self.lineEdit_date_select.clear()
        self.lineEdit_link_select.clear()
        self.lineEdit_description_select.clear()
        self.radioButton_sent_select_2.setChecked(True)
        self.checkBox_like.setChecked(True)
    #
    def add_row_in_db(self):

        self.link = self.lineEdit_link.text()
        self.genre = self.lineEdit_genre.text()
        if self.genre == '':
            self.genre = 'undefined'
        self.date_of = date(2001, 1, 1)
        if self.radioButton_add_into_sent.isChecked():
            self.whether_sent = 1
        else:
            self.whether_sent = 0

        self.description, self.author = get_info_about_video(self.link)

        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())

        if connection == True:

            print('Connection is Established')

            if self.author == '' or self.link == '' or self.description == '':
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
    #
    def select_from_db(self):
        select_condition = {
            'id': (self.lineEdit_id_select.text() != '', self.lineEdit_id_select.text()),
            'genre': (self.lineEdit_genre_select.text() != '', f"'%{self.lineEdit_genre_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_genre_select.text()}'"),
            'channel_author': (self.lineEdit_author_select.text() != '', f"'%{self.lineEdit_author_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_author_select.text()}'"),
            'link': (self.lineEdit_link_select.text() != '', f"'{self.lineEdit_link_select.text()}'"),
            'description': (self.lineEdit_description_select.text() != '', f"'%{self.lineEdit_description_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_description_select.text()}'"),
            'date_when_send_into_group': (self.lineEdit_date_select.displayText() != '', f"'{self.lineEdit_date_select.text()}'"),
            'whether_sent': (self.radioButton_sent_select_2.isChecked() != True, 1 if self.radioButton_sent_select.isChecked() else 0),
        }
        query_list = []
        query_list_column_name = []
        query_list_value = []
        for key, value in select_condition.items():
            if value[0] == True:
                query_list_column_name.append(key)
                query_list_value.append((value[1]))
        for item in zip(query_list_column_name, query_list_value):
            if self.checkBox_like.isChecked():
                query_list.append(f'{item[0]} like {item[1]}')
            else:
                query_list.append(f'{item[0]} = {item[1]}')
        self.select_list = query_list.copy()
        query = f'select * from music where {" and ".join(query_list)}'
        print(query)
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        if connection == True:
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result = mycursor.fetchall()
                if result:
                    self.tableWidget_select_result.setRowCount(0)
                    for row_number, row_data in enumerate(result):
                        self.tableWidget_select_result.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget_select_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))

                    self.label_edit_tab_result.setText('Information was selected successfully')
                    self.label_edit_tab_result.setStyleSheet('color:green')
                else:
                    self.tableWidget_select_result.setRowCount(0)
                    self.label_edit_tab_result.setText('Nothing find')
                    self.label_edit_tab_result.setStyleSheet('color:red')
            except Exception as e:
                e = string_split(str(e))
                print(e)
                self.label_edit_tab_result.setText('Can\'t select information from DB' + '\n' + e)
                self.label_edit_tab_result.setStyleSheet('color:red')
        else:
            print(connection)
            self.label_edit_tab_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_edit_tab_result.setStyleSheet('color:red')
    #
    def replace_by(self):
        replace_insertion = {
            'id': (self.lineEdit_id_replace.text() != '', self.lineEdit_id_replace.text()),
            'genre': (self.lineEdit_genre_replace.text() != '', f"'{self.lineEdit_genre_replace.text()}'"),
            'channel_author': (self.lineEdit_author_replace.text() != '', f"'{self.lineEdit_author_replace.text()}'"),
            'link': (self.lineEdit_link_replace.text() != '', f"'{self.lineEdit_link_replace.text()}'"),
            'description': (self.lineEdit_description_replace.text() != '', f"'{self.lineEdit_description_replace.text()}'"),
            'date_when_send_into_group': (self.lineEdit_date_replace.displayText() != '', f"'{self.lineEdit_date_replace.text()}'"),
            'whether_sent': (True, 1 if self.radioButton_sent_replace.isChecked() else 0),
        }
        print(replace_insertion)
        query_list = []
        query_list_column_name = []
        query_list_value = []
        for key, value in replace_insertion.items():
            if value[0] == True:
                query_list_column_name.append(key)
                query_list_value.append((value[1]))
        for item in zip(query_list_column_name, query_list_value):
            query_list.append(f'{item[0]} = {item[1]}')
        print(query_list)
        print('!')
        query = f'update music set {",".join(query_list)} where {" and ".join(self.select_list)}'
        print('!!')
        print(query)
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        if connection == True:
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                mydb.commit()
                print('!!!')
                self.label_edit_tab_result.setText('Replaced successfully')
                self.label_edit_tab_result.setStyleSheet('color:green')
            except Exception as e:
                e = string_split(str(e))
                print(e)
                self.label_edit_tab_result.setText('Can\'t replace information' + '\n' + e)
                self.label_edit_tab_result.setStyleSheet('color:red')
        else:
            print(connection)
            self.label_edit_tab_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_edit_tab_result.setStyleSheet('color:red')

    def execute_free_query(self):
        query = self.textEdit.toPlainText()
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        if connection == True:
            try:
                if self.buttonGroup.checkedButton().text() == 'Select':
                    mycursor = mydb.cursor()
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    if result:
                        self.tableWidget_select_result_2.setRowCount(0)
                        for row_number, row_data in enumerate(result):
                            self.tableWidget_select_result_2.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget_select_result_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                                self.label_query_result_2.setText('Information was selected successfully')
                                self.label_query_result_2.setStyleSheet('color:green')
                    else:
                         self.tableWidget_select_result_2.setRowCount(0)
                         self.label_query_result_2.setText('Nothing find')
                         self.label_query_result_2.setStyleSheet('color:red')
                elif self.buttonGroup.checkedButton().text() == 'Update':
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute(query)
                        mydb.commit()
                        self.label_query_result_2.setText('Information was updates successfully')
                        self.label_query_result_2.setStyleSheet('color:green')
                    except:
                        self.label_query_result_2.setText('Information was not updated')
                        self.label_query_result_2.setStyleSheet('color:red')
                elif self.buttonGroup.checkedButton().text() == 'Delete':
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute(query)
                        mydb.commit()
                        self.label_query_result_2.setText('Information was deleted successfully')
                        self.label_query_result_2.setStyleSheet('color:green')
                    except:
                        self.label_query_result_2.setText('Information was not deleted')
                        self.label_query_result_2.setStyleSheet('color:red')
                else:
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute(query)
                        mydb.commit()
                        self.label_query_result_2.setText('Information was inserted successfully')
                        self.label_query_result_2.setStyleSheet('color:green')
                    except:
                        self.label_query_result_2.setText('Information was not inserted')
                        self.label_query_result_2.setStyleSheet('color:red')
            except Exception as e:
                e = string_split(str(e))
                print(e)
                self.label_query_result_2.setText('Can\'t select information from DB' + '\n' + e)
                self.label_query_result_2.setStyleSheet('color:red')

    def clear_free_query(self):
        self.textEdit.clear()
        self.radioButton_select.setChecked(True)
        self.tableWidget_select_result_2.clear()





