from datetime import datetime
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
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

        self.pushButton_connect.clicked.connect(self.db_connect)
        self.pushButton_add_to_db_ds_info.clicked.connect(self.add_row_in_ds_info)
        self.pushButton_clear_add_to_ds_info.clicked.connect(self.clear_add_to_ds_info)
        self.pushButton_backup_tables.clicked.connect(self.backup_ds_info)
        self.comboBox_subject_level_1_add_to_ds.activated.connect(self.renew_combo_subject_level_2)

    #     self.pushButton_save.clicked.connect(self.add_row_in_db)
    #     self.pushButton_clear.clicked.connect(self.clear_add_into_db)
    #     self.pushButton_find_select.clicked.connect(self.select_from_db)
    #     self.pushButton_select_clear.clicked.connect(self.clear_select_from_music_where)
    #     self.pushButton_replace.clicked.connect(self.replace_by)
    #     self.pushButton_replace_clear.clicked.connect(self.clear_replace_by)
    #     self.pushButton_send_query.clicked.connect(self.execute_free_query)
    #     self.pushButton_clear_query.clicked.connect(self.clear_free_query)
    #

    def backup_ds_info(self):
        text_result = ''
        mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
                                         self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
        if connection == True:
            for item in [self.checkBox_DS_info_backup_local, self.checkBox_DS_info_backup_NAS,self.checkBox_DS_QA_backup_local, self.checkBox_DS_QA_backup_NAS]:
                if item.isChecked():
                    if item.text()[-4:] == 'INFO':
                        table = 'DS_info'
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

    def renew_combo_subject_level_2(self):
        subject_level_1 = self.comboBox_subject_level_1_add_to_ds.currentText()
        self.comboBox_subject_level_2_add_to_ds.clear()
        query = f'select Subject_level_2 from Subject_level_2 where ' \
                f'subject_level_1_id = (select id from subject_level_1 where subject_level_1 = "{subject_level_1}")'
        print(query)
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        result = mycursor.fetchall()
        result.append(('',))
        if result:
            self.combo2 = sorted(tuple([x[0] for x in result]))
            self.comboBox_subject_level_2_add_to_ds.addItems(self.combo2)
            result_text = 'Combobox Subject_level_2 successfully filled'
        else:
            result_text = 'Subject_Level_2 in DS_info empty'
        self.label_result_add_to_ds_info.setText(result_text)


    def renew_combo_subject_level_1(self, mydb):
        query = 'select distinct Subject_level_1 from Subject_level_1'
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
            self.renew_combo_subject_level_1(mydb)
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
        self.db_connect()

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
            if self.comboBox_subject_level_2_add_to_ds.currentText():
                subject_level_2 = self.comboBox_subject_level_2_add_to_ds.currentText()
            elif self.lineEdit_subject_level_2_ds_info.text() and self.checkBox_subject_level_2_add_ds_info.isChecked():
                subject_level_2 = self.lineEdit_subject_level_2_ds_info.text()
            else:
                print('!!!')
                subject_level_2 = ''
                result += 'поле subject_level_2 не заполнено\n'
            subject_level_3 = self.lineEdit_subject_level_3_ds_info.text()
            source = self.lineEdit_source_ds_info.text()
            notes = self.lineEdit_notes_ds_info.text()
            good_for_question = 1 if self.checkBox_good_for_question_add_to_ds_info.isChecked() else 0

            if subject_level_1 == '' or subject_level_2 == '':
                print('заполнены не все поля')
                self.label_result_add_to_ds_info.setText('Please fill all fields\n' + result)
                self.label_result_add_to_ds_info.setStyleSheet('color:red')
            else:
                try:
                    query_SL1 = f'insert into Subject_level_1 (Subject_level_1) VALUES ("{subject_level_1}")'
                    mycursor = mydb.cursor()
                    mycursor.execute(query_SL1)
                    query_id_SL1 = f'select id from Subject_level_1 where Subject_level_1 = "{subject_level_1}"'
                    mycursor.execute(query_id_SL1)
                    id_SL1 = mycursor.fetchall()[0][0]
                    query_SL2 = f'insert into Subject_level_2 (Subject_level_2, Subject_level_1_id) VALUES' \
                                f'("{subject_level_2}", "{id_SL1}")'
                                # f'where Subject_level_1_id = (select id from Subject_level_1 where Subject_level_1 = "{subject_level_1}")'
                    print(query_SL2)
                    mycursor.execute(query_SL2)
                    print('!!!')
                    query_id_SL2 = f'select id from Subject_level_2 where Subject_level_2 = "{subject_level_2}"'
                    mycursor.execute(query_id_SL2)
                    id_SL2 = mycursor.fetchall()[0][0]
                    mydb.commit()
                    print(id_SL1, id_SL2)

                    query_condition = {
                        'Subject_level_1_id': (id_SL1 != '', f"{id_SL1}"),
                        'Subject_level_2_id': (id_SL2 != '', f"{id_SL2}"),
                        'Subject_level_3': (subject_level_3 != '', f"'{subject_level_3}'"),
                        'Source': (source != '', f"'{source}'"),
                        'Notes': (notes != '', f"'{notes}'"),
                        'for_question': (True, f"'{good_for_question}'")
                        }
                    print(query_condition)
                    mycursor = mydb.cursor()
                    query_list_column_name = []
                    query_list_value = []
                    for key, value in query_condition.items():
                            if value[0] == True:
                                query_list_column_name.append(key)
                                query_list_value.append(value[1])
                    query = f'insert into DS_info ({",".join(query_list_column_name)}) VALUES ({",".join(query_list_value)})'
                    print(query)
                    mycursor.execute(query)
                    mydb.commit()
                    print('Информация успешно записана')
                    self.label_result_add_to_ds_info.setText('Information added successfully')
                    self.label_result_add_to_ds_info.setStyleSheet('color:green')
                    self.comboBox_subject_level_1_add_to_ds.clear()
                    self.comboBox_subject_level_2_add_to_ds.clear()
                    self.renew_combo_subject_level_1(mydb)
                except Exception as e:
                    e = string_split(str(e))
                    print(e)
                    self.label_result_add_to_ds_info.setText('Can\'t add information to DB' + '\n' + e)
                    self.label_result_add_to_ds_info.setStyleSheet('color:red')
        else:
            print(connection)
            self.label_result_add_to_ds_info.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result_add_to_ds_info.setStyleSheet('color:red')
    #
    # def select_from_db(self):
    #     select_condition = {
    #         'id': (self.lineEdit_id_select.text() != '', self.lineEdit_id_select.text()),
    #         'genre': (self.lineEdit_genre_select.text() != '', f"'{self.lineEdit_genre_select.text()}'"),
    #         'channel_author': (self.lineEdit_author_select.text() != '', f"'{self.lineEdit_author_select.text()}'"),
    #         'link': (self.lineEdit_link_select.text() != '', f"'{self.lineEdit_link_select.text()}'"),
    #         'description': (self.lineEdit_description_select.text() != '', f"'{self.lineEdit_description_select.text()}'"),
    #         'date_when_send_into_group': (self.lineEdit_date_select.displayText() != '', f"'{self.lineEdit_date_select.text()}'"),
    #         'whether_sent': (True, 1 if self.radioButton_sent_select.isChecked() else 0),
    #     }
    #     query_list = []
    #     query_list_column_name = []
    #     query_list_value = []
    #     for key, value in select_condition.items():
    #         if value[0] == True:
    #             query_list_column_name.append(key)
    #             query_list_value.append((value[1]))
    #     for item in zip(query_list_column_name, query_list_value):
    #         query_list.append(f'{item[0]} = {item[1]}')
    #     self.select_list = query_list.copy()
    #     query = f'select * from music where {" and ".join(query_list)}'
    #     print(query)
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #     if connection == True:
    #         try:
    #             mycursor = mydb.cursor()
    #             mycursor.execute(query)
    #             result = mycursor.fetchall()
    #             if result:
    #                 self.tableWidget_select_result.setRowCount(0)
    #                 for row_number, row_data in enumerate(result):
    #                     self.tableWidget_select_result.insertRow(row_number)
    #                     for column_number, data in enumerate(row_data):
    #                         self.tableWidget_select_result.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    #
    #                 self.label_edit_tab_result.setText('Information was selected successfully')
    #                 self.label_edit_tab_result.setStyleSheet('color:green')
    #             else:
    #                 self.tableWidget_select_result.setRowCount(0)
    #                 self.label_edit_tab_result.setText('Nothing find')
    #                 self.label_edit_tab_result.setStyleSheet('color:red')
    #         except Exception as e:
    #             e = string_split(str(e))
    #             print(e)
    #             self.label_edit_tab_result.setText('Can\'t select information from DB' + '\n' + e)
    #             self.label_edit_tab_result.setStyleSheet('color:red')
    #     else:
    #         print(connection)
    #         self.label_edit_tab_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
    #         self.label_edit_tab_result.setStyleSheet('color:red')
    # #
    # def replace_by(self):
    #     replace_insertion = {
    #         'id': (self.lineEdit_id_replace.text() != '', self.lineEdit_id_replace.text()),
    #         'genre': (self.lineEdit_genre_replace.text() != '', f"'{self.lineEdit_genre_replace.text()}'"),
    #         'channel_author': (self.lineEdit_author_replace.text() != '', f"'{self.lineEdit_author_replace.text()}'"),
    #         'link': (self.lineEdit_link_replace.text() != '', f"'{self.lineEdit_link_replace.text()}'"),
    #         'description': (self.lineEdit_description_replace.text() != '', f"'{self.lineEdit_description_replace.text()}'"),
    #         'date_when_send_into_group': (self.lineEdit_date_replace.displayText() != '', f"'{self.lineEdit_date_replace.text()}'"),
    #         'whether_sent': (True, 1 if self.radioButton_sent_replace.isChecked() else 0),
    #     }
    #     print(replace_insertion)
    #     query_list = []
    #     query_list_column_name = []
    #     query_list_value = []
    #     for key, value in replace_insertion.items():
    #         if value[0] == True:
    #             query_list_column_name.append(key)
    #             query_list_value.append((value[1]))
    #     for item in zip(query_list_column_name, query_list_value):
    #         query_list.append(f'{item[0]} = {item[1]}')
    #     print(query_list)
    #     print('!')
    #     query = f'update music set {",".join(query_list)} where {" and ".join(self.select_list)}'
    #     print('!!')
    #     print(query)
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #     if connection == True:
    #         try:
    #             mycursor = mydb.cursor()
    #             mycursor.execute(query)
    #             mydb.commit()
    #             print('!!!')
    #             self.label_edit_tab_result.setText('Replaced successfully')
    #             self.label_edit_tab_result.setStyleSheet('color:green')
    #         except Exception as e:
    #             e = string_split(str(e))
    #             print(e)
    #             self.label_edit_tab_result.setText('Can\'t replace information' + '\n' + e)
    #             self.label_edit_tab_result.setStyleSheet('color:red')
    #     else:
    #         print(connection)
    #         self.label_edit_tab_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
    #         self.label_edit_tab_result.setStyleSheet('color:red')
    #
    # def execute_free_query(self):
    #     query = self.textEdit.toPlainText()
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #     if connection == True:
    #         try:
    #             if self.buttonGroup.checkedButton().text() == 'Select':
    #                 mycursor = mydb.cursor()
    #                 mycursor.execute(query)
    #                 result = mycursor.fetchall()
    #                 if result:
    #                     self.tableWidget_select_result_2.setRowCount(0)
    #                     for row_number, row_data in enumerate(result):
    #                         self.tableWidget_select_result_2.insertRow(row_number)
    #                         for column_number, data in enumerate(row_data):
    #                             self.tableWidget_select_result_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    #                             self.label_query_result_2.setText('Information was selected successfully')
    #                             self.label_query_result_2.setStyleSheet('color:green')
    #                 else:
    #                      self.tableWidget_select_result_2.setRowCount(0)
    #                      self.label_query_result_2.setText('Nothing find')
    #                      self.label_query_result_2.setStyleSheet('color:red')
    #             elif self.buttonGroup.checkedButton().text() == 'Update':
    #                 try:
    #                     mycursor = mydb.cursor()
    #                     mycursor.execute(query)
    #                     mydb.commit()
    #                     self.label_query_result_2.setText('Information was updates successfully')
    #                     self.label_query_result_2.setStyleSheet('color:green')
    #                 except:
    #                     self.label_query_result_2.setText('Information was not updated')
    #                     self.label_query_result_2.setStyleSheet('color:red')
    #             elif self.buttonGroup.checkedButton().text() == 'Delete':
    #                 try:
    #                     mycursor = mydb.cursor()
    #                     mycursor.execute(query)
    #                     mydb.commit()
    #                     self.label_query_result_2.setText('Information was deleted successfully')
    #                     self.label_query_result_2.setStyleSheet('color:green')
    #                 except:
    #                     self.label_query_result_2.setText('Information was not deleted')
    #                     self.label_query_result_2.setStyleSheet('color:red')
    #             else:
    #                 try:
    #                     mycursor = mydb.cursor()
    #                     mycursor.execute(query)
    #                     mydb.commit()
    #                     self.label_query_result_2.setText('Information was inserted successfully')
    #                     self.label_query_result_2.setStyleSheet('color:green')
    #                 except:
    #                     self.label_query_result_2.setText('Information was not inserted')
    #                     self.label_query_result_2.setStyleSheet('color:red')
    #         except Exception as e:
    #             e = string_split(str(e))
    #             print(e)
    #             self.label_query_result_2.setText('Can\'t select information from DB' + '\n' + e)
    #             self.label_query_result_2.setStyleSheet('color:red')
    #
    # def clear_free_query(self):
    #     self.textEdit.clear()
    #     self.radioButton_select.setChecked(True)
    #     self.tableWidget_select_result_2.clear()





