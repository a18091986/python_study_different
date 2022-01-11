# Form implementation generated from reading ui file 'C:\Users\admin\Desktop\PYTHON_2022\python_study_different\GUI_different\Udemy\Qt_UI\calculator.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 299)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_first = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_first.setFont(font)
        self.label_first.setObjectName("label_first")
        self.horizontalLayout.addWidget(self.label_first)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.LE_1 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LE_1.setFont(font)
        self.LE_1.setObjectName("LE_1")
        self.horizontalLayout.addWidget(self.LE_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_second = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_second.setFont(font)
        self.label_second.setObjectName("label_second")
        self.horizontalLayout_2.addWidget(self.label_second)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.LE_2 = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LE_2.setFont(font)
        self.LE_2.setObjectName("LE_2")
        self.horizontalLayout_2.addWidget(self.LE_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.B_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B_add.setFont(font)
        self.B_add.setObjectName("B_add")

        self.B_add.clicked.connect(self.add)

        self.horizontalLayout_3.addWidget(self.B_add)
        self.B_minus = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B_minus.setFont(font)
        self.B_minus.setObjectName("B_minus")

        self.B_minus.clicked.connect(self.minus)

        self.horizontalLayout_3.addWidget(self.B_minus)
        self.B_multi = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B_multi.setFont(font)
        self.B_multi.setObjectName("B_multi")

        self.B_multi.clicked.connect(self.multiply)

        self.horizontalLayout_3.addWidget(self.B_multi)
        self.B_dev = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.B_dev.setFont(font)
        self.B_dev.setObjectName("B_dev")

        self.B_dev.clicked.connect(self.devision)

        self.horizontalLayout_3.addWidget(self.B_dev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("QLabel\n"
"{\n"
"\n"
"color:rgb(3, 3, 255)\n"
"\n"
"}")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add(self):
        num1, num2 = float(self.LE_1.text()), float(self.LE_2.text())
        res = num1 + num2
        self.label_result.setText(str(res))

    def minus(self):
        num1, num2 = float(self.LE_1.text()), float(self.LE_2.text())
        res = num1 - num2
        self.label_result.setText(str(res))

    def multiply(self):
        num1, num2 = float(self.LE_1.text()), float(self.LE_2.text())
        res = num1 * num2
        self.label_result.setText(str(res))

    def devision(self):
        num1, num2 = float(self.LE_1.text()), float(self.LE_2.text())
        res = num1 / num2
        self.label_result.setText(str(res))


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_first.setText(_translate("Form", "First Number"))
        self.LE_1.setPlaceholderText(_translate("Form", "Please Enter First Number"))
        self.label_second.setText(_translate("Form", "Second Number"))
        self.LE_2.setPlaceholderText(_translate("Form", "Please Enter Second Number"))
        self.B_add.setText(_translate("Form", "+"))
        self.B_minus.setText(_translate("Form", "-"))
        self.B_multi.setText(_translate("Form", "*"))
        self.B_dev.setText(_translate("Form", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
