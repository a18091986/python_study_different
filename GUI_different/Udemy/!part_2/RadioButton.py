from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QRadioButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('RadioButton')
        self.setWindowIcon(QIcon('../images/icon.png'))
        self.create_radio()

    def create_radio(self):
        hbox = QHBoxLayout()
        rb1 = QRadioButton('Python')
        rb1.setIcon(QIcon('../images/python.png'))
        rb1.setIconSize(QSize(40,40))
        rb1.setFont(QFont('Times', 14))
        rb1.setChecked(True)

        hbox.addWidget(rb1)
        rb1.toggled.connect(self.radio_select)

        rb2 = QRadioButton('Java')
        rb2.setIcon(QIcon('../images/java.png'))
        rb2.setIconSize(QSize(40,40))
        rb2.setFont(QFont('Times', 14))
        rb2.setChecked(False)

        hbox.addWidget(rb2)
        rb2.toggled.connect(self.radio_select)

        rb3 = QRadioButton('JavaScript')
        rb3.setIcon(QIcon('../images/JS.png'))
        rb3.setIconSize(QSize(40,40))
        rb3.setFont(QFont('Times', 14))
        rb3.setChecked(False)

        hbox.addWidget(rb3)
        rb3.toggled.connect(self.radio_select)

        self.label = QLabel('')
        self.label.setFont(QFont('Arial',15))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def radio_select(self):
        rbtn = self.sender()
        if rbtn.isChecked():
            self.label.setText(f'You have selected:{rbtn.text()}')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())