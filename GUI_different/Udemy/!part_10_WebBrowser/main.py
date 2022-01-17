from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QSize, QUrl
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("Web Browser")
        self.setWindowIcon(QIcon('icons/python.png'))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/back.png"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)


        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/reload.png"))
        self.reloadButton.setIconSize(QSize(36,36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize(36, 36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/home.png"))
        self.homeButton.setIconSize(QSize(36, 36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)


        self.addLineEdit = QLineEdit()
        self.addLineEdit.setFont(QFont("Times", 18))
        self.addLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("icons/search.png"))
        self.searchButton.setIconSize(QSize(36, 36))

        self.searchButton.clicked.connect(self.searchBtn)

        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://www.google.com'
        self.addLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))


    def searchBtn(self):
        myurl = self.addLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()


    def homeBtn(self):
        self.webEngineView.load(QUrl('https://www.google.com'))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())