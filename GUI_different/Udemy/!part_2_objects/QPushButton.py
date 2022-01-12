from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PythonGuiDevelopment')
        self.setWindowIcon(QIcon('../images/icon.png'))
        self.create_button()



    def create_button(self):
        btn = QPushButton('Click', self)
        btn.setGeometry(100,100, 200,100)
        btn.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('../images/python.svg'))
        btn.setIconSize(QSize(20,20))

        #popup menu

        menu = QMenu()
        menu.setFont(QFont('Times', 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:red')
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Paste')
        btn.setMenu(menu )


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())