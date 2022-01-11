from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,300,300)
        self.setWindowTitle('Rectangle')
        self.setWindowIcon(QIcon('../images/python.svg'))


    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashLine))
        # painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotLine))
        # painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.DiagCrossPattern))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.drawRect(100, 15,100,200)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())