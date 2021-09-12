from gui.core.functions import Functions
from qt_core import *
import sys
class SvgTest(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = Functions.set_svg_image("table-football.svg")
        self.show()

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        rect = QRect(0,0,self.width(),self.height())
        image = QPixmap(self.image_path)
        #image= image.scaled(300,800,Qt.KeepAspectRatio)
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(image.rect(), QColor("red"))

        size = self.size()
        point = QPoint(0,0)
        scaledPix = image.scaled(size, Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        point.setX((size.width() - scaledPix.width())/2)
        point.setY((size.height() - scaledPix.height())/2)
        p.drawPixmap(point, scaledPix)
        painter.end() 
        p.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = SvgTest()
    sys.exit(app.exec_())      
           
