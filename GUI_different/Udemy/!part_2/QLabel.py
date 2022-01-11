from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PythonGuiDevelopment')
        self.setWindowIcon(QIcon('../images/icon.png'))
        # self.setStyleSheet('background-color:green')
        # self.setWindowOpacity(0.9)


        gifLabel = QLabel(self)
        movie = QMovie('../images/dragon.gif')
        gifLabel.setMovie(movie)
        movie.start()
        gifLabel.move(170,100)
        movie.setSpeed(10)
        '''
        label = QLabel(self)
        pixmap = QPixmap('../images/python.png').scaled(100,100)
        label.setPixmap(pixmap)
        '''

        '''
        label = QLabel('Python GUI development', self)
        # label.setText("New Text is here")
        label.move(100,100)
        label.setFont(QFont('Arial', 15))
        label.setStyleSheet('color:blue')
        # label.setNum(15)
        # label.clear()
        '''


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())