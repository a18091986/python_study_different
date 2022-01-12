from PyQt6.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QLabel, QLineEdit, QInputDialog, QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('InputDialog')
        self.setWindowIcon(QIcon('../images/icon.png'))

        self.create_dialog()

    def create_dialog(self):
        hbox = QHBoxLayout()

        label = QLabel('Choose Country')
        label.setFont(QFont('Arial', 15))

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont('Arial', 15))

        btn = QPushButton('Choose Country')
        btn.setFont(QFont('Arial', 15))
        # btn.clicked.connect(self.show_dialog)
        # btn.clicked.connect(self.get_text)
        btn.clicked.connect(self.get_int)


        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(btn)



        self.setLayout(hbox)


    def show_dialog(self):
        countries = ['Russia', 'Albania', 'USA', 'United States', 'Pakistan']

        country, ok = QInputDialog.getItem(self, 'Input Dialog', 'List of Countries', countries, 0, False)

        if ok and country:
            self.lineedit.setText(country)

    def get_text(self):
        mytext, ok = QInputDialog.getText(self, 'get username', 'Enter your name: ')
        if ok and mytext:
            self.lineedit.setText(mytext)

    def get_int(self):
        mynumber, ok = QInputDialog.getInt(self, 'Order Quantity', 'Enter Quantity: ', 1,2,0)
        if ok and mynumber:
            self.lineedit.setText(str(mynumber))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())