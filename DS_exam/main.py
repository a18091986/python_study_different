import sys
from PyQt6.QtWidgets import QApplication
from DS_exam_management_system import DS_exam_management_system


app = QApplication(sys.argv)
DS_exam_management_system = DS_exam_management_system()
sys.exit(app.exec())