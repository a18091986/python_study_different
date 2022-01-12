from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Table')
        self.setWindowIcon(QIcon('../images/icon.png'))

        vbox = QVBoxLayout()

        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(3)

        table.setItem(0, 0, QTableWidgetItem('Name'))
        table.setItem(0, 1, QTableWidgetItem('Email'))
        table.setItem(0, 2, QTableWidgetItem('Phone'))

        table.setItem(1, 0, QTableWidgetItem('Andrei'))
        table.setItem(1, 1, QTableWidgetItem('behappyman@mail.ru'))
        table.setItem(1, 2, QTableWidgetItem('89262535088'))

        table.setItem(2, 0, QTableWidgetItem('Ann'))
        table.setItem(2, 1, QTableWidgetItem('ann@mail.ru'))
        table.setItem(2, 2, QTableWidgetItem('89152535088'))


        vbox.addWidget(table)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())