import pyqtgraph
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout, QLineEdit
import sys
import pyqtgraph as pg
import numpy as np


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph LineGraph')

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.x1 = QLineEdit()
        self.x2 = QLineEdit()
        self.x3 = QLineEdit()
        self.x4 = QLineEdit()

        self.y1 = QLineEdit()
        self.y2 = QLineEdit()
        self.y3 = QLineEdit()
        self.y4 = QLineEdit()

        btn = QPushButton('Plot')

        btn.clicked.connect(self.plot)

        btn2 = QPushButton('Clear')

        btn2.clicked.connect(self.clear)

        self.myplot = pg.PlotWidget()

        hbox.addWidget(self.x1)
        hbox.addWidget(self.x2)
        hbox.addWidget(self.x3)
        hbox.addWidget(self.x4)

        hbox2.addWidget(self.y1)
        hbox2.addWidget(self.y2)
        hbox2.addWidget(self.y3)
        hbox2.addWidget(self.y4)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        vbox.addWidget(self.myplot)
        vbox.addWidget(btn)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

    def plot(self):
        x1 = int(self.x1.text())
        x2 = int(self.x2.text())
        x3 = int(self.x3.text())
        x4 = int(self.x4.text())

        y1 = int(self.y1.text())
        y2 = int(self.y2.text())
        y3 = int(self.y3.text())
        y4 = int(self.y4.text())

        x = np.array([x1,x2,x3,x4])
        y = np.array([y1,y2,y3,y4])

        self.myplot.plot(x,y)


    def clear(self):
        self.myplot.clear()



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
