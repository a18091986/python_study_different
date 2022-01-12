from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QTextDocument
from PyQt6.QtCore import QRect, Qt, QRectF
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,300,300)
        self.setWindowTitle('Text')
        self.setWindowIcon(QIcon('../images/python.svg'))

    def paintEvent(self, event):

        painter = QPainter(self)

        painter.drawText(50,50, 'PyQt6')

        rect = QRect(50,50,100,100)

        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, 'PyQt6 Course')

        document = QTextDocument()
        rect2 = QRectF(0,0,300,300)
        document.setTextWidth(rect2.width())
        document.setHtml('<b>Welcome to PyQt6</b><i>Udemy Course</i> \n <font size = "15" color = "red">Enjoy It</font>')
        document.drawContents(painter,rect2)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())