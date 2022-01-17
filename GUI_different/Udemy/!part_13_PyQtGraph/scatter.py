import pyqtgraph
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
import pyqtgraph as pg
import numpy as np


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph Scatter')

        x = np.random.normal(size=1000)
        y = np.random.random(size=1000)

        self.pw = pg.PlotWidget()

        self.plot = self.pw.plot(x,y,pen=None, symbol = 'o', symbolBrush = 'r')

        self.plot_btn = QPushButton('Replot')

        self.plot_btn.clicked.connect(self.plot_scatter)

        vbox = QVBoxLayout()
        vbox.addWidget(self.pw)
        vbox.addWidget(self.plot_btn)

        self.setLayout(vbox)

    def plot_scatter(self):
        x = np.random.normal(size=1000)
        y = np.random.random(size=1000)

        self.plot.setData(x,y)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
