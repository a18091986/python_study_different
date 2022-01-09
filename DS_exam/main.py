import random

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from gui import Ui_Form
from random import randint
from db_connect import connect_to_db
import sys

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.pushButton_new_question.clicked.connect(self.get_question)
        self.pushButton_send.clicked.connect(self.send_answer)

    def get_question(self):
        mydb = connect_to_db()
        mycursor = mydb.cursor()
        # определяю количество строк в таблице по id c целью генерации рандомного
        # запроса в рамках этого диапазона
        mycursor.execute('select * from QA')
        result = mycursor.fetchall()
        query = f'select question from QA where id = {random.randint(1, len(result))}'
        mycursor.execute(query)
        self.label_question.setText(mycursor.fetchone()[0])

    def send_answer(self):
        mydb = connect_to_db()
        mycursor = mydb.cursor()
        question = self.label_question.text()
        answer = self.lineEdit_answer.text()
        # print(answer)
        query = f'select answer from QA where question = "{question}"'
        mycursor.execute(query)
        result = mycursor.fetchone()[0]
        if result == answer:
            self.label_answer_result.setText('Your answer is right')
        else:
            self.label_answer_result.setText('Your answer is wrong')
        self.label_right_answer.setText(result)



app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
