import os
import random
import subprocess
from datetime import datetime
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from main_window import Ui_MainWindow
# from db_connect import connect_to_db
from NOT_FOR_GIT.db_connect_ import connect_to_db
from string_split import string_split


class DS_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.mydb = self.db_connect()
        self.renew_combo_subject_level_1()

        self.pushButton_connect.clicked.connect(self.db_connect)
        self.pushButton_add_to_db_ds_info.clicked.connect(self.add_row_in_ds_info)
        self.pushButton_clear_add_to_ds_info.clicked.connect(self.clear_add_to_ds_info)
        self.pushButton_backup_tables.clicked.connect(self.backup_ds_info)
        self.pushButton_backup_tables_all.clicked.connect(self.backup_ds_info_all)
        self.pushButton_RESTORE.clicked.connect(self.restore_all)
        self.comboBox_subject_level_1_add_to_ds.activated.connect(self.renew_combo_subject_level_2)
        self.pushButton_RESTORE.clicked.connect(self.restore_all)
        self.pushButton_img.clicked.connect(self.load_image)
        self.pushButton_setfile.clicked.connect(self.get_filename_and_format)
        self.pushButton_get_question.clicked.connect(self.select_random_from_db)
        self.pushButton_show_answer.clicked.connect(self.show_answer)


        self.filename_to_db = ''
        self.fileformat_to_db = ''
        self.file = b''

    def restore_all(self):
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
                                         self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())

        for item in [self.lineEdit_restore_SL1, self.lineEdit_restore_SL2, self.lineEdit_restore_DS_info]:
            path = item.text()
            if item.objectName() == 'lineEdit_restore_SL1':
                fpath = f'NOT_FOR_GIT/backup/subject_level_1/{path}'
                table = 'Subject_level_1'
                df = pd.read_excel(fpath, header = None)#names=['asdfs','sdf','sdfs'])
                df.set_axis(['id', 'Subject_level_1'], axis = 'columns', inplace=True)
            elif item.objectName() == 'lineEdit_restore_SL2':
                fpath = f'NOT_FOR_GIT/backup/subject_level_2/{path}'
                table = 'Subject_level_2'
            elif item.objectName() == 'lineEdit_restore_DS_info':
                fpath = f'NOT_FOR_GIT/backup/INFO/{path}'
                table = 'DS_info'
            else:
                fpath = f'NOT_FOR_GIT/backup/QA/{path}'
                table = 'QA'
            # df = pd.read_excel(fpath)
            # print(df)
            for row in df.itertuples():
                print(row)
                try:
                    if table == 'Subject_level_1':
                        query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]}, '{row[2]}')"
                    elif table == 'Subject_level_2':
                        query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},'{row[3]}')"
                    elif table == 'DS_info':
                        query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},{row[3]}," \
                            f"'{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}'," \
                            f" '{row[9]}', '{row[10]}', '{row[11]}', '{row[12]}','{row[13]}')"
                    # else:
                    #     query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},{row[3]}," \
                    #             f"'{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}',{row[9]})"
                    mycursor = mydb.cursor()
                    print(query)
                    mycursor.execute(query)
                    mydb.commit()
                    print('Информация успешно записана')
                except Exception as e:
                    pass
                    print(e)

    def backup_ds_info_all(self):
        text_result = ''
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
                                         self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        checked_list = [self.checkBox_DS_info_backup_local, self.checkBox_DS_info_backup_NAS, \
                        self.checkBox_DS_QA_backup_local, self.checkBox_DS_QA_backup_NAS, \
                        self.checkBox_SL_1_backup_local, self.checkBox_SL_1_backup_NAS, \
                        self.checkBox_SL_2_backup_local, self.checkBox_SL_2_backup_NAS,]
        if connection == True:
            for item in checked_list:
                if item.text()[-4:] == 'INFO':
                    table = 'DS_info'
                elif item.text()[-1] == '1':
                        table = 'Subject_level_1'
                elif item.text()[-1] == '2':
                     table = 'Subject_level_2'
                else:
                     table = 'QA'
                path = f'{item.text()}/backup_{table}_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx'
                try:
                    mycursor = mydb.cursor()
                    mycursor.execute(
                    f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND table_schema = 'DS'")
                    result = mycursor.fetchall()
                    print(result)
                    columns = [x[0] for x in result]
                    mycursor.execute(f"SELECT * from {table}")
                    result = mycursor.fetchall()
                    df = pd.DataFrame(result, columns=columns)
                    df.to_excel(path, index=False)
                    df1 = pd.DataFrame(result)
                    df1.to_excel(path, index=False)
                    text_result += f'- успешный backup {table} в {path}\n'
                except Exception as c:
                    print(c)
                    text_result += f'- Неудачный backup {table} в {path}\n'
            self.label_backup_result.setText(text_result)
            if 'Неудачный' in text_result:
                self.label_backup_result.setStyleSheet('color:red')
            else:
                self.label_backup_result.setStyleSheet('color:green')

    def backup_ds_info(self):
        text_result = ''
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
                                         self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        checked_list = [self.checkBox_DS_info_backup_local, self.checkBox_DS_info_backup_NAS, \
                        self.checkBox_DS_QA_backup_local, self.checkBox_DS_QA_backup_NAS, \
                        self.checkBox_SL_1_backup_local, self.checkBox_SL_1_backup_NAS, \
                        self.checkBox_SL_2_backup_local, self.checkBox_SL_2_backup_NAS,]
        if connection == True:
            for item in checked_list:
                if item.isChecked():
                    if item.text()[-4:] == 'INFO':
                        table = 'DS_info'
                    elif item.text()[-1] == '1':
                        table = 'Subject_level_1'
                    elif item.text()[-1] == '2':
                        table = 'Subject_level_2'
                    else:
                        table = 'QA'
                    path = f'{item.text()}/backup_{table}_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx'
                    try:
                        mycursor = mydb.cursor()
                        mycursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND table_schema = 'DS'")
                        result = mycursor.fetchall()
                        print(result)
                        columns = [x[0] for x in result]
                        mycursor.execute(f"SELECT * from {table}")
                        result = mycursor.fetchall()
                        df = pd.DataFrame(result, columns=columns)
                        df.to_excel(path, index=False)
                        text_result += f'- успешный backup {table} в {path}\n'
                    except Exception as c:
                        print(c)
                        text_result += f'- Неудачный backup {table} в {path}\n'
            self.label_backup_result.setText(text_result)
            if 'Неудачный' in text_result:
                self.label_backup_result.setStyleSheet('color:red')
            else:
                self.label_backup_result.setStyleSheet('color:green')

    def renew_combo_subject_level_2(self):
        mydb = self.db_connect()
        subject_level_1 = self.comboBox_subject_level_1_add_to_ds.currentText()
        self.comboBox_subject_level_2_add_to_ds.clear()
        query = f'select Subject_level_2 from Subject_level_2 where ' \
                f'subject_level_1_id = (select id from subject_level_1 where subject_level_1 = "{subject_level_1}")'
        print(query)
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        print(result)
        result.append(('',))
        print(result)
        if result:
            self.combo2 = sorted(tuple([x[0] for x in result]))
            self.comboBox_subject_level_2_add_to_ds.addItems(self.combo2)
            result_text = 'Combobox Subject_level_2 successfully filled'
        else:
            result_text = 'Subject_Level_2 in DS_info empty'
        self.label_result_add_to_ds_info.setText(result_text)

    def renew_combo_subject_level_1(self):
        mydb = self.db_connect()
        query = 'select Subject_level_1 from Subject_level_1'
        mycursor = mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        result.append(('',))
        if result:
            self.combo1 = sorted(tuple([x[0] for x in result]))
            self.comboBox_subject_level_1_add_to_ds.addItems(self.combo1)
            result_text = 'Combobox Subject_level_1 successfully filled'
        else:
            result_text = 'Subject_Level_1 in DS_info empty'
        self.label_result_add_to_ds_info.setText(result_text)

    def db_connect(self):
        ip = self.lineEdit_ip.text() if self.lineEdit_ip.text() else '192.168.2.165'
        port = self.lineEdit_port.text() if self.lineEdit_port.text() else '3306'
        login = self.lineEdit_login.text() if self.lineEdit_login.text() else 'admin'
        password = self.lineEdit_pass.text() if self.lineEdit_pass.text() else ''
        database = self.lineEdit_name_of_db.text() if self.lineEdit_name_of_db.text() else 'DS'

        self.lineEdit_ip.setText(ip)
        self.lineEdit_port.setText(port)
        self.lineEdit_login.setText(login)
        self.lineEdit_pass.setText(password)
        self.lineEdit_name_of_db.setText(database)

        mydb, connection = connect_to_db(ip, port, login, password, database)
        if connection == True:
            print('Connection is Established')
            self.label_result_connect_to_db.setText('Connected to DB')
            self.label_result_connect_to_db.setStyleSheet('color:green')
            return mydb
        else:
            print(connection)
            self.label_result_connect_to_db.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result_connect_to_db.setStyleSheet('color:red')

    def clear_add_to_ds_info(self):
        self.lineEdit_subject_level_1_ds_info.clear()
        self.lineEdit_subject_level_2_ds_info.clear()
        self.lineEdit_subject_level_3_ds_info.clear()
        self.lineEdit_source_ds_info.clear()
        self.lineEdit_notes_ds_info.clear()
        self.checkBox_subject_level_1_add_ds_info.setChecked(False)
        self.checkBox_subject_level_2_add_ds_info.setChecked(False)
        self.checkBox_good_for_question_add_to_ds_info.setChecked(False)
        self.comboBox_subject_level_1_add_to_ds.clear()
        self.comboBox_subject_level_2_add_to_ds.clear()
        self.checkBox_viewed_add_to_ds_info_3.setChecked(False)
        self.comboBox_rating_add_to_ds_info.setCurrentIndex(0)
        self.checkBox_linktogooglecolab_add_to_ds_info.setChecked(False)
        self.checkBox_fillanswer_add_to_ds_info_2.setChecked(False)
        self.renew_combo_subject_level_1()

    def get_filename_and_format(self):
        path = QFileDialog.getOpenFileName(self, 'Open File', r'C:/', 'All Files (*)')
        filepath_to_db = path[0]
        if path:
            self.filename_to_db, self.fileformat_to_db = path[0].split(r'/')[-1].split('.')
            self.convert_to_binary_data(filepath_to_db)

    def convert_to_binary_data(self, path):
        # Преобразование данных в двоичный формат
        with open(path, 'rb') as file:
            self.file = file.read()

    def show_answer(self):
        file_name_format = '.'.join([self.filename_to_db,self.fileformat_to_db])
        print(file_name_format)
        self.write_to_file(self.file, file_name_format)

    def write_to_file(self, data, filename):
        # Преобразование двоичных данных в нужный формат
        with open(filename, 'wb') as file:
                file.write(data)
        self.open_file(self.fileformat_to_db, filename)

    def open_file(self, format, path):
        if format == 'ipynb':
            exec = rf"jupyter notebook {path}"
            print(exec)
            subprocess.run(exec)
        else:
            os.startfile(rf"{path}", "open")

    def select_random_from_db(self):
        query = """select * from ds_info where for_question = 0 and file is NOT NULL"""
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), 'test_for_blob')
        if connection == True:
            try:
                mycursor = mydb.cursor()
                mycursor.execute(query)
                result = mycursor.fetchall()
                question = random.choice(result)
                if question:
                    for i in question:
                        print(i)
                    self.textBrowser_for_question.setText(f'{str(question[3])}')
                    self.textBrowser_for_question.setText(f'{str(question[4])}')
                    self.filename_to_db = question[5]
                    self.fileformat_to_db = question[6]
                    self.file = question[7]
                else:
                    self.textBrowser_for_question.setText('Nothing find')
                    self.textBrowser_for_question.setStyleSheet('color:red')
            except Exception as e:
                e = string_split(str(e))
                print(e)
                self.textBrowser_for_question.setText('Can\'t select information from DB' + '\n' + e)
                self.textBrowser_for_question.setStyleSheet('color:red')
        else:
            print(connection)
            self.textBrowser_for_question.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.textBrowser_for_question.setStyleSheet('color:red')

    def add_row_in_ds_info(self):
        result = ''
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        if connection == True:
            if self.comboBox_subject_level_1_add_to_ds.currentText():
                subject_level_1 = self.comboBox_subject_level_1_add_to_ds.currentText()
            elif self.lineEdit_subject_level_1_ds_info.text() and self.checkBox_subject_level_1_add_ds_info.isChecked():
                subject_level_1 = self.lineEdit_subject_level_1_ds_info.text()
            else:
                subject_level_1 = ''
                result += 'поле subject_level_1 не заполнено\n'
            print(subject_level_1)
            if self.comboBox_subject_level_2_add_to_ds.currentText():
                subject_level_2 = self.comboBox_subject_level_2_add_to_ds.currentText()
            elif self.lineEdit_subject_level_2_ds_info.text() and self.checkBox_subject_level_2_add_ds_info.isChecked():
                subject_level_2 = self.lineEdit_subject_level_2_ds_info.text()
            else:
                print('!!!')
                subject_level_2 = ''
                result += 'поле subject_level_2 не заполнено\n'
            print(subject_level_2)
            subject_level_3 = self.lineEdit_subject_level_3_ds_info.text()
            if not self.lineEdit_source_ds_info.text() and self.checkBox_linktogooglecolab_add_to_ds_info.isChecked():
                source = 'https://colab.research.google.com/drive/1-f34MB1y6Ytuom1Ja6Wlz7hIetpf7wzs?usp=sharing'
            else:
                source = self.lineEdit_source_ds_info.text().replace('\\', '\\\\')
            if not self.lineEdit_notes_ds_info.text() and self.checkBox_fillanswer_add_to_ds_info_2.isChecked():
                notes = 'заполнить ответ'
            else:
                notes = self.lineEdit_notes_ds_info.text()
            good_for_question = 1 if self.checkBox_good_for_question_add_to_ds_info.isChecked() else 0
            viewed = 1 if self.checkBox_viewed_add_to_ds_info_3.isChecked() else 0
            rating = self.comboBox_rating_add_to_ds_info.currentText()

            if subject_level_1 == '' or subject_level_2 == '':
                print('заполнены не все поля')
                self.label_result_add_to_ds_info.setText('Please fill all fields\n' + result)
                self.label_result_add_to_ds_info.setStyleSheet('color:red')
            else:
                try:
                    mycursor = mydb.cursor()
                    mycursor.execute(f'select id from Subject_level_1 where Subject_level_1 = "{subject_level_1}"')
                    result = mycursor.fetchall()
                    if result:
                        id_SL1 = result[0][0]
                        mycursor = mydb.cursor()
                        mycursor.execute(f'select id from Subject_level_2 where Subject_level_2 = "{subject_level_2}" and Subject_level_1_id = "{id_SL1}"')
                        print(f'select id from Subject_level_2 where Subject_level_2 = "{subject_level_2}" and Subject_level_1_id = "{id_SL1}"')
                        result = mycursor.fetchall()
                        if result:
                            id_SL2 = result[0][0]
                            print(id_SL2)
                        else:
                            query_SL2 = f'insert into Subject_level_2 (Subject_level_2, Subject_level_1_id) VALUES' \
                                    f'("{subject_level_2}", "{id_SL1}")'
                            try:
                                mycursor.execute(query_SL2)
                                query_id_SL2 = f'select id from Subject_level_2 where Subject_level_2 = "{subject_level_2}"'
                                print(query_SL2)
                                mycursor.execute(query_id_SL2)
                                id_SL2 = mycursor.fetchall()[0][0]
                                mydb.commit()
                            except Exception as e:
                                print(e)

                    else:
                        query_SL1 = f'insert into Subject_level_1 (Subject_level_1) VALUES ("{subject_level_1}")'
                        mycursor = mydb.cursor()
                        mycursor.execute(query_SL1)
                        query_id_SL1 = f'select id from Subject_level_1 where Subject_level_1 = "{subject_level_1}"'
                        mycursor.execute(query_id_SL1)
                        id_SL1 = mycursor.fetchall()[0][0]
                        query_SL2 = f'insert into Subject_level_2 (Subject_level_2, Subject_level_1_id) VALUES' \
                                f'("{subject_level_2}", "{id_SL1}")'
                        mycursor.execute(query_SL2)
                        query_id_SL2 = f'select id from Subject_level_2 where Subject_level_2 = "{subject_level_2}"'
                        mycursor.execute(query_id_SL2)
                        id_SL2 = mycursor.fetchall()[0][0]
                        mydb.commit()

                    # query_condition = {
                    #     'Subject_level_1_id': (id_SL1 != '', f"{id_SL1}"),
                    #     'Subject_level_2_id': (id_SL2 != '', f"{id_SL2}"),
                    #     'Subject_level_3': (subject_level_3 != '', f"'{subject_level_3}'"),
                    #     'Source': (source != '', f"'{source}'"),
                    #     'Notes': (notes != '', f"'{notes}'"),
                    #     'for_question': (True, f"'{good_for_question}'"),
                    #     'VIEWED': (True, f"'{viewed}'"),
                    #     'RATING': (True, f"'{rating}'"),
                    #     'filename': (self.filename_to_db != '', f"'{self.filename_to_db}'"),
                    #     'fileformat': (self.fileformat_to_db != '', f"'{self.fileformat_to_db}'"),
                    #     'file': (self.file != '', f"'{self.file}'")
                    #     }

                    query_condition = {
                        'Subject_level_1_id': (id_SL1 != '', f"{id_SL1}"),
                        'Subject_level_2_id': (id_SL2 != '', f"{id_SL2}"),
                        'Subject_level_3': (subject_level_3 != '', f"{subject_level_3}"),
                        'Source': (source != '', f"{source}"),
                        'Notes': (notes != '', f"{notes}"),
                        'for_question': (True, f"{good_for_question}"),
                        'VIEWED': (True, f"{viewed}"),
                        'RATING': (True, f"{rating}"),
                        'filename': (self.filename_to_db != '', f"{self.filename_to_db}"),
                        'fileformat': (self.fileformat_to_db != '', f"{self.fileformat_to_db}"),
                        'file': (self.file != '', f"{self.file}")
                        }
                    query_for_examination_SL3 = f"select Source, Notes from DS_info where " \
                                                f"Source = '{source}' and " \
                                                f"Subject_level_3 = '{subject_level_3}' and " \
                                                f"Subject_level_2_id = '{id_SL2}' and " \
                                                f"Subject_level_1_id = '{id_SL1}'"
                    mycursor = mydb.cursor()
                    print('1')
                    mycursor.execute(query_for_examination_SL3)
                    print('2')
                    result = mycursor.fetchall()
                    print('3')
                    if result:
                        text_before_notes = result[0][1]
                        if text_before_notes:
                            new_text_notes = text_before_notes + '\n' + f"{notes}"
                        else:
                            new_text_notes = f'{notes}'
                        query_condition.update([('Notes', (notes != '', f"{new_text_notes}"))])
                        print(query_condition)
                        mycursor = mydb.cursor()
                        query_list_column_name = []
                        query_list_value = []
                        query_list = []
                        for key, value in query_condition.items():
                            if value[0] == True:
                                query_list_column_name.append(key)
                                query_list_value.append(value[1])
                        for item in zip(query_list_column_name, query_list_value):
                            query_list.append(f'{item[0]} = {item[1]}')
                        query = f'update DS_info set {",".join(query_list)} where ' \
                                f'Subject_level_3 = "{subject_level_3}" ' \
                                f'and Subject_level_2_id = "{id_SL2}" and Subject_level_1_id = "{id_SL1}"'
                        mycursor.execute(query)
                        mydb.commit()
                        print('Информация обновлена')
                        self.label_result_add_to_ds_info.setText('Information updated successfully')
                        self.label_result_add_to_ds_info.setStyleSheet('color:green')
                        self.clear_add_to_ds_info()
                    else:
                        mycursor = mydb.cursor()
                        query_list_column_name = []
                        query_list_value = []
                        for key, value in query_condition.items():
                                if value[0] == True:
                                    query_list_column_name.append(key)
                                    query_list_value.append(value[1])
                        values_str = f'{"%s,"*len(query_list_value)}'[:-1]
                        query = f'insert into DS_info ({",".join(query_list_column_name)}) VALUES ({values_str})'
                        mycursor.execute(query, query_list_value)
                        mydb.commit()
                        print('Информация успешно записана')
                        self.label_result_add_to_ds_info.setText('Information added successfully')
                        self.label_result_add_to_ds_info.setStyleSheet('color:green')
                        self.clear_add_to_ds_info()
                except Exception as e:
                    e = string_split(str(e))
                    print(e)
                    self.label_result_add_to_ds_info.setText('Can\'t add information to DB' + '\n' + e)
                    self.label_result_add_to_ds_info.setStyleSheet('color:red')
        else:
            print(connection)
            self.label_result_add_to_ds_info.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result_add_to_ds_info.setStyleSheet('color:red')

        self.filename_to_db = ''
        self.fileformat_to_db = ''
        self.file = ''




    def load_image(self):
        myPixmap = QPixmap('2.jpg')
        myScaledPixmap = myPixmap.scaled(self.label_img.size())
        self.label_img.setPixmap(myScaledPixmap)





