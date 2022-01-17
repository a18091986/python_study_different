from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStyle, QSlider, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt,QUrl
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,500)
        self.setWindowTitle("PyQt Media Player")
        self.setWindowIcon(QIcon('icon.ico'))

        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaplayer.stateChanged.connect(self.mediastate_change)
        self.mediaplayer.positionChanged.connect(self.position_change)
        self.mediaplayer.durationChanged.connect(self.duration_change)


        videowidget = QVideoWidget()

        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_video)

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        hbox = QHBoxLayout()

        hbox.addWidget(openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()

        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        self.mediaplayer.setVideoOutput(videowidget)


    def open_video(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'open video')

        if filename != '':
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.mediaplayer.pause()

        else:
            self.mediaplayer.play()

    def mediastate_change(self):

        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def position_change(self, position):
        self.slider.setValue(position)


    def duration_change(self, duration):
        self.slider.setRange(0, duration)


    def set_position(self, position):
        self.mediaplayer.setPosition(position)



app = QApplication(sys.argv)
window = Window()

window.show()
sys.exit(app.exec())

