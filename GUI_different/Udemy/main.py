import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()

window.statusBar().showMessage('Welcom to PyWt6 Course')
window.menuBar().addMenu('File')
window.menuBar().addMenu('Properties')

window.show()
sys.exit(app.exec())