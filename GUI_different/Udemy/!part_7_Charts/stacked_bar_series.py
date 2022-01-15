from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QStackedBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QPointF
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,500,500)
        self.setWindowTitle('Stacked Bar Series')
        self.setWindowIcon(QIcon('../images/python.png'))

        low = QBarSet('min')
        high = QBarSet('max')

        low.append([-52, -50, -45.3, 37.0, -25.6, -8.0, -6.0, -11.8, -19.7, -32.8, -43.0, -48.0])
        high.append([11.9, 12.8, 18.5, 26.5, 32.0, 34.8, 38.2, 34.8, 29.8, 20.4, 15.1, 11.8])

        series = QStackedBarSeries()

        series.append(low)
        series.append(high)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Temperature')

        categories = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']

        axis_x = QBarCategoryAxis()
        axis_x.append(categories)

        axis_x.setTitleText('month')

        axis_y = QValueAxis()
        axis_y.setRange(-52,52)
        axis_y.setTitleText('temperature [&deg;C]')



        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())


