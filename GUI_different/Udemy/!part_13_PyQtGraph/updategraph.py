import pyqtgraph
from PyQt6.QtWidgets import QApplication, QWidget,QVBoxLayout, QPushButton
import sys
import pyqtgraph as pg
import numpy as np
from PyQt6.QtCore import QTimer



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Update Graph')


        vbox = QVBoxLayout()

        self.pw = pg.PlotWidget()

        self.btn = QPushButton('Update')

        self.btn.clicked.connect(self.show_plot)

        x = np.random.normal(size=(100))
        y = np.random.normal(size=(100))

        self.pw.plot(x,y, clear=False)

        vbox.addWidget(self.pw)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

    def update(self):
        x = np.random.normal(size=(100))
        y = np.random.normal(size=(100))

        self.pw.plot(x,y, clear=False)

    def show_plot(self):
        # self.timer = QTimer()
        self.timer = pg.QtCore.QTimer()
        self.timer.setSingleShot(False)

        self.timer.timeout.connect(self.update)
        self.timer.start(100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
