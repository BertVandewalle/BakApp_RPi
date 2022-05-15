import math, sys
from qt_core import *

class GoalView(QGraphicsView):

    def __init__(self,parent=None):
        super().__init__()
        self.pwidget = parent
        self.setParent(parent)
        self.s = QGraphicsScene()
        self.initScene()
        self.setScene(self.s)
        self.setGeometry(0,0,500,500)
        self.setBackgroundBrush(Qt.green)
        self.show()

    def initScene(self):
        self.s.sceneRect = QRectF(0,0,500,500)
        self.goalLine = QGraphicsLineItem(0,self.parent().height()/2,self.parent().width(),self.parent().height()/2)
        self.s.addItem(self.goalLine)
        self.s.setBackgroundBrush(Qt.blue)

    def paint(self,painter:QPainter):
        self.setGeometry(0,0,self.parent().width(),self.parent().height())
        self.s.update(0,0,self.width(),self.height())
        self.goalLine.setLine(0,self.s.height()/2,self.s.width(),self.s.height()/2)
        # print('repainting')
        pass
    


class GoalLine(QGraphicsLineItem):
    def __init__(self,parent):
        super().__init__(parent)
        self.setLine(0,self.parent().height()/2,self.parent().width(),self.parent().height()/2)
    
    def paint(self,painter:QPainter):
        self.setLine(self.setLine(0,self.parent().height()/2,self.parent().width(),self.parent().height()/2))

class GoalWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,700,700)
        self.view = GoalView(self)
        self.show()

    def paintEvent(self,event):
        p = QPainter()
        self.view.paint(p)


def main():
    app = QApplication(sys.argv)
    window = GoalWidget()



    sys.exit(app.exec())


if __name__ == "__main__":
    main()