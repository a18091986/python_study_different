from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QConicalGradient, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,300,300)
        self.setWindowTitle('Text')
        self.setWindowIcon(QIcon('../images/python.svg'))


    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.red, 4,Qt.PenStyle.SolidLine))

        conicalGradient = QConicalGradient(150,100,10)

        conicalGradient.setColorAt(0.0, Qt.GlobalColor.yellow)
        conicalGradient.setColorAt(0.5, Qt.GlobalColor.green)
        conicalGradient.setColorAt(1.0, Qt.GlobalColor.blue)

        painter.setBrush(QBrush(conicalGradient))

        painter.drawRect(50,50,200,200)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())