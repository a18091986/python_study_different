from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries
from PyQt6.QtCore import QPointF
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('LineCharts')
        self.setWindowIcon(QIcon('../images/python.png'))

        self.line_chart()

    def line_chart(self):
        series = QLineSeries()

        series.append([
            QPointF(1.0,1.0), QPointF(2.0,73.0), QPointF(3.0,268.0), QPointF(4.0,17.0), QPointF(5.0,120.0), QPointF(6.0,210.0)
        ])

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle('LineChart Example')
        # chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        chart.setTheme(QChart.ChartTheme.ChartThemeHighContrast)

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


