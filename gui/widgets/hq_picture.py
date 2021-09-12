import sys
sys.path.append('../BakApp_RPi')
from gui.widgets.circular_picture import ScaledCircularPicture
from gui.core.json_settings import Settings
from data_controller import DataController
from data_initializer import DataInitializer
from qt_core import *
import logging
# CREATES HIGH QUALITY PIXMAP IRRESPECTIVE OF SCALE (ANTIALIASING)
class ScaledHQPicture(QWidget):
    def __init__(self,pixMap:QPixmap):
        super().__init__()
        self._pixMap = pixMap
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(True)
        self.setSizePolicy(sizePolicy)
        self.scaledPix = self._pixMap

    def setPixmap(self,pixMap):
        self._pixMap = pixMap
        self.repaint()

    def paintEvent(self,event):
        p = QPainter()
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        self.scaledPix = self._pixMap.scaled(self.size(), Qt.KeepAspectRatio, transformMode = Qt.SmoothTransformation)
        p.drawPixmap(
                    int((self.width()-self.scaledPix.width())/2),
                    int((self.height()-self.scaledPix.height())/2),
                    self.scaledPix)
        p.end()

    def sizeHint(self):
        return QSize(int(self.scaledPix.width()),int(self.scaledPix.height()))

    def heightForWidth(self, width):
        return width * int(self.scaledPix.height()/self.scaledPix.width())




# APPLICATION TO TEST WIDGET
# ///////////////////////////////////////////////////////////////
class MainApp(QApplication):
    dti = DataInitializer
    def __init__(self, argv):
        super().__init__(argv)
        dtc = DataController()
        settings = Settings()
        self.settings = settings.items
        self.dti = DataInitializer(dtc,self.settings,self.initUI)

    def initUI(self):
        logging.warning("init UI")
        self.widget = ScaledHQPicture(self.dti.players[1].pixMap)
        self.widget.show() 
        logging.warning("show widget")



if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())      
                  