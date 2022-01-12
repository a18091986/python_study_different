from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('Event handling')
        self.setWindowIcon(QIcon('../images/icon.png'))
        self.create_widgete()

    def create_widgete(self):
        hbox = QHBoxLayout()
        btn = QPushButton('Text')
        btn.clicked.connect(self.click_button)
        self.label = QLabel('Default Text')

        hbox.addWidget(btn)
        hbox.addWidget(self.label)
        self.setLayout(hbox)


    def click_button(self):
        self.label.setText('Another Text')
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('color:red')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())