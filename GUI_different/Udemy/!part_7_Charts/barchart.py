from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QPercentBarSeries
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QPointF
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('BarChart')
        self.setWindowIcon(QIcon('../images/python.png'))

        self.bar_chart()

    def bar_chart(self):
        set0 = QBarSet('Parwiz')
        set1 = QBarSet('Andreq')
        set2 = QBarSet('Ann')
        set3 = QBarSet('John')

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 7 << 0 << 10 << 1 << 3
        set2 << 3 << 2 << 1 << 4 << 5 << 6
        set3 << 4 << 5 << 6 << 2 << 1 << 0

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle('Bar Chart Example')
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)

        chartview = QChartView(chart)

        self.setCentralWidget(chartview)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


