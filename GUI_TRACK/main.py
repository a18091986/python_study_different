from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate

Form, Window = uic.loadUiType("qt/TRACKER.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    print(form.plainTextEdit.toPlainText(), end = ' ')
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'), end = ' ')
    print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'), end = ' ')
    print('Clicked')



    # date = QDate(2022,1,31)
    # form.calendarWidget.setSelectedDate(date)
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'), end=' ')

def on_click_calendar():
    date = form.calendarWidget.selectedDate()
    form.dateEdit.setDate(date)

def on_dateEdit_change():
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'), end=' ')


form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateEdit_change)



app.exec_()


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     w = Ui()
#     w.show()
#     sys.exit(app.exec_())
