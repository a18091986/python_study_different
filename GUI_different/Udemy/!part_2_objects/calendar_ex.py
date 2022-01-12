from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle('QCalendar_widget')
        self.setWindowIcon(QIcon('../images/icon.png'))

        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel('')
        self.label.setFont(QFont('Arial', 15))
        self.label.setStyleSheet('color:green')


        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def calendar_date(self):
        dateSelect = self.calendar.selectedDate()
        date_string = str(dateSelect.toPyDate())

        self.label.setText(date_string)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())