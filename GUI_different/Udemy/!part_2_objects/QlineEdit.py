from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('PythonGuiDevelopment')
        self.setWindowIcon(QIcon('../images/icon.png'))

        lineedit = QLineEdit(self)
        lineedit.setFont(QFont('Arial', 25))
        lineedit.setGeometry(10,10,500,100)
        # lineedit.setText('Default text')
        lineedit.setPlaceholderText('Сюда можно что-то написать')
        # lineedit.setEnabled(False)
        lineedit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())