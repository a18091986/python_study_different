from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle('LCDNumber')
        self.setWindowIcon(QIcon('../images/icon.png'))
        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel('Select account type: ')
        label.setFont(QFont('Times', 16))

        self.combo = QComboBox()
        self.combo.addItem('Current Account')
        self.combo.addItem('Deposte Account')
        self.combo.addItem('Saving Account')


        vbox = QVBoxLayout()
        self.label_result = QLabel('')
        self.label_result.setFont(QFont('Times', 15))
        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)

        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.combo.currentTextChanged.connect(self.combo_changed)

        self.setLayout(vbox)


    def combo_changed(self):
        txt = self.combo.currentText()
        self.label_result.setText(f'Your account: {txt}')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())