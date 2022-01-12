from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QHBoxLayout')
        self.setWindowIcon(QIcon('../images/icon.png'))

        hbox = QHBoxLayout()

        btn1 = QPushButton('Click One')
        btn2 = QPushButton('Click Two')
        btn3 = QPushButton('Click Three')
        btn4 = QPushButton('Click Four')

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        hbox.addSpacing(100)
        hbox.addStretch(10)

        self.setLayout(hbox)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())