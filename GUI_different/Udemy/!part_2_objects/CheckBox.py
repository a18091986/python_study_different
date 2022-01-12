from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('CheckBox')
        self.setWindowIcon(QIcon('../images/icon.png'))

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.label = QLabel('Hello')
        self.label.setFont(QFont('Arial', 22))


        self.chkb1 = QCheckBox('Python')
        self.chkb1.setIcon(QIcon('../images/python.png'))
        self.chkb1.setIconSize(QSize(30,30))
        self.chkb1.setFont(QFont('Arial', 16))
        self.chkb1.stateChanged.connect(self.chkb_selected)

        self.chkb2 = QCheckBox('Java')
        self.chkb2.setIcon(QIcon('../images/java.png'))
        self.chkb2.setIconSize(QSize(30,30))
        self.chkb2.setFont(QFont('Arial', 16))
        self.chkb2.stateChanged.connect(self.chkb_selected)

        self.chkb3 = QCheckBox('JS')
        self.chkb3.setIcon(QIcon('../images/JS.png'))
        self.chkb3.setIconSize(QSize(30,30))
        self.chkb3.setFont(QFont('Arial', 16))
        self.chkb3.stateChanged.connect(self.chkb_selected)


        hbox.addWidget(self.chkb1)
        hbox.addWidget(self.chkb2)
        hbox.addWidget(self.chkb3)

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


    def chkb_selected(self):
        val = ''
        if self.chkb1.isChecked():
            val = self.chkb1.text()
        if self.chkb2.isChecked():
            val = self.chkb2.text()
        if self.chkb3.isChecked():
            val = self.chkb3.text()
        self.label.setText(f'Your have selected: {val}')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())