from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PythonGuiDevelopment')
        self.setWindowIcon(QIcon('../images/icon.png'))
        # self.setFixedWidth(700) #фиксируем ширину
        # self.setFixedHeight(400) #фиксируем высоту
        # self.setFixedSize(500,500) #фиксируем ширину и высоту
        self.setStyleSheet('background-color:green')
        self.setWindowOpacity(0.7)

        #pyuic6 -x
        # C:\Users\admin\Desktop\PYTHON_2022\python_study_different\GUI_different\Udemy\first.ui
        # -o
        # C:\Users\admin\Desktop\PYTHON_2022\python_study_different\GUI_different\Udemy\first_window.py

        # pyuic6 -x C:\Users\admin\Desktop\PYTHON_2022\python_study_different\GUI_different\Udemy\first.ui -o C:\Users\admin\Desktop\PYTHON_2022\python_study_different\GUI_different\Udemy\first_window.py


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())