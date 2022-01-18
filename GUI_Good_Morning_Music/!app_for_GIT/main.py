import sys
from PyQt6.QtWidgets import QApplication
from music_management_system import Music_management_system


app = QApplication(sys.argv)
Music_management_system = Music_management_system()
sys.exit(app.exec())