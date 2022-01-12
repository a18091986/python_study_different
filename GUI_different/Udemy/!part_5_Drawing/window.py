from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QGraphicsItem
import sys
from handling_key_press_event import MyRect

class Window(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800, 600)
        self.show()


        scene = QGraphicsScene()

        # rect = QGraphicsRectItem()
        rect = MyRect()
        rect.setRect(0,0,100,100)
        scene.addItem(rect)

        rect.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        rect.setFocus()


        self.setScene(scene)




app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())