from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication

Form, _ = uic.loadUiType("qt/1.ui")

class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.printButtonPressed)
        self.label.setText('Hellow World')
        self.CB_1.setChecked(False)
        self.CB_2.setChecked(True)
        for i in range(15):
            self.LW.addItem(f"{i}st element")
        self.LW.clicked.connect(self.printItemClicked)
        self.LW.itemSelectionChanged.connect(self.printItemClicked)




    def printButtonPressed(self):
        print(f"'pressed', 'CB_1:' {self.CB_1.isChecked()}, 'СВ_2': {self.CB_2.isChecked()}")

    def printItemClicked(self):
        print('clicked', end = ' ')
        for i in self.LW.selectedItems():
            print(i.text())





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

