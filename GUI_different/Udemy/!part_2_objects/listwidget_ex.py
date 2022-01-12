from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('listwidget')
        self.setWindowIcon(QIcon('../images/icon.png'))

        vbox = QVBoxLayout()

        self.list_w = QListWidget()

        self.list_w.insertItem(0, 'Python')
        self.list_w.insertItem(1, 'Java')
        self.list_w.insertItem(2, 'C++')
        self.list_w.insertItem(3, 'C#')
        self.list_w.insertItem(4, 'Kotlin')
        self.list_w.setFont(QFont('Times', 16))
        self.list_w.setStyleSheet('background-color:pink')

        self.list_w.clicked.connect(self.item_from_list_select)

        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 20))

        vbox.addWidget(self.list_w)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_from_list_select(self):
        item = self.list_w.currentItem()
        self.label.setText(f'You have selected {item.text()}')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())