from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('Slider')
        self.setWindowIcon(QIcon('../images/icon.png'))


        hbox = QHBoxLayout()

        self.label = QLabel()
        self.setFont(QFont('Arial', 20))
        hbox.addWidget(self.label)

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(10)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.change_slider)

        hbox.addWidget(self.slider)

        self.setLayout(hbox)

    def change_slider(self):
        val = self.slider.value()
        self.label.setText(str(val))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())