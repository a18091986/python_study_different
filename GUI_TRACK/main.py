from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QDate
import pickle
import os


dirname, filename = os.path.split(os.path.realpath(__file__))
print(dirname)
Form, Window = uic.loadUiType(dirname+"\\qt/TRACKER.ui")



app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def on_click():
    global start_date, calc_date, description
    calc_date = form.calendarWidget.selectedDate()
    description = form.plainTextEdit.toPlainText()
    # print(form.plainTextEdit.toPlainText(), end = ' ')
    # print(form.dateEdit.dateTime().toString('dd-MM-yyyy'), end = ' ')
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'), end = ' ')
    save_to_file()

    # date = QDate(2022,1,31)
    # form.calendarWidget.setSelectedDate(date)
    # print(form.calendarWidget.selectedDate().toString('dd-MM-yyyy'), end=' ')

def on_click_calendar():
    global start_date, calc_date
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    form.label_3.setText(f'До наступления события осталось {delta_days} дней')

def on_dateEdit_change():
    global start_date, calc_date, current_date
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = current_date.daysTo(calc_date)
    form.label_3.setText(f'До наступления события осталось {delta_days} дней')

def save_to_file():
    global start_date, calc_date, description
    start_date = QDate(2022,1,4)
    data_to_save = {'start': start_date, 'end' : calc_date, 'description' : description}
    file1 = open(f'{dirname}\config.txt', 'wb')
    pickle.dump(data_to_save, file1)
    file1.close()

def read_from_file():
    global start_date, calc_date, description, current_date, delta_days
    try:
        file1 = open(f'{dirname}\config.txt', 'rb')
        data_to_load = pickle.load(file1)
        file1.close()
        start_date = data_to_load['start']
        calc_date = data_to_load['end']
        description = data_to_load['description']
        print(f"Начальная дата: {start_date.toString('dd-MM-yyyy')}, "
              f"Дата события: {calc_date.toString('dd-MM-yyyy')}, "
              f"Описание: {description}")
        form.calendarWidget.setSelectedDate(calc_date)
        form.dateEdit.setDate(calc_date)
        form.plainTextEdit.setPlainText(description)
        form.progressBar.setProperty('value', start_date.daysTo(current_date)*100/start_date.daysTo(calc_date))

    except:
        print('не могу прочитать файл')


form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateEdit_change)


start_date = form.calendarWidget.selectedDate()
current_date = form.calendarWidget.selectedDate()

read_from_file()

calc_date = form.calendarWidget.selectedDate()
delta_days = current_date.daysTo(calc_date)
description = form.plainTextEdit.toPlainText()

form.label.setText(f'Трекер события от {start_date.toString("dd-MM-yyyy")}')
on_click_calendar()
form.label_3.setText(f'До наступления события осталось {delta_days} дней')
app.exec_()


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     w = Ui()
#     w.show()
#     sys.exit(app.exec_())
