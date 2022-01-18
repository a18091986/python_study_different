from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox
from main_window import Ui_MainWindow
from db_connect import connect_to_db
from string_split import string_split
from random import choice


class DS_exam_management_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.set_categories_to_combobox()

        self.pushButton_insert_into_db.clicked.connect(self.add_information)


    def add_information(self):

        question = self.lineEdit_question_into_db.text()
        print('!')
        category = self.comboBox_question_category.currentText()
        print('!')

        mydb, connection = connect_to_db()

        if connection == True:

            print('Connection is Established')

            if question == '' or category == '':
                self.label_result.setText('Please add all fields')
                self.label_result.setStyleSheet('color:red')

            else:
                try:
                    mycursor = mydb.cursor()
                    query = f'insert into qa (question, category)  VALUE (%s, %s)'
                    value = (question, category)
                    mycursor.execute(query, value)
                    mydb.commit()
                    self.label_result.setText('Information added successfully')
                    self.label_result.setStyleSheet('color:green')
                    self.lineEdit_question_into_db.setText('')
                except Exception as e:
                    e = string_split(str(e))
                    self.label_result.setText('Can\'t add information to DB' + '\n' + e)
                    self.label_result.setStyleSheet('color:red')

        else:
            self.label_result.setText('Not connected to DB' + '\n' + string_split(str(connection)))
            self.label_result.setStyleSheet('color:red')

    def set_categories_to_combobox(self):
        result_list = []
        mydb, connection = connect_to_db()
        if connection == True:
            print('Connection is Established')
            try:
                mycursor = mydb.cursor()
                mycursor.execute(f'select * from qa group by category')
                result = mycursor.fetchall()
                if result:
                    for row in result:
                       result_list.append(row[2])
                    self.comboBox_question_category.addItems(result_list)
                else:
                    self.label_result.setText(f'Информация о категориях не найдена')
            except Exception as e:
                e = str(e)
                print(e)
        else:
            print(str(connection))





