from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView,QPieSeries
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QPointF
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('linechart and barchart')
        self.setWindowIcon(QIcon('../images/python.png'))

        series = QPieSeries()
        series.setHoleSize(0.4)
        series.append('Protein 4.3%', 4.3)

        my_slice = series.append('Fat 15.6 %', 15.6)
        my_slice.setExploded(True)

        series.append('Other 30%', 3)
        series.append('Carbs 57%', 57)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTitle('Donut Chart')
        chart.setTheme(QChart.ChartTheme.ChartThemeBrownSand)

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


