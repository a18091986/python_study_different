import sys

from PyQt6.QtWidgets import QApplication, QWidget,QLineEdit, QDoubleSpinBox
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi('../Qt_UI/Double_Spin_Demo.ui', self)

        self.price = self.findChild(QLineEdit, 'price')
        self.dspin = self.findChild(QDoubleSpinBox, 'dSpin')
        self.result = self.findChild(QLineEdit, 'total')
        self.dspin.valueChanged.connect(self.spin_selected)

    def spin_selected(self):
        try:
            _price = float(self.price.text())
            n = float(self.dspin.value())
            self.result.setText(str(_price*n))
        except:
            self.result.setText('error')


app = QApplication(sys.argv)
window = UI()


window.show()
app.exec()