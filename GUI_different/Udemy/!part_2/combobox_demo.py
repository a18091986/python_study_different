import sys

from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('../Qt_UI/combobox_demo.ui', self)

        self.label_result = self.findChild(QLabel, 'label_result')
        self.combo = self.findChild(QComboBox, 'comboBox')
        self.combo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText(f'Your Favourite Language: {item}')



app = QApplication(sys.argv)
window = UI()
window.show()

app.exec()