import pandas as pd
from datetime import date, datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from main_window import Ui_MainWindow
from parce_from_youtube import get_info_about_video
from db_connect import connect_to_db
from string_split import string_split


class Music_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.show()

        self.ip = ''
        self.port = ''
        self.database = ''
        self.login = ''
        self.password = ''

        self.pushButton_connect.clicked.connect(self.db_connect_from_add_tab)
        self.pushButton_save.clicked.connect(self.add_row_in_db)
        self.pushButton_clear.clicked.connect(self.clear_add_into_db)
        self.pushButton_find_select.clicked.connect(self.select_from_db)
        self.pushButton_select_clear.clicked.connect(self.clear_select_from_music_where)
        self.pushButton_replace.clicked.connect(self.replace_by)
        self.pushButton_replace_clear.clicked.connect(self.clear_replace_by)
        self.pushButton_send_query.clicked.connect(self.execute_free_query)
        self.pushButton_clear_query.clicked.connect(self.clear_free_query)
        self.pushButton_export.clicked.connect(self.export)

    def db_connect_from_add_tab(self):
        self.ip = self.lineEdit_ip.text() if self.lineEdit_ip.text() else '192.168.2.165'
        self.port = self.lineEdit_port.text() if self.lineEdit_port.text() else '3306'
        self.login = self.lineEdit_login.text() if self.lineEdit_login.text() else 'admin'
        self.password = self.lineEdit_pass.text() if self.lineEdit_pass.text() else ''
        self.database = self.lineEdit_name_of_db.text() if self.lineEdit_name_of_db.text() else 'music'

        self.lineEdit_ip.setText(self.ip)
        self.lineEdit_port.setText(self.port)
        self.lineEdit_login.setText(self.login)
        self.lineEdit_pass.setText(self.password)
        self.lineEdit_name_of_db.setText(self.database)

        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)
        if connection == 'connected':
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
        self.radioButton_sent_replace.setChecked(True)
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

    def add_row_in_db(self):
        self.label_result.setText('')
        self.link = self.lineEdit_link.text()
        self.genre = self.lineEdit_genre.text()
        if self.genre == '':
            self.genre = 'undefined'
        if self.lineEdit_date.text():
            try:
                date_of = datetime.strptime(self.lineEdit_date.text(), '%d%m%Y').date()
                self.radioButton_add_into_sent.setChecked(True)
            except:
                self.label_result.setText('Wrong data format!')
                self.label_result.setStyleSheet('color:red')
                print('Жду исправления даты')
                return False
        else:
            date_of = date(2001, 1, 1)
        if self.radioButton_add_into_sent.isChecked():
            self.whether_sent = 1
        else:
            self.whether_sent = 0

        status, self.description, self.author = get_info_about_video(self.link)
        if status == True:
            pass
        else:
            self.label_result.setText(f'Ошибка парсинга информации о видео \n {self.description}\nДобавлены данные: '
                                      f'description: ошибка парсинга информации'
                                      f'author: ошибка парсинга информации')
            self.label_result.setStyleSheet('color:red')
            self.description = 'Ошибка парсинга информации'
            self.author = 'Ошибка парсинга информации'


        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)

        if connection == 'connected':

            print('Connection is Established')

            if self.author == '' or self.link == '' or self.description == '':
                print('заполнены не все поля')
                self.label_result.setText('Please fill all fields')
                self.label_result.setStyleSheet('color:red')
            else:
                try:
                    mycursor = mydb.cursor()
                    query = f"INSERT INTO music(link, genre, channel_author, description, date_when_send_into_group, whether_sent) VALUES (%s, %s, %s, %s, %s, %s)"
                    value = (self.link, self.genre, self.author, self.description, date_of, self.whether_sent)
                    mycursor.execute(query, value)
                    mydb.commit()
                    print('Информация успешно записана')
                    self.label_result.setText(self.label_result.text() + '\n' + 'Information added successfully')
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

    def select_from_db(self):
        if self.lineEdit_date_select.text() != '':
            try:
                date_of = f"'{datetime.strptime(self.lineEdit_date_select.text(), '%d%m%Y').date()}'"
                print(date_of)
            except:
                self.label_edit_tab_result.setText('Wrong data format!')
                self.label_edit_tab_result.setStyleSheet('color:red')
                print('Жду исправления даты')
                return False
        else:
            date_of = ''
        select_condition = {
            'id': (self.lineEdit_id_select.text() != '', self.lineEdit_id_select.text()),
            'genre': (self.lineEdit_genre_select.text() != '',
                      f"'%{self.lineEdit_genre_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_genre_select.text()}'"),
            'channel_author': (self.lineEdit_author_select.text() != '',
                               f"'%{self.lineEdit_author_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_author_select.text()}'"),
            'link': (self.lineEdit_link_select.text() != '', f"'{self.lineEdit_link_select.text()}'"),
            'description': (self.lineEdit_description_select.text() != '',
                            f"'%{self.lineEdit_description_select.text()}%'" if self.checkBox_like.isChecked() else f"'{self.lineEdit_description_select.text()}'"),
            'date_when_send_into_group': (
                self.lineEdit_date_select.displayText() != '', date_of),
            'whether_sent': (
                self.radioButton_sent_select_2.isChecked() != True,
                1 if self.radioButton_sent_select.isChecked() else 0),
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

        print(self.ip, self.port, self.login, self.password, self.database)

        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)

        if connection == 'connected':
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result = mycursor.fetchall()
                if result:
                    self.tableWidget_select_result.setRowCount(0)
                    for row_number, row_data in enumerate(result):
                        self.tableWidget_select_result.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget_select_result.setItem(row_number, column_number,
                                                                   QTableWidgetItem(str(data)))

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

    def replace_by(self):
        if self.lineEdit_date_replace.text():
            try:
                date_of = f"'{datetime.strptime(self.lineEdit_date_replace.text(), '%d%m%Y').date()}'"
                print(date_of)
            except:
                self.label_edit_tab_result.setText('Wrong data format!')
                self.label_edit_tab_result.setStyleSheet('color:red')
                print('Жду исправления даты')
                return False
        else:
            date_of = ''
        replace_insertion = {
            'id': (self.lineEdit_id_replace.text() != '', self.lineEdit_id_replace.text()),
            'genre': (self.lineEdit_genre_replace.text() != '', f"'{self.lineEdit_genre_replace.text()}'"),
            'channel_author': (self.lineEdit_author_replace.text() != '', f"'{self.lineEdit_author_replace.text()}'"),
            'link': (self.lineEdit_link_replace.text() != '', f"'{self.lineEdit_link_replace.text()}'"),
            'description': (
                self.lineEdit_description_replace.text() != '', f"'{self.lineEdit_description_replace.text()}'"),
            'date_when_send_into_group': (
                self.lineEdit_date_replace.displayText() != '', date_of),
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

        query = f'update music set {",".join(query_list)} where {" and ".join(self.select_list)}'

        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)

        if connection == 'connected':
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                mydb.commit()
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

        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)

        if connection == 'connected':
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
                                self.tableWidget_select_result_2.setItem(row_number, column_number,
                                                                         QTableWidgetItem(str(data)))
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

        else:
            self.label_query_result_2.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_query_result_2.setStyleSheet('color:red')

    def clear_free_query(self):
        self.textEdit.clear()
        self.radioButton_select.setChecked(True)
        self.tableWidget_select_result_2.clear()

    def export(self):
        """
        для периодического бэкапа музыки из БД
        """

        query = f'select * from music'

        path1 = self.lineEdit_path.text() if self.lineEdit_path.text() else 'C:\\Users\\admin\\Desktop\\PYTHON_2022\\python_study_different\\GUI_Good_Morning_Music\\NOT_FOR_GIT\\backup_music'
        path2 = self.lineEdit_path.text() if self.lineEdit_path.text() else '\\\\192.168.2.222\\study\\!my_projects\\!!!backup!!!\\music'
        filename = self.lineEdit_filename.text() if self.lineEdit_filename.text() else f'backup_music_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx'
        mydb, connection = connect_to_db(self.ip, self.port, self.login, self.password, self.database)

        print(mydb)
        print(connection)

        if connection == 'connected':
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result = mycursor.fetchall()
                if result:
                    try:
                        df = pd.DataFrame(result, columns=['id', 'link', 'genre', 'channel_author', 'description',
                                                           'date_when_send_into_group', 'whether_sent',
                                                           'date_when_added_into_table'])
                        df.to_excel(path1+"/"+filename, index=False)
                        df.to_excel(path2 + "/" + filename, index=False)
                        self.label_administration_tab_result.setText('Information was saved successfully')
                        self.label_administration_tab_result.setStyleSheet('color:green')
                    except:
                        self.label_administration_tab_result.setText('Information wasn"t export')
                        self.label_administration_tab_result.setStyleSheet('color:red')
                else:
                    self.label_administration_tab_result.setText('DB is Empty')
                    self.label_administration_tab_result.setStyleSheet('color:red')

            except Exception as exc:
                self.label_administration_tab_result.setText(f'Information wasn"t export \n {string_split(str(exc))}')
                self.label_administration_tab_result.setStyleSheet('color:red')

        else:
            print(connection)
            self.label_administration_tab_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_administration_tab_result.setStyleSheet('color:red')



