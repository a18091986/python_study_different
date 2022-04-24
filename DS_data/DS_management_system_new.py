import os
import random
import shutil
import subprocess
import time
from datetime import datetime
import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QLabel, QHBoxLayout, QFileDialog, QMessageBox
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from main_window_new import Ui_MainWindow
# from db_connect import connect_to_db
from NOT_FOR_GIT.db_connect_new import Base, engine, TopLevelSubject, MiddleLevelSubject, LowLevelSubject, Answer
from sqlalchemy.orm import sessionmaker
from string_split import string_split
import winshell
from work_with_files import File

WHITE = '\033[00m'
GREEN = '\033[32m'
RED =   '\033[31m'

class DS_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.question = None



        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        self.session = session_maker()


        try: #TODO перенести в work_with_files
            shutil.rmtree('\\'.join([winshell.desktop(), 'temp_dir_for_ds']))
        except Exception as e:
            print(e)
        try:
            os.mkdir('\\'.join([winshell.desktop(), 'temp_dir_for_ds']))
        except Exception as e:
            pass

        # self.session.query(Answer).filter(Answer.answer == '222').delete()
        # self.session.commit()
        # self.session.query(LowLevelSubject).filter(LowLevelSubject.subject == '222').delete()
        # self.session.commit()
        # self.session.query(MiddleLevelSubject).filter(MiddleLevelSubject.subject == '111').delete()
        # self.session.commit()
        # self.session.query(TopLevelSubject).filter(TopLevelSubject.subject == '111').delete()
        # self.session.commit()

        self.renew_combo_top_level_subject()
        self.comboBox_subject_level_1_add_to_ds.activated.connect(self.renew_combo_middle_level_subject)
        self.pushButton_add_to_db_ds_info.clicked.connect(self.add_row_in_ds_and_clear)
        self.pushButton_clear_add_to_ds_info.clicked.connect(self.clear_add_to_ds_info)
        self.pushButton_setfile.clicked.connect(self.file_in_db)
        self.pushButton_get_question.clicked.connect(self.select_random_question)
        self.pushButton_show_answer.clicked.connect(self.show_answer)

    def renew_combo_top_level_subject(self):
        top_level_subject_1 = self.session.query(TopLevelSubject.subject).order_by(TopLevelSubject.subject).all()
        top_level_subject_1 = [subject[0] for subject in top_level_subject_1]
        self.comboBox_subject_level_1_add_to_ds.addItems(top_level_subject_1)

    def renew_combo_middle_level_subject(self):
        self.comboBox_subject_level_2_add_to_ds.clear()
        top_level_subject_id = self.session.query(TopLevelSubject).filter_by(
                               subject = self.comboBox_subject_level_1_add_to_ds.currentText()).one()
        middle_level_subject_2 = self.session.query(MiddleLevelSubject.subject).filter_by(tls_id = top_level_subject_id.id).all()
        self.comboBox_subject_level_2_add_to_ds.addItems([subject[0] for subject in middle_level_subject_2])

    def add_row_in_ds_and_clear(self):
        is_question = 1 if self.checkBox_good_for_question_add_to_ds_info.isChecked() else 0
        rating = int(self.comboBox_rating_add_to_ds_info.currentText())
        filename = self.ready_to_send_file_name
        fileextension = self.ready_to_send_file_format
        file = self.ready_to_send_file_binary
        notes = self.lineEdit_notes_ds_info.text()

        if self.checkBox_subject_level_1_add_ds_info.isChecked(): #если добавляем тему верхнего уровня, то остальных тоже нет

            tls = TopLevelSubject(subject = self.lineEdit_subject_level_1_ds_info.text())
            mls = MiddleLevelSubject(subject = self.lineEdit_subject_level_2_ds_info.text())
            lls = LowLevelSubject(subject = self.lineEdit_subject_level_3_ds_info.text(), rating = rating, is_question = is_question)
            mls.lls = [lls]
            tls.mls = [mls]
            if self.checkBox_good_for_question_add_to_ds_info.isChecked():
                answer = Answer(answer = notes,
                               file_name = filename, file_extension = fileextension, file = file)
                lls.answer = answer
                try:
                    self.session.add(lls)
                    self.session.add(answer)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*"*100}\n{e}\n{"*"*100}{WHITE}')
            else:
                lls.notes = notes
                lls.file_name = filename
                lls.file_extension = fileextension
                lls.file = file
                try:
                    self.session.add(lls)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*" * 100}\n{e}\n{"*" * 100}{WHITE}')

        elif self.checkBox_subject_level_2_add_ds_info.isChecked():  # если добавляем тему среднего уровня

            tls_id = self.session.query(TopLevelSubject).filter_by(subject = self.comboBox_subject_level_1_add_to_ds.currentText()).one().id
            mls = MiddleLevelSubject(subject=self.lineEdit_subject_level_2_ds_info.text(), tls_id = tls_id)
            lls = LowLevelSubject(subject=self.lineEdit_subject_level_3_ds_info.text(), rating=rating,
                                  is_question=is_question)
            mls.lls = [lls]

            if self.checkBox_good_for_question_add_to_ds_info.isChecked():
                answer = Answer(answer=notes,
                                file_name=filename, file_extension=fileextension, file=file)
                lls.answer = answer
                try:
                    self.session.add(lls)
                    self.session.add(answer)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*" * 100}\n{e}\n{"*" * 100}{WHITE}')
            else:
                lls.notes = notes
                lls.file_name = filename
                lls.file_extension = fileextension
                lls.file = file
                try:
                    self.session.add(lls)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*" * 100}\n{e}\n{"*" * 100}{WHITE}')

        else:  # если добавляем только нижний уровень

            mls = self.session.query(MiddleLevelSubject).filter_by(subject=self.comboBox_subject_level_2_add_to_ds.currentText()).one().id
            lls = LowLevelSubject(subject=self.lineEdit_subject_level_3_ds_info.text(), rating=rating,
                                  is_question=is_question, mls_id = mls)

            if self.checkBox_good_for_question_add_to_ds_info.isChecked(): #TODO эти ифы можно попробовать переписать функцией
                answer = Answer(answer=notes,
                                file_name=filename, file_extension=fileextension, file=file)
                lls.answer = answer
                try:
                    self.session.add(lls)
                    self.session.add(answer)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*" * 100}\n{e}\n{"*" * 100}{WHITE}')
            else:
                lls.notes = notes
                lls.file_name = filename
                lls.file_extension = fileextension
                lls.file = file
                try:#TODO заменить на общий try-except для всей функции
                    self.session.add(lls)
                    self.session.commit()
                except Exception as e:
                    print(f'{RED}{"*" * 100}\n{e}\n{"*" * 100}{WHITE}')
        self.clear_add_to_ds_info()





        # self.pushButton_connect.clicked.connect(self.db_connect)

        #
        # self.pushButton_backup_tables.clicked.connect(self.backup_ds_info)
        # self.pushButton_backup_tables_all.clicked.connect(self.backup_ds_info_all)
        # self.pushButton_RESTORE.clicked.connect(self.restore_all)
        # self.comboBox_subject_level_1_add_to_ds.activated.connect(self.renew_combo_subject_level_2)
        # self.pushButton_RESTORE.clicked.connect(self.restore_all)
        # self.pushButton_img.clicked.connect(self.load_image)
        # self.pushButton_setfile.clicked.connect(self.get_filename_and_format)
        # self.pushButton_get_question.clicked.connect(self.select_random_from_db)
        # self.pushButton_show_answer.clicked.connect(self.show_answer)
        #
        #
        # self.desktop = winshell.desktop()
        # self.tempdir = r'C:\TempForDS'
        # self.filename_to_db = ''
        # self.fileformat_to_db = ''
        # self.file = ''

    def clear_add_to_ds_info(self):
        self.lineEdit_subject_level_1_ds_info.clear()
        self.lineEdit_subject_level_2_ds_info.clear()
        self.lineEdit_subject_level_3_ds_info.clear()
        self.lineEdit_notes_ds_info.clear()
        self.checkBox_subject_level_1_add_ds_info.setChecked(False)
        self.checkBox_subject_level_2_add_ds_info.setChecked(False)
        self.checkBox_good_for_question_add_to_ds_info.setChecked(False)
        self.comboBox_subject_level_1_add_to_ds.clear()
        self.comboBox_subject_level_2_add_to_ds.clear()
        self.comboBox_rating_add_to_ds_info.setCurrentIndex(0)
        self.renew_combo_top_level_subject()

    def file_in_db(self):
        file = File()
        file.get_filename_and_format()
        self.ready_to_send_file_name = file.filename_to_db
        self.ready_to_send_file_format = file.fileformat_to_db
        self.ready_to_send_file_binary = file.binary

    def select_random_question(self):#TODO ввести систему учета рейтинга
        self.question = random.choice(self.session.query(LowLevelSubject).filter_by(is_question = 1).all())
        self.textBrowser_for_question.setText('\n'.join([self.question.subject, self.question.notes]))
        print('Тут пока ок')
        # print(question.answer.file)
        if self.question.answer.file:
            print('Тут файл есть')
            self.is_answer_file = 1
            self.view_answer = File()
        else:
            self.is_answer_file = 0
            self.view_answer = str()
            print('Тут файла нет')

    def show_answer(self):
        if self.question:
            if self.is_answer_file == 0:
                self.textBrowser_for_question.setText(self.question.answer.notes)
            else:
                File.show_answer(self.question.answer.file_name, self.question.answer.file_extension, self.question.answer.file)
                self.textBrowser_for_question.setText('\n'.join(['Есть файл с ответом', self.question.answer.answer, self.question.answer.notes]))
        else:
            self.textBrowser_for_question.setText('Сначала выберите вопрос')






#############################################

    # def restore_all(self):
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
    #                                      self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #
    #     for item in [self.lineEdit_restore_SL1, self.lineEdit_restore_SL2, self.lineEdit_restore_DS_info]:
    #         path = item.text()
    #         if item.objectName() == 'lineEdit_restore_SL1':
    #             fpath = f'NOT_FOR_GIT/backup/subject_level_1/{path}'
    #             table = 'Subject_level_1'
    #             df = pd.read_excel(fpath, header = None)#names=['asdfs','sdf','sdfs'])
    #             df.set_axis(['id', 'Subject_level_1'], axis = 'columns', inplace=True)
    #         elif item.objectName() == 'lineEdit_restore_SL2':
    #             fpath = f'NOT_FOR_GIT/backup/subject_level_2/{path}'
    #             table = 'Subject_level_2'
    #         elif item.objectName() == 'lineEdit_restore_DS_info':
    #             fpath = f'NOT_FOR_GIT/backup/INFO/{path}'
    #             table = 'DS_info'
    #         else:
    #             fpath = f'NOT_FOR_GIT/backup/QA/{path}'
    #             table = 'QA'
    #         # df = pd.read_excel(fpath)
    #         # print(df)
    #         for row in df.itertuples():
    #             print(row)
    #             try:
    #                 if table == 'Subject_level_1':
    #                     query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]}, '{row[2]}')"
    #                 elif table == 'Subject_level_2':
    #                     query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},'{row[3]}')"
    #                 elif table == 'DS_info':
    #                     query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},{row[3]}," \
    #                         f"'{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}'," \
    #                         f" '{row[9]}', '{row[10]}', '{row[11]}', '{row[12]}','{row[13]}')"
    #                 # else:
    #                 #     query = f"INSERT INTO {table} ({','.join(df.columns)}) VALUES ({row[1]},{row[2]},{row[3]}," \
    #                 #             f"'{row[4]}','{row[5]}','{row[6]}','{row[7]}','{row[8]}',{row[9]})"
    #                 mycursor = mydb.cursor()
    #                 print(query)
    #                 mycursor.execute(query)
    #                 mydb.commit()
    #                 print('Информация успешно записана')
    #             except Exception as e:
    #                 pass
    #                 print(e)


##############################################

    # def backup_ds_info_all(self):
    #     text_result = ''
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
    #                                      self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #     checked_list = [self.checkBox_DS_info_backup_local, self.checkBox_DS_info_backup_NAS, \
    #                     self.checkBox_DS_QA_backup_local, self.checkBox_DS_QA_backup_NAS, \
    #                     self.checkBox_SL_1_backup_local, self.checkBox_SL_1_backup_NAS, \
    #                     self.checkBox_SL_2_backup_local, self.checkBox_SL_2_backup_NAS,]
    #     if connection == True:
    #         for item in checked_list:
    #             if item.text()[-4:] == 'INFO':
    #                 table = 'DS_info'
    #             elif item.text()[-1] == '1':
    #                     table = 'Subject_level_1'
    #             elif item.text()[-1] == '2':
    #                  table = 'Subject_level_2'
    #             else:
    #                  table = 'QA'
    #             path = f'{item.text()}/backup_{table}_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx'
    #             try:
    #                 mycursor = mydb.cursor()
    #                 mycursor.execute(
    #                 f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND table_schema = 'DS'")
    #                 result = mycursor.fetchall()
    #                 print(result)
    #                 columns = [x[0] for x in result]
    #                 mycursor.execute(f"SELECT * from {table}")
    #                 result = mycursor.fetchall()
    #                 df = pd.DataFrame(result, columns=columns)
    #                 df.to_excel(path, index=False)
    #                 df1 = pd.DataFrame(result)
    #                 df1.to_excel(path, index=False)
    #                 text_result += f'- успешный backup {table} в {path}\n'
    #             except Exception as c:
    #                 print(c)
    #                 text_result += f'- Неудачный backup {table} в {path}\n'
    #         self.label_backup_result.setText(text_result)
    #         if 'Неудачный' in text_result:
    #             self.label_backup_result.setStyleSheet('color:red')
    #         else:
    #             self.label_backup_result.setStyleSheet('color:green')

##########################

    # def backup_ds_info(self):
    #     text_result = ''
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(),
    #                                      self.lineEdit_pass.text(), self.lineEdit_name_of_db.text())
    #     checked_list = [self.checkBox_DS_info_backup_local, self.checkBox_DS_info_backup_NAS, \
    #                     self.checkBox_DS_QA_backup_local, self.checkBox_DS_QA_backup_NAS, \
    #                     self.checkBox_SL_1_backup_local, self.checkBox_SL_1_backup_NAS, \
    #                     self.checkBox_SL_2_backup_local, self.checkBox_SL_2_backup_NAS,]
    #     if connection == True:
    #         for item in checked_list:
    #             if item.isChecked():
    #                 if item.text()[-4:] == 'INFO':
    #                     table = 'DS_info'
    #                 elif item.text()[-1] == '1':
    #                     table = 'Subject_level_1'
    #                 elif item.text()[-1] == '2':
    #                     table = 'Subject_level_2'
    #                 else:
    #                     table = 'QA'
    #                 path = f'{item.text()}/backup_{table}_db_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.xlsx'
    #                 try:
    #                     mycursor = mydb.cursor()
    #                     mycursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = '{table}' AND table_schema = 'DS'")
    #                     result = mycursor.fetchall()
    #                     print(result)
    #                     columns = [x[0] for x in result]
    #                     mycursor.execute(f"SELECT * from {table}")
    #                     result = mycursor.fetchall()
    #                     df = pd.DataFrame(result, columns=columns)
    #                     df.to_excel(path, index=False)
    #                     text_result += f'- успешный backup {table} в {path}\n'
    #                 except Exception as c:
    #                     print(c)
    #                     text_result += f'- Неудачный backup {table} в {path}\n'
    #         self.label_backup_result.setText(text_result)
    #         if 'Неудачный' in text_result:
    #             self.label_backup_result.setStyleSheet('color:red')
    #         else:
    #             self.label_backup_result.setStyleSheet('color:green')
    #
    #
    #


#################################




###################################


    # def select_random_from_db(self):
    #     for item in os.listdir(self.tempdir)[1:]:
    #         os.remove('//'.join([self.tempdir, item]))
    #     query = """select * from ds_info where for_question = 1 and file is NOT NULL"""
    #     mydb, connection = connect_to_db(self.lineEdit_ip.text(), self.lineEdit_port.text(), self.lineEdit_login.text(), self.lineEdit_pass.text(), 'test_for_blob')
    #     if connection == True:
    #         try:
    #             mycursor = mydb.cursor()
    #             mycursor.execute(query)
    #             result = mycursor.fetchall()
    #             question = random.choice(result)
    #             if question:
    #                 for i in question:
    #                     print(i)
    #                 self.textBrowser_for_question.setText(f'{str(question[3])}')
    #                 self.textBrowser_for_question.setText(f'{str(question[4])}')
    #                 self.filename_to_db = question[5]
    #                 self.fileformat_to_db = question[6]
    #                 self.file = question[7]
    #             else:
    #                 self.textBrowser_for_question.setText('Nothing find')
    #                 self.textBrowser_for_question.setStyleSheet('color:red')
    #         except Exception as e:
    #             e = string_split(str(e))
    #             print(e)
    #             self.textBrowser_for_question.setText('Can\'t select information from DB' + '\n' + e)
    #             self.textBrowser_for_question.setStyleSheet('color:red')
    #     else:
    #         print(connection)
    #         self.textBrowser_for_question.setText('Not connected to DB' + '\n' + string_split(str(connection)))
    #         self.textBrowser_for_question.setStyleSheet('color:red')


################################################
    #
    # def load_image(self):
    #     myPixmap = QPixmap('2.jpg')
    #     myScaledPixmap = myPixmap.scaled(self.label_img.size())
    #     self.label_img.setPixmap(myScaledPixmap)