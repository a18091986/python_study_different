from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QIcon, QPen, QBrush
from PyQt6.QtCore import Qt
import sys




class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('ClickText')
        self.setWindowIcon(QIcon('../images/python.svg'))

        scene = QGraphicsScene()

        greenBrush = QBrush(Qt.GlobalColor.green)
        yellowBrush = QBrush(Qt.GlobalColor.yellow)

        redPen = QPen(Qt.GlobalColor.red)
        redPen.setWidth(7)

        ellipse = scene.addEllipse(100,100,200,200,redPen,greenBrush)

        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)

        rect = scene.addRect(-100,-100,200,200, redPen, yellowBrush)

        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)






        view = QGraphicsView(scene, self)
        view.setGeometry(0,0, 280, 200)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())