from datetime import datetime
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from client_ui import Ui_MainWindow
from PyQt6 import QtCore
import requests

class messanger_management(QMainWindow, Ui_MainWindow):
    def __init__(self, host):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.host = host

        self.pushButton.pressed.connect(self.send_message)
        self.after = 0
        #to run by timer

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time'])
            self.textBrowser.append(f"{dt.time()} {message['name']}")
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')


    def get_messages(self):
        try:
            response = requests.get(url=self.host + '/messages',
                                params={'after': self.after})
        except:
            self.textBrowser.append('Сервер недоступен')
            self.textBrowser.append('')
            return

        messages = response.json()['messages']
        if messages:
            self.show_messages(messages)
            self.after = messages[-1]['time']

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(
            url=self.host + '/send',
            json={'name': name, 'text': text}
            )
        except:
            pass
            return

        if response.status_code != 200:
            self.textBrowser.append('Сервер недоступен')
            self.textBrowser.append('')
            return

        self.textEdit.clear()