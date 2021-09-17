
import sys
sys.path.append('../BakApp_RPi')

from gui.core.functions import Functions
from qt_core import *


class SVGWidget(QWidget):
    def __init__(self,parent=None,image_name:str="icon_home",color:str="white",width=15,height=15):
        QWidget.__init__(self)
        if parent != None: self.setParent(parent)
        self.image_path = Functions.set_svg_icon(image_name)
        self.image = QPixmap(self.image_path)
        self.setFixedSize(width,height)
        self.scaledPix = self.image.scaled(self.size(), Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        self.color = QColor(color)

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        rect = QRect(0,0,self.width(),self.height())
        painter = QPainter(self.image)
        painter.setRenderHint(QPainter.Antialiasing)
        self.scaledPix = self.image.scaled(self.size(), Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)

        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(self.image.rect(),self.color)

        p.drawPixmap(
                    round((self.width()-self.scaledPix.width())/2),
                    round((self.height()-self.scaledPix.height())/2),
                    self.scaledPix)
        painter.end() 
        p.end()
    
    def updateSize(self,width,height):
        self.setFixedSize(width,height)
        self.repaint()


# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class _MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.initUI()
        

    def initUI(self):
        self.button = SVGWidget("icon_team","blue",100,100)
        self.button.show()
        



if __name__ == '__main__':
    app = _MainApp(sys.argv)
    sys.exit(app.exec_())  