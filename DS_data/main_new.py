import sys
from PyQt6.QtWidgets import QApplication
from DS_management_system_new import DS_management_system


app = QApplication(sys.argv)
DS_management_system = DS_management_system()
sys.exit(app.exec())