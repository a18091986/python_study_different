from PyQt6.QtWidgets import QApplication, QWidget, QSpinBox, QHBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('SpinBox')
        self.setWindowIcon(QIcon('../images/icon.png'))

        hbox = QHBoxLayout()

        self.label = QLabel('Laptop Price: ')
        self.label.setFont(QFont('Times',15))
        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.total_result = QLineEdit()

        self.spinbox.valueChanged.connect(self.spin_selected)

        hbox.addWidget(self.label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)


    def spin_selected(self):
        if self.lineedit.text().isnumeric():
           price = int(self.lineedit.text())
           tPrice = price * self.spinbox.value()
           self.total_result.setText(str(tPrice))
        else:
            self.total_result.setText('Error')
        # try:
        #     self.total_result.setText('sdfsd')
        # except:
        #     pass

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())