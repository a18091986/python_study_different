from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QGridLayout')
        self.setWindowIcon(QIcon('../images/icon.png'))

        qgrid = QGridLayout()

        btn1 = QPushButton('One')
        btn2 = QPushButton('Two')
        btn3 = QPushButton('Three')
        btn4 = QPushButton('Four')
        btn5 = QPushButton('Five')
        btn6 = QPushButton('Six')
        btn7 = QPushButton('Seven')
        btn8 = QPushButton('Eight')

        qgrid.addWidget(btn1,0,0)
        qgrid.addWidget(btn2,0,1)
        qgrid.addWidget(btn3,0,2)
        qgrid.addWidget(btn4,0,3)
        qgrid.addWidget(btn5,1,0)
        qgrid.addWidget(btn6,1,1)
        qgrid.addWidget(btn7,1,2)
        qgrid.addWidget(btn8,1,3)

        self.setLayout(qgrid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())