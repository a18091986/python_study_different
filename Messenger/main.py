import sys
from PyQt6.QtWidgets import QApplication
from messanger_management import messanger_management

app = QApplication(sys.argv)
messanger_management = messanger_management('http://c8eb-46-8-219-63.ngrok.io')
sys.exit(app.exec())