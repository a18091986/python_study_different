from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QStackedBarSeries, QBarSet, QLineSeries, QBarSeries
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QPointF
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('linechart and barchart')
        self.setWindowIcon(QIcon('../images/python.png'))

        set0 = QBarSet('John')
        set1 = QBarSet('Bob')
        set2 = QBarSet('Ann')
        set3 = QBarSet('Andrew')
        set4 = QBarSet('Sam')

        set0.append([1,2,3,4,5,6])
        set1.append([5,0,0,4,0,7])
        set2.append([3,5,8,13,8,5])
        set3.append([5,6,7,3,4,5])
        set4.append([9,7,5,3,1,2])

        barseries = QBarSeries()
        barseries.append(set0)
        barseries.append(set1)
        barseries.append(set2)
        barseries.append(set3)
        barseries.append(set4)

        lineseries = QLineSeries()
        lineseries.append(QPointF(0,4))
        lineseries.append(QPointF(1,15))
        lineseries.append(QPointF(2,20))
        lineseries.append(QPointF(3,4))
        lineseries.append(QPointF(4,12))
        lineseries.append(QPointF(5,17))

        chart = QChart()

        chart.addSeries(barseries)
        chart.addSeries(lineseries)
        chart.setTitle('Line and Barchart')

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


