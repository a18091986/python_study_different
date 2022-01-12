from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QVBoxLayout')
        self.setWindowIcon(QIcon('../images/icon.png'))

        vbox = QVBoxLayout()

        btn1 = QPushButton('Button_1')
        btn2 = QPushButton('Button_2')
        btn3 = QPushButton('Button_3')
        btn4 = QPushButton('Button_4')

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addSpacing(100)
        vbox.addStretch(10)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())