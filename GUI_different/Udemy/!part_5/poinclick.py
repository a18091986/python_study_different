from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QFont, QPainter, QPen
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,300,300)
        self.setWindowTitle('Mouse Event')
        self.setWindowIcon(QIcon('../images/python.svg'))

        self.pos1 = [0,0]

    def paintEvent(self, event):
        painter = QPainter()

        painter.begin(self)

        pen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)
        painter.drawPoint(self.pos1[0], self.pos1[1])

        painter.end()


    def mousePressEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = self.pos().x(), self.pos().y()
            self.update()



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())