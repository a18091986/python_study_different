import pyqtgraph
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout,QPushButton, QLineEdit,QListWidget
import sys
import pyqtgraph as pg
import numpy as np


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQtGraph LineChart')

        btn = QPushButton('Click me')
        text = QLineEdit('Some Text')
        listw = QListWidget()

        grid = QGridLayout()

        myplot = pg.PlotWidget()

        x = np.array([0,1,2,4])
        y = np.array(([5,6,7,8]))
        myplot.plot(x,y)

        grid.addWidget(btn, 0,0)
        grid.addWidget(text, 1,0)
        grid.addWidget(listw, 2,0)
        grid.addWidget(myplot, 0,1,3,1)

        self.setLayout(grid)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
